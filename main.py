from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = web_site_entry.get()
    email = mail_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are "
                                                          f"the details entered: \nEmail: "
                                                          f"{email}\nPassword: {password}\nIs it"
                                                          f" ok to save?")
    if is_ok:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
            web_site_entry.delete(0, END)
            password_entry.delete(0, END)
    else:
        messagebox.showinfo(title="Cancelled", message="Your password was not saved")
        web_site_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(60, 100, image=image)
canvas.grid(row=0, column=1)

# Labels
web_site_label = Label(text="Website:", font=("Arial", 12, "bold"))
web_site_label.grid(row=1, column=0)
mail_label = Label(text="Email/Username:", font=("Arial", 12, "bold"))
mail_label.grid(row=2, column=0)
password_label = Label(text="Password:", font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0)

# Entries
web_site_entry = Entry(width=35)
web_site_entry.grid(row=1, column=1, columnspan=2)
web_site_entry.focus()
mail_entry = Entry(width=35)
mail_entry.grid(row=2, column=1, columnspan=2)
mail_entry.insert(0, "narcissekabongongandu@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
generate_button = Button(text="Generate Password", font=("Arial", 11, "bold"), width=23)
generate_button.grid(row=4, column=1, columnspan=2)
add_button = Button(text="Add", font=("Arial", 11, "bold"), width=23, command=add_password)
add_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
