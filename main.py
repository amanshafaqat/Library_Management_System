import tkinter as tk
from tkinter import messagebox


class Book:

    def __init__(self, title, author, isbn, download_size=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.download_size = download_size

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})" + (
            f" [eBook: {self.download_size}MB]" if self.download_size else "")


class LibraryApp:

    def __init__(self, root):
        self.books = []
        self.root = root
        self.root.title("Library Management System")

        # Title
        tk.Label(root, text="Book Title:").grid(row=0,
                                                column=0,
                                                sticky="e",
                                                padx=5,
                                                pady=5)
        self.title_entry = tk.Entry(root, width=30)
        self.title_entry.grid(row=0, column=1, pady=5)

        # Author
        tk.Label(root, text="Author:").grid(row=1,
                                            column=0,
                                            sticky="e",
                                            padx=5)
        self.author_entry = tk.Entry(root, width=30)
        self.author_entry.grid(row=1, column=1)

        # ISBN
        tk.Label(root, text="ISBN:").grid(row=2, column=0, sticky="e", padx=5)
        self.isbn_entry = tk.Entry(root, width=30)
        self.isbn_entry.grid(row=2, column=1)

        # eBook checkbox
        self.ebook_var = tk.IntVar()
        self.ebook_check = tk.Checkbutton(root,
                                          text="Is eBook?",
                                          variable=self.ebook_var,
                                          command=self.toggle_ebook)
        self.ebook_check.grid(row=3, column=0, columnspan=2, pady=5)

        # Download Size
        tk.Label(root, text="Download Size (MB):").grid(row=4,
                                                        column=0,
                                                        sticky="e",
                                                        padx=5)
        self.size_entry = tk.Entry(root, width=30)
        self.size_entry.grid(row=4, column=1)
        self.size_entry.config(state='disabled')

        # Add Book Button
        self.add_button = tk.Button(root,
                                    text="Add Book",
                                    command=self.add_book)
        self.add_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Output Area
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.grid(row=6, column=0, columnspan=2, padx=10)

    def toggle_ebook(self):
        if self.ebook_var.get():
            self.size_entry.config(state='normal')
        else:
            self.size_entry.delete(0, tk.END)
            self.size_entry.config(state='disabled')

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        isbn = self.isbn_entry.get()
        download_size = self.size_entry.get() if self.ebook_var.get() else None

        if self.ebook_var.get() and (not download_size.isdigit()):
            messagebox.showerror("Input Error",
                                 "Download size must be a number!")
            return

        book = Book(title, author, isbn, download_size)
        self.books.append(book)
        self.output_text.insert(tk.END, str(book) + "\n")


# Run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()
