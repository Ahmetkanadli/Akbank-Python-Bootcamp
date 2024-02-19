import tkinter as tk
from tkinter import messagebox
import tkinter.simpledialog


    

class LibraryApp:
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")

        self.library = Library()

        self.label = tk.Label(master, text="Welcome to Library Management System", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.list_button = tk.Button(master, text="List Books", command=self.list_books)
        self.list_button.pack(pady=5)

        self.add_button = tk.Button(master, text="Add Book", command=self.add_book)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(master, text="Remove Book", command=self.remove_book)
        self.remove_button.pack(pady=5)

        self.exit_button = tk.Button(master, text="Exit", command=master.quit)
        self.exit_button.pack(pady=5)

    def list_books(self):
       # messagebox.showinfo("List Books", self.library.list_books())
        book_list = self.library.list_books()

        list_window = tk.Toplevel(self.master)
        list_window.title("List Books")

        list_label = tk.Label(list_window, text=book_list)
        list_label.pack(pady=10) 
        
    def add_book(self):
        ısbn = tk.simpledialog.askstring("Add Book", "ISBN")
        title = tk.simpledialog.askstring("Add Book", "Enter book title:")
        author = tk.simpledialog.askstring("Add Book", "Enter book author:")
        release_year = tk.simpledialog.askstring("Add Book", "Enter release year:")
        num_pages = tk.simpledialog.askstring("Add Book", "Enter number of pages:")

        if title and author and release_year and num_pages and ısbn:
            self.library.add_book(ısbn,title, author, release_year, num_pages)
            messagebox.showinfo("Add Book", "Book added successfully.")
        else:
            messagebox.showerror("Error", "All fields are required.")

    def remove_book(self):
        title = tk.simpledialog.askstring("Remove Book", "Enter the ISBN of the book to be removed:")
        if title:
            result = self.library.remove_book(title)
            if result:
                messagebox.showinfo("Remove Book", "Book removed successfully.")
            else:
                messagebox.showerror("Remove Book", "Book not found.")
        else:
            messagebox.showerror("Error", "Please enter a book title.")

class Library:
    def __init__(self):
        self.file_name = "books.txt"

    def list_books(self):
        try:
            with open(self.file_name, "r") as file:
                lines = file.readlines()
                book_list = ""
                for line in lines:
                    book_info = line.strip().split(',')
                    book_list += f"ISBN: {book_info[0]} Book: {book_info[1]}, Author: {book_info[2]}, Release Year: {book_info[3]}, Pages: {book_info[4]}\n"
                return book_list
        except FileNotFoundError:
            return "The library is currently empty."

    def add_book(self, ısbn,title, author, release_year, num_pages):
        book_info = f"{ısbn},{title},{author},{release_year},{num_pages}\n"
        with open(self.file_name, "a+") as file:
            file.write(book_info)

    def remove_book(self, title):
        try:
            with open(self.file_name, "r") as file:
                lines = file.readlines()
                books = [line.strip() for line in lines]
                for book in books:
                    if book.split(',')[0] == title:
                        books.remove(book)
                        break
                else:
                    return False
            with open(self.file_name, "w") as file:
                for book in books:
                    file.write(book + '\n')
            return True
        except FileNotFoundError:
            return False

def main():
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
