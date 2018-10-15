"""
    Function to return the total cost of renting books
    Arguments:
    customer_name -- name of the customer renting books
    total_cost -- total cost to be paid
    cost_per_Day --cost of renting a book per day
    no_of_books_rented --total number of books rented
    no_of_days_rented --total days the book is rented
"""

class Book_Rental:
    def calculate_charge(self):
        total_no_of_days = input ("enter the number of days books"
            "have been borrowed")
        if total_no_of_days > 1:
           pass
        else:
            raise Exception("invalid input: Enter number of days"
                " greater than 1") 
        no_of_books_rented = int(input("enter the total"
                                        "number of books that"
                                        "were rented"))
        if no_of_books_rented > 0:
            pass
        else:
            raise Exception("invalid input: Enter number of books"
                " greater than 1") 

        total_cost = 0
        cost_per_day = 0
        return total_cost

class Book_Rental_Child(Book_Rental):
    def cost1(self):
        cost_per_day = 1
        total_cost = cost_per_day * \
            self.no_of_days_rented

    def cost2(self):
            book_type = input ("Enter the type of the book:"
                " R or r for Regular, F or f for Fiction, "
                "or N or n Novel ", 
                book_type )
            if book_type in {'r', 'R'}:
                cost_per_day = 1.5
                total_cost_for_regular = self.no_of_days_rented * \
                    cost_per_day
            elif book_type in {'f', 'F'}:
                cost_per_day = 3
                total_cost_for_fiction = self.no_of_days_rented *\
                    cost_per_day
            elif book_type in {'n', 'N'}:
                cost_per_day = 1.5
                total_cost_for_novel = self.no_of_days_rented *\
                    cost_per_day
            else:
                raise Exception('character is not R or r for Regular,'
                    ' F or f for Fiction'
                    'or N or n Novel : {}'.format(book_type))

            total_cost = total_cost_for_regular +\
                total_cost_for_fiction +\
                total_cost_for_novel

    def cost3(self):
        








    def total_rental_cost1(self):
        customer_name = input("Enter your names ")
        no_of_books_rented = int(input("enter the total"
                                      "number of books that"
                                      "were rented"))
        no_of_days_rented = int(input("enter the total"
                                      "number of days the"
                                      "book was rented"))
        cost_per_day = 1
        total_cost_per_day = cost_per_day * \
            no_of_books_rented
        total_cost = no_of_days_rented * \
            total_cost_per_day

        return customer_name, total_cost


#  library=Library(["The Last Battle","The Screwtape letters","The Great Divorce"])
#       student=Student()
#       done=False
#       while done==False:
#             print(""" ======LIBRARY MENU=======
#                   1. Display all available books
#                   2. Request a book
#                   3. Return a book
#                   4. Exit
#                   """)
#             choice=int(input("Enter Choice:"))
#             if choice==1:
#                         library.displayAvailablebooks()
#             elif choice==2:
#                         library.lendBook(student.requestBook())
#             elif choice==3:
#                         library.addBook(student.returnBook())
#             elif choice==4:
#                   sys.exit()
                  
# main()