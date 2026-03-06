from tkinter import *
from tkinter import messagebox
import os

class User:
    def __init__(self, name):
        self.name = name

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class MiniBlogApp:
    def __init__(self, screen):
        self.screen = screen
        self.screen.title("MiniBlog App")
        self.screen.geometry("600x600")

        Label(screen, text="Name").pack()
        self.name_entry = Entry(screen)
        self.name_entry.pack()

        Label(screen, text="Post Title").pack()
        self.title_entry = Entry(screen)
        self.title_entry.pack()

        Label(screen, text="Post Content").pack()
        self.content_text = Text(screen, height=10, width=40)
        self.content_text.pack()

        Button(screen, text="Save Post", command=self.save_post).pack(pady=5)

        Label(screen, text="Saved Posts").pack()
        self.post_listbox = Listbox(screen)
        self.post_listbox.pack()

        Button(screen, text="Refresh Posts", command=self.load_posts).pack(pady=5)
        Button(screen, text="View Post", command=self.view_post).pack(pady=5)

    def save_post(self):
        try:
            name = self.name_entry.get()
            title = self.title_entry.get()
            content = self.content_text.get("1.0", END)

            if name == "" or title == "" or content.strip() == "":
                messagebox.showerror("Error", "All fields are required")
                return

            user = User(name)
            post = Post(title, content)

            filename = f"{user.name}_{post.title}.txt"

            with open(filename, "w") as file:
                file.write(post.content)

            messagebox.showinfo("Success", "Post saved successfully")
            self.load_posts()

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_posts(self):
        self.post_listbox.delete(0, END)
        files = [f for f in os.listdir() if f.endswith(".txt")]
        for file in files:
            self.post_listbox.insert(END, file)

    def view_post(self):
        try:
            selected = self.post_listbox.get(self.post_listbox.curselection())
            with open(selected, "r") as file:
                content = file.read()

            self.content_text.delete("1.0", END)
            self.content_text.insert(END, content)

        except:
            messagebox.showerror("Error", "Please select a post")

screen = Tk()
app = MiniBlogApp(screen)
screen.mainloop()