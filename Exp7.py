import os 
def create_file(file_name):  
    try: 
        with open(file_name, 'w') as file: 
            file.write("This is the initial content of the file.\n") 
        print(f"File '{file_name}' created successfully.") 
    except Exception as e: 
        print(f"Error creating file: {e}") 
 
def read_file(file_name):  
    try: 
        with open(file_name, 'r') as file: 
            print(f"Contents of '{file_name}':\n{file.read()}") 
    except FileNotFoundError: 
        print(f"Error: File '{file_name}' not found.") 
    except Exception as e: 
        print(f"Error reading file: {e}") 
 
def update_file(file_name):  
    try: 
        with open(file_name, 'a') as file: 
            new_content = input("Enter content to add to the file: ") 
            file.write(new_content + "\n")  
 
        print(f"Content added to '{file_name}' successfully.") 
    except FileNotFoundError: 
        print(f"Error: File '{file_name}' not found.") 
    except Exception as e: 
        print(f"Error updating file: {e}") 
 
def delete_file(file_name): 
     
    try: 
        if os.path.exists(file_name): 
            os.remove(file_name) 
            print(f"File '{file_name}' deleted successfully.") 
        else: 
            print(f"Error: File '{file_name}' does not exist.") 
    except Exception as e: 
        print(f"Error deleting file: {e}") 
 
def main(): 
    while True: 
        print("\nMenu:") 
        print("1. Create a File") 
        print("2. Read a File") 
        print("3. Update a File") 
        print("4. Delete a File") 
        print("5. Exit") 
         
        choice = input("Enter your choice: ") 
         
        if choice == '1': 
            file_name = input("Enter the name of the file to create: ") 
            create_file(file_name) 
         
        elif choice == '2': 
            file_name = input("Enter the name of the file to read: ") 
            read_file(file_name) 
         
        elif choice == '3': 
            file_name = input("Enter the name of the file to update: ") 
            update_file(file_name) 
         
        elif choice == '4': 
            file_name = input("Enter the name of the file to delete: ") 
            delete_file(file_name) 
         
        elif choice == '5': 
            print("Exiting the program.") 
            break 
         
        else: 
            print("Invalid choice. Please try again.") 
 
if __name__ == "__main__": 
    main()
