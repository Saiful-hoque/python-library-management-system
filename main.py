from library import Library
def main():
    library = Library()
    while True:
        print("=========================================")
        print("LIBRARY MANAGEMENT SYSTEM")
        print("=========================================")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Show All Books")
        print("6. Show All Members")
        print("7. Search Book")
        print("8. Exit")
        try:
            choice = input("Enter your choice: ").strip()
            if choice == '1':
                print("----- Add New Book -----")
                title = input("Enter Book Title : ").strip()
                author = input("Enter Author     : ").strip()
                isbn = input("Enter ISBN       : ").strip()
                library.add_book(title, author, isbn)
            elif choice == '2':
                print("----- Register Member -----")
                member_id = input("Enter Member ID : ").strip()
                name = input("Enter Name      : ").strip()
                try:
                    age = int(input("Enter Age       : ").strip())
                except ValueError:
                    print("Error: Invalid age input! Age must be an integer.")
                    input("Press Enter to continue...")
                    continue
                library.register_member(name, age, member_id)
            elif choice == '3':
                print("------ Borrow Book ------")
                member_id = input("Enter Member ID : ").strip()
                isbn = input("Enter Book ISBN : ").strip()
                library.borrow_book(member_id, isbn)
            elif choice == '4':
                print("------ Return Book ------")
                member_id = input("Enter Member ID : ").strip()
                isbn = input("Enter Book ISBN : ").strip()
                library.return_book(member_id, isbn)
            elif choice == '5':
                library.show_books()
            elif choice == '6':
                library.show_members()
            elif choice == '7':
                print("------ Search Book ------")
                title = input("Enter Book Title : ").strip()
                library.search_book(title)
            elif choice == '8':
                print("Thank you for using Library Management System.")
                print("Goodbye!")
                break
            else:
                print("Error: Invalid menu choice! Please select between 1 and 8.")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        input("Press Enter to continue...")
        print("\n" * 2)
if __name__ == "__main__":
    main()