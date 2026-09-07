#python --> everything is object in python
#Functions --> in python a fucntion can be passes as an argument to another fucntion, so they are first class objects
'''
email_id = "saketh@codegnan.com"
print(email_id[7:15])


email_ids = ['saketh@codegnan.com','bannu@codegnan.com','sai@codegnan.com','trishank@codegnan.com']
#print(len(email_ids))
#print(email_ids[1])
#print(email_ids[-2:])

#store 3 more mailids into above list, at once
email_ids.extend(['a@gmail.com','b@gmail.com','c@gmail,com'])
print(email_ids)

#access each mail id one by one --> Loops
email_ids = ['saketh@codegnan.com','bannu@codegnan.com','sai@codegnan.com','trishank@codegnan.com']
for email in email_ids:
    print(f'Mail Id of person is : {email}')

users = {}
email_ids = ['saketh@codegnan.com','bannu@codegnan.com','sai@codegnan.com','trishank@codegnan.com']
users.setdefault(('saketh@codegnan.com','bannu@codegnan.com','sai@codegnan.com','trishank@codegnan.com'))
print(users)

emails = ['saketh@codegnan.com','bannu@codegnan.com','sai@codegnan.com','trishank@codegnan.com']
users = {}
print(users)
for i in range(len(emails)):
    users[i+1] = emails[i]
print(users)
'''
#enumerate --> it provides by default a counter object(you can store in desired collection)
emails = ['saketh@codegnan.com','bannu@codegnan.com','sai@codegnan.com','trishank@codegnan.com']
data = dict(enumerate(emails))
print(data)
#Functions --> in python a fucntion can be passed as an argument to another fucntion or a fucntion can be written in another function, so they are called first class objects

# Set is an unordered collection, as we dont have indexing
# only ordered data types have indexing(list, tuple, dict), and unordered data types, dont have indexing(set)
