import requests
from bs4 import BeautifulSoup
from datetime import date, timedelta
import json
import csv
import os


class Book:
    def __init__(self, book_id, title, price, rating,
                 availability, category="Unknown", url=""):
        self.book_id = str(book_id)
        self.title = title
        self.price = float(price)
        self.rating = rating
        self.availability = availability
        self.category = category
        self.url = url

        self.issued = False
        self.issued_to = None
        self.issue_date = None

    def display(self):
        print("\n----------------------------------------")
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Price: £", self.price)
        print("Rating:", self.rating)
        print("Category:", self.category)
        print("Availability:", self.availability)

        if self.issued:
            print("Library Status: Issued")
            print("Issued To:", self.issued_to)
            print("Issue Date:", self.issue_date)
        else:
            print("Library Status: Available")

        print("URL:", self.url)


class Member:
    def __init__(self, member_id, name, phone=""):
        self.member_id = str(member_id)
        self.name = name
        self.phone = phone
        self.issued_books = []
        self.history = []

    def display(self):
        print("\n----------------------------------------")
        print("Member ID:", self.member_id)
        print("Name:", self.name)
        print("Phone:", self.phone)

        if not self.issued_books:
            print("Issued Books: None")
        else:
            print("Issued Books:", len(self.issued_books))
            for book_id in self.issued_books:
                print("  -", book_id)


class BookScraper:
    def __init__(self):
        self.base_url = "https://books.toscrape.com/"
        self.books = []

        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 LibraryManagementSystem"
        })

    def scrape_books(self):
        self.books = []

        print("\n========================================")
        print("       BOOKS TO SCRAPE IMPORT")
        print("========================================")
        print("Scraping books...")
        print("Please wait...\n")

        url = self.base_url
        book_number = 1

        while url:
            try:
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
            except requests.exceptions.RequestException as error:
                print("\nConnection error:", error)
                print("Scraping stopped.")
                break

            soup = BeautifulSoup(response.text, "html.parser")

            products = soup.find_all(
                "article",
                class_="product_pod"
            )

            for product in products:
                title = product.find("h3").find("a")["title"]

                price_text = product.find(
                    "p",
                    class_="price_color"
                ).text.strip().replace("£", "")

                try:
                    price = float(price_text)
                except ValueError:
                    price = 0.0

                availability = product.find(
                    "p",
                    class_="instock availability"
                ).text.strip()

                rating_tag = product.find(
                    "p",
                    class_="star-rating"
                )

                rating = rating_tag.get("class")[1]

                link = product.find("h3").find("a")["href"]
                book_url = self.get_full_url(link)

                self.books.append({
                    "book_id": str(book_number),
                    "title": title,
                    "price": price,
                    "rating": rating,
                    "availability": availability,
                    "category": "Unknown",
                    "url": book_url
                })

                book_number += 1

            print("Books scraped:", len(self.books))

            next_button = soup.find("li", class_="next")

            if next_button:
                next_link = next_button.find("a")["href"]
                current_url = url.rsplit("/", 1)[0] + "/"
                url = current_url + next_link
            else:
                url = None

        print("\nTotal books scraped:", len(self.books))
        return self.books

    def get_full_url(self, link):
        if link.startswith("http"):
            return link

        link = link.replace("../", "")
        return self.base_url + "catalogue/" + link


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

        self.due_days = 14
        self.fine_per_day = 10
        self.max_books_per_member = 3

    def load_books(self, books_data):
        for data in books_data:
            book = Book(
                data["book_id"],
                data["title"],
                data["price"],
                data["rating"],
                data["availability"],
                data.get("category", "Unknown"),
                data.get("url", "")
            )
            self.books[book.book_id] = book

    def add_book(self):
        print("\n========== ADD BOOK ==========")

        book_id = input("Enter Book ID: ").strip()

        if book_id in self.books:
            print("Book ID already exists.")
            return

        title = input("Enter Book Title: ").strip()

        while True:
            try:
                price = float(input("Enter Price: "))
                if price < 0:
                    raise ValueError
                break
            except ValueError:
                print("Enter a valid positive price.")

        rating = input("Enter Rating: ").strip()
        category = input("Enter Category: ").strip()

        book = Book(
            book_id,
            title,
            price,
            rating,
            "In stock",
            category,
            "Added manually"
        )

        self.books[book_id] = book
        print("Book added successfully.")

    def view_books(self):
        print("\n========== VIEW BOOKS ==========")

        if not self.books:
            print("No books found.")
            return

        books = list(self.books.values())
        page_size = 10

        for start in range(0, len(books), page_size):
            end = min(start + page_size, len(books))

            for book in books[start:end]:
                book.display()

            if end == len(books):
                break

            choice = input(
                "\nShow next page? (y/n): "
            ).lower()

            if choice != "y":
                break

    def search_book(self):
        print("\n========== SEARCH BOOK ==========")

        search = input(
            "Enter title / ID / keyword: "
        ).strip().lower()

        found = []

        for book in self.books.values():
            if (
                search == book.book_id.lower()
                or search in book.title.lower()
                or search in book.category.lower()
            ):
                found.append(book)

        if not found:
            print("No matching books found.")
            return

        print("\nFound", len(found), "book(s).")

        for book in found:
            book.display()

    def filter_books(self):
        print("\n========== FILTER BOOKS ==========")
        print("1. Price greater than")
        print("2. Price less than")
        print("3. Rating")
        print("4. Available only")
        print("5. Category")

        choice = input("Enter choice: ")
        result = []

        if choice == "1":
            try:
                value = float(input("Price greater than: "))
            except ValueError:
                print("Invalid price.")
                return

            result = [
                book for book in self.books.values()
                if book.price > value
            ]

        elif choice == "2":
            try:
                value = float(input("Price less than: "))
            except ValueError:
                print("Invalid price.")
                return

            result = [
                book for book in self.books.values()
                if book.price < value
            ]

        elif choice == "3":
            rating = input(
                "Enter rating (One/Two/Three/Four/Five): "
            ).strip().lower()

            result = [
                book for book in self.books.values()
                if book.rating.lower() == rating
            ]

        elif choice == "4":
            result = [
                book for book in self.books.values()
                if not book.issued
            ]

        elif choice == "5":
            category = input(
                "Enter category: "
            ).strip().lower()

            result = [
                book for book in self.books.values()
                if category in book.category.lower()
            ]

        else:
            print("Invalid choice.")
            return

        if not result:
            print("No books match the filter.")
            return

        print("\nMatching books:", len(result))

        for book in result:
            print(
                book.book_id,
                "-",
                book.title,
                "- £",
                book.price
            )

    def sort_books(self):
        print("\n========== SORT BOOKS ==========")
        print("1. Price Low to High")
        print("2. Price High to Low")
        print("3. Title A-Z")
        print("4. Rating High to Low")

        choice = input("Enter choice: ")
        books = list(self.books.values())

        if choice == "1":
            books.sort(key=lambda book: book.price)

        elif choice == "2":
            books.sort(
                key=lambda book: book.price,
                reverse=True
            )

        elif choice == "3":
            books.sort(
                key=lambda book: book.title.lower()
            )

        elif choice == "4":
            rating_order = {
                "One": 1,
                "Two": 2,
                "Three": 3,
                "Four": 4,
                "Five": 5
            }

            books.sort(
                key=lambda book:
                rating_order.get(book.rating, 0),
                reverse=True
            )

        else:
            print("Invalid choice.")
            return

        for book in books[:50]:
            print(
                book.book_id,
                "|",
                book.title,
                "|",
                book.rating,
                "| £",
                book.price
            )

        if len(books) > 50:
            print("\nShowing first 50 results.")

    def delete_book(self):
        print("\n========== DELETE BOOK ==========")

        book_id = input("Enter Book ID: ").strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if book.issued:
            print("Book is currently issued.")
            return

        confirm = input(
            "Delete this book? (y/n): "
        ).lower()

        if confirm == "y":
            del self.books[book_id]
            print("Book deleted successfully.")

    def register_member(self):
        print("\n========== REGISTER MEMBER ==========")

        member_id = input(
            "Enter Member ID: "
        ).strip()

        if member_id in self.members:
            print("Member already exists.")
            return

        name = input(
            "Enter Member Name: "
        ).strip()

        phone = input(
            "Enter Phone: "
        ).strip()

        self.members[member_id] = Member(
            member_id,
            name,
            phone
        )

        print("Member registered successfully.")

    def view_members(self):
        print("\n========== VIEW MEMBERS ==========")

        if not self.members:
            print("No members found.")
            return

        for member in self.members.values():
            member.display()

    def member_details(self):
        print("\n========== MEMBER DETAILS ==========")

        member_id = input(
            "Enter Member ID: "
        ).strip()

        if member_id not in self.members:
            print("Member not found.")
            return

        self.members[member_id].display()

    def issue_book(self):
        print("\n========== ISSUE BOOK ==========")

        book_id = input(
            "Enter Book ID: "
        ).strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if book.issued:
            print("Book is already issued.")
            return

        member_id = input(
            "Enter Member ID: "
        ).strip()

        if member_id not in self.members:
            print("Member not found.")
            return

        member = self.members[member_id]

        if len(member.issued_books) >= self.max_books_per_member:
            print(
                "Member has reached the maximum book limit:",
                self.max_books_per_member
            )
            return

        book.issued = True
        book.issued_to = member_id
        book.issue_date = date.today()

        member.issued_books.append(book_id)

        member.history.append({
            "book_id": book_id,
            "action": "Issued",
            "date": str(date.today())
        })

        due_date = (
            date.today()
            + timedelta(days=self.due_days)
        )

        print("\nBook issued successfully.")
        print("Title:", book.title)
        print("Member:", member.name)
        print("Issue Date:", book.issue_date)
        print("Due Date:", due_date)

    def calculate_fine(self, book):
        if book.issue_date is None:
            return 0

        issue_date = date.fromisoformat(
            str(book.issue_date)
        )

        total_days = (
            date.today() - issue_date
        ).days

        late_days = total_days - self.due_days

        if late_days <= 0:
            return 0

        return late_days * self.fine_per_day

    def return_book(self):
        print("\n========== RETURN BOOK ==========")

        book_id = input(
            "Enter Book ID: "
        ).strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if not book.issued:
            print("Book is not currently issued.")
            return

        fine = self.calculate_fine(book)
        member_id = book.issued_to

        if member_id in self.members:
            member = self.members[member_id]

            if book_id in member.issued_books:
                member.issued_books.remove(book_id)

            member.history.append({
                "book_id": book_id,
                "action": "Returned",
                "date": str(date.today()),
                "fine": fine
            })

        print("\n========== RETURN DETAILS ==========")
        print("Book:", book.title)
        print("Issued To:", member_id)
        print("Fine: ₹", fine)

        book.issued = False
        book.issued_to = None
        book.issue_date = None

        print("Book returned successfully.")

    def view_issued_books(self):
        print("\n========== ISSUED BOOKS ==========")

        found = False

        for book in self.books.values():
            if book.issued:
                found = True

                issue_date = date.fromisoformat(
                    str(book.issue_date)
                )

                due_date = (
                    issue_date
                    + timedelta(days=self.due_days)
                )

                print("\nBook ID:", book.book_id)
                print("Title:", book.title)
                print("Issued To:", book.issued_to)
                print("Issue Date:", book.issue_date)
                print("Due Date:", due_date)
                print(
                    "Current Fine: ₹",
                    self.calculate_fine(book)
                )

        if not found:
            print("No books are currently issued.")

    def show_fine(self):
        print("\n========== FINE DETAILS ==========")

        book_id = input(
            "Enter Book ID: "
        ).strip()

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]

        if not book.issued:
            print("Book is available.")
            print("Fine: ₹0")
            return

        fine = self.calculate_fine(book)

        issue_date = date.fromisoformat(
            str(book.issue_date)
        )

        due_date = (
            issue_date
            + timedelta(days=self.due_days)
        )

        print("Book:", book.title)
        print("Issue Date:", issue_date)
        print("Due Date:", due_date)
        print("Fine: ₹", fine)

    def member_history(self):
        print("\n========== MEMBER HISTORY ==========")

        member_id = input(
            "Enter Member ID: "
        ).strip()

        if member_id not in self.members:
            print("Member not found.")
            return

        history = self.members[member_id].history

        if not history:
            print("No transaction history.")
            return

        for item in history:
            print(item)

    def statistics(self):
        print("\n========== LIBRARY STATISTICS ==========")

        total_books = len(self.books)
        issued_books = sum(
            1 for book in self.books.values()
            if book.issued
        )
        available_books = (
            total_books - issued_books
        )

        total_value = sum(
            book.price for book in self.books.values()
        )

        print("Total Books:", total_books)
        print("Available Books:", available_books)
        print("Issued Books:", issued_books)
        print("Total Members:", len(self.members))
        print(
            "Catalogue Value: £",
            round(total_value, 2)
        )
        print("Due Days:", self.due_days)
        print(
            "Fine Per Late Day: ₹",
            self.fine_per_day
        )

    def export_csv(self):
        filename = "library_books.csv"

        try:
            with open(
                filename,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Book ID",
                    "Title",
                    "Price",
                    "Rating",
                    "Category",
                    "Availability",
                    "Issued",
                    "Issued To",
                    "Issue Date",
                    "URL"
                ])

                for book in self.books.values():
                    writer.writerow([
                        book.book_id,
                        book.title,
                        book.price,
                        book.rating,
                        book.category,
                        book.availability,
                        book.issued,
                        book.issued_to,
                        book.issue_date,
                        book.url
                    ])

            print(
                "\nExported successfully:",
                filename
            )

        except Exception as error:
            print("Export failed:", error)

    def save_data(self):
        data = {
            "due_days": self.due_days,
            "fine_per_day": self.fine_per_day,
            "max_books_per_member":
                self.max_books_per_member,
            "books": {},
            "members": {}
        }

        for book_id, book in self.books.items():
            data["books"][book_id] = {
                "book_id": book.book_id,
                "title": book.title,
                "price": book.price,
                "rating": book.rating,
                "availability": book.availability,
                "category": book.category,
                "url": book.url,
                "issued": book.issued,
                "issued_to": book.issued_to,
                "issue_date": (
                    str(book.issue_date)
                    if book.issue_date
                    else None
                )
            }

        for member_id, member in self.members.items():
            data["members"][member_id] = {
                "member_id": member.member_id,
                "name": member.name,
                "phone": member.phone,
                "issued_books": member.issued_books,
                "history": member.history
            }

        try:
            with open(
                "library_data.json",
                "w",
                encoding="utf-8"
            ) as file:
                json.dump(
                    data,
                    file,
                    indent=4
                )

            print("Library data saved successfully.")

        except Exception as error:
            print("Save failed:", error)

    def load_data(self):
        filename = "library_data.json"

        if not os.path.exists(filename):
            return False

        try:
            with open(
                filename,
                "r",
                encoding="utf-8"
            ) as file:
                data = json.load(file)

            self.due_days = data.get(
                "due_days",
                14
            )

            self.fine_per_day = data.get(
                "fine_per_day",
                10
            )

            self.max_books_per_member = data.get(
                "max_books_per_member",
                3
            )

            self.books = {}

            for book_id, item in data.get(
                "books", {}
            ).items():

                book = Book(
                    item["book_id"],
                    item["title"],
                    item["price"],
                    item["rating"],
                    item["availability"],
                    item.get(
                        "category",
                        "Unknown"
                    ),
                    item.get(
                        "url",
                        ""
                    )
                )

                book.issued = item.get(
                    "issued",
                    False
                )

                book.issued_to = item.get(
                    "issued_to"
                )

                book.issue_date = item.get(
                    "issue_date"
                )

                self.books[book_id] = book

            self.members = {}

            for member_id, item in data.get(
                "members", {}
            ).items():

                member = Member(
                    item["member_id"],
                    item["name"],
                    item.get("phone", "")
                )

                member.issued_books = item.get(
                    "issued_books",
                    []
                )

                member.history = item.get(
                    "history",
                    []
                )

                self.members[member_id] = member

            return True

        except Exception as error:
            print("Load failed:", error)
            return False


def book_management(library):
    while True:
        print("\n================================")
        print("       BOOK MANAGEMENT")
        print("================================")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Filter Books")
        print("5. Sort Books")
        print("6. Delete Book")
        print("7. Export CSV")
        print("8. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.filter_books()
        elif choice == "5":
            library.sort_books()
        elif choice == "6":
            library.delete_book()
        elif choice == "7":
            library.export_csv()
        elif choice == "8":
            break
        else:
            print("Invalid choice.")


def member_management(library):
    while True:
        print("\n================================")
        print("      MEMBER MANAGEMENT")
        print("================================")
        print("1. Register Member")
        print("2. View Members")
        print("3. Member Details")
        print("4. Member History")
        print("5. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.register_member()
        elif choice == "2":
            library.view_members()
        elif choice == "3":
            library.member_details()
        elif choice == "4":
            library.member_history()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


def settings_menu(library):
    while True:
        print("\n================================")
        print("           SETTINGS")
        print("================================")
        print("1. Change Due Days")
        print("2. Change Fine Per Day")
        print("3. Change Maximum Books")
        print("4. Back")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                days = int(input("Enter due days: "))

                if days > 0:
                    library.due_days = days
                    print("Due days updated.")
                else:
                    print("Enter a positive number.")
            except ValueError:
                print("Invalid value.")

        elif choice == "2":
            try:
                fine = float(
                    input(
                        "Enter fine per late day: "
                    )
                )

                if fine >= 0:
                    library.fine_per_day = fine
                    print("Fine updated.")
                else:
                    print("Invalid value.")
            except ValueError:
                print("Invalid value.")

        elif choice == "3":
            try:
                limit = int(
                    input(
                        "Enter maximum books per member: "
                    )
                )

                if limit > 0:
                    library.max_books_per_member = limit
                    print("Maximum book limit updated.")
                else:
                    print("Invalid value.")
            except ValueError:
                print("Invalid value.")

        elif choice == "4":
            break

        else:
            print("Invalid choice.")


def refresh_books(library):
    print("\nRefreshing book catalogue...")

    scraper = BookScraper()
    books_data = scraper.scrape_books()

    if not books_data:
        print("Refresh failed.")
        return

    old_books = library.books

    library.books = {}
    library.load_books(books_data)

    for book_id, old_book in old_books.items():
        if book_id in library.books:
            new_book = library.books[book_id]

            new_book.issued = old_book.issued
            new_book.issued_to = old_book.issued_to
            new_book.issue_date = old_book.issue_date

    library.save_data()

    print("\nCatalogue refreshed successfully.")


def main():
    print("\n==========================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("==========================================")
    print("Source: Books to Scrape")

    library = Library()

    if library.load_data():
        print(
            "\nLoaded",
            len(library.books),
            "books from saved data."
        )
    else:
        print("\nNo saved library found.")

        scraper = BookScraper()
        books_data = scraper.scrape_books()

        if not books_data:
            print("No books could be loaded.")
            return

        library.load_books(books_data)
        library.save_data()

    while True:
        print("\n==========================================")
        print("              MAIN MENU")
        print("==========================================")
        print("1. Book Management")
        print("2. Member Management")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. View Issued Books")
        print("6. Calculate Fine")
        print("7. Library Statistics")
        print("8. Settings")
        print("9. Save Data")
        print("10. Refresh Books From Website")
        print("11. Export Books CSV")
        print("12. Exit")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_management(library)

        elif choice == "2":
            member_management(library)

        elif choice == "3":
            library.issue_book()

        elif choice == "4":
            library.return_book()

        elif choice == "5":
            library.view_issued_books()

        elif choice == "6":
            library.show_fine()

        elif choice == "7":
            library.statistics()

        elif choice == "8":
            settings_menu(library)

        elif choice == "9":
            library.save_data()

        elif choice == "10":
            refresh_books(library)

        elif choice == "11":
            library.export_csv()

        elif choice == "12":
            library.save_data()

            print("\nThank You!")
            print("Library Management System Closed.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()