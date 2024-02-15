import shutil
import subprocess
import os

def create_file(filename):
    with open(filename, 'w'):
        pass
    print(f"File '{filename}' created.")

def delete_file(filename):
    os.remove(filename)
    print(f"File '{filename}' deleted.")

def move_file(source, destination):
    shutil.move(source, destination)
    print(f"File '{source}' moved to '{destination}'.")

def copy_file(source, destination):
    shutil.copy2(source, destination)
    print(f"File '{source}' copied to '{destination}'.")

def git_add(filename):
    subprocess.run(['git', 'add', filename])
    print(f"Added '{filename}' to Git.")

def git_commit(message):
    subprocess.run(['git', 'commit', '-m', message])
    print("Changes committed to Git.")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Create file")
        print("2. Delete file")
        print("3. Move file")
        print("4. Copy file")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            filename = input("Enter filename to create: ")
            create_file(filename)
            git_add(filename)
            git_commit("Added " + filename)
        elif choice == '2':
            filename = input("Enter filename to delete: ")
            delete_file(filename)
            git_commit("Deleted " + filename)
        elif choice == '3':
            source = input("Enter source filename: ")
            destination = input("Enter destination filename: ")
            move_file(source, destination)
            git_commit(f"Moved {source} to {destination}")
        elif choice == '4':
            source = input("Enter source filename: ")
            destination = input("Enter destination filename: ")
            copy_file(source, destination)
            git_add(destination)
            git_commit(f"Copied {source} to {destination}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
