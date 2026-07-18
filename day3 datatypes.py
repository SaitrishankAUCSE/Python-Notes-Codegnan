'''
Data types
            -->  to find datatype -- type(variable_name)
                 to find memory -- id(variable_name)
                 
                - int :- number = 9
                
                - float :- number = 89.45
                           print(type(num))

                - string :- . string is a sequence of characters that are inclosed in (' ', " ", ''' ''')
                            . string is immutable
                            
                            example: so = 'python is a language'
                                     for j in so:
                                     print(j)
                            
                            methods :- - replace()
                                            :- used to replace old string with new string
                                            :- syntax: variable_name.replace('old_str', 'new_str','how many')

                                             example: so = 'python is a language'
                                                      print(so.replace('python', 'java'))
                                                      print(so)
                                                      
                                   - join()
                                       :- this method will add the new character after every sub_string
                                       :- syntax: 'new_string'.join(variable_name)

                                       example: so = 'python is a language'
                                                print('-'.join(so))
                                                
                                   - split()
                                       :- syntax: variable_name.split("given_string")

                                       example: so = 'python is a language'
                                                print(so.split("is"))
                                                
                                   - index()
                                       :- displays only index numbers
                                       
                                       example: so = 'python is a language'
                                                print(so.index("a"))
                                   - count()
                                   
                                       example: so = 'python is a language'
                                                print(so.count('n',10,16))
                                   - indexing:
                                        :- syntax: variable_name[index]
                                   
                                       example: str = "hello everyone"
                                                print(str[0],str[1])
                                   
                                   - list
                                       :- list is the collection of different datatypes that are represented in [] and seperated by ,
                                       :- mutable datatype

                                       example: any_ = [1,'python',[2,['python',9],4],'java',['python',[56,78],'java',90]]
                                                print(any_[4][1][0])
                                                
                                                    methods :-
                                                                - append()
                                                                    :- this is used to add new item into the list and it will add at last index position

                                                                    example: any_ = [1,2,3,4,5]
                                                                             any_.append(10)
                                                                             print(any_)

                                                                - extend()

                                                                    example: any_ = [1,2,3,4,5]
                                                                             any_.append("python")
                                                                             print(any_)
                                                                             any_.extend("python")

                                                                - remove()
                                                                    :- the remove will delete the item based on the value given, if the given value not there in the list will show error

                                                                    example: any_ =[1,2,3,4,5]
                                                                             any_.remove(2)
                                                                             print(any_)

                                                                - pop()
                                                                    :- the pop will delete the item based on the index position given, if the index position is out of range in the list than it will show error

                                                                    example: any_ = [1,2,3,4,5]
                                                                             any_.pop(2)
                                                                             print(any_)

                                                                         

                                                                             


                                                
'''
any_ = [1,2,3,4,5]
any_.pop(2)
print(any_)
