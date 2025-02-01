def book_info(book_id):
    books = {
        101: "Python Programming - A Beginner's Guide",
        102: "Data Science with Python - Hands-on Projects",
        103: "Machine Learning Basics",
        104: "Deep Learning with TensorFlow",
        105: "Artificial Intelligence - Concepts and Applications",
        106: "Web Development with Django",
        107: "Cyber Security Essentials"
    }
    return books.get(book_id, "Book not found")

def buy_book(book_id):
    return f"You have successfully purchased {book_info(book_id)}."

def library_system():
    while True:
        print("\nWelcome to Skill Circle Library System")
        print("Press 1 for 101 Python Programming - A Beginner Guide")
        print("Press 2 for 102 Data Science with Python - Hands-on Projects")
        print("Press 3 for 103 Machine Learning Basics")
        print("Press 4 for 104 Deep Learning with TensorFlow")
        print("Press 5 for 105 Artificial Intelligence - Concepts and Applications")
        print("Press 6 for 106 Web Development with Django")
        print("Press 7 for 107 Cyber Security Essentials")
        print("Press 8 to Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print(f"Book Info: {book_info(101)}")
        elif choice == '2':
            print(buy_book(102))
        elif choice == '3':
            print(f"Book Info: {book_info(103)}")
        elif choice == '4':
            print(buy_book(104))
        elif choice == '5':
            print(f"Book Info: {book_info(105)}")
        elif choice == '6':
            print(buy_book(106))
        elif choice == '7':
            print(f"Book Info: {book_info(107)}")
        elif choice == '8':
            print("Thanks for visiting Skill Circle Library System!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        continue_choice = input("Do you want to continue? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("Thanks for visiting Skill Circle Library System!")
            break

if __name__ == "__main__":
    library_system()
