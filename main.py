from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # print(nr_numbers,nr_symbols,nr_letters)
    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_input.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    print("save")
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website)==0 or len(password)==0 or len(email) == 0:
        messagebox.showinfo(title='Oops',message='Do not leave any field empty.')
    else:
        is_ok = messagebox.askokcancel(title=website,message=f'These are the details entered: \nEmail: {email}\n'
                                                     f'Password: {password}\n'
                                                     f'Do you want to save?')
        if is_ok:
            with open("Password log",'a') as file_log:
                file_log.write(f"{website} | {email} | {password}\n")

                website_input.delete(0,END)
                email_input.delete(0, END)
                password_input.delete(0, END)
                website_input.focus()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.minsize(width=400,height=400)
window.config(padx = 50,pady =50)

canvas = Canvas(width=200,height=200)
logo_img = PhotoImage(file = 'logo.png')
canvas.create_image(100,100,image = logo_img)
canvas.grid(column = 1, row =0)

website_label = Label(text='Website:')
website_label.grid(column=0,row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0,row=2)

password_label = Label(text='Password:')
password_label.grid(column=0,row=3)

#entry
website_input = Entry(width=50)
website_input.grid(column = 1, row=1,columnspan=2)
website_input.focus()

email_input = Entry(width=50)
email_input.grid(column = 1, row=2,columnspan=2)

password_input = Entry(width=50)
password_input.grid(column = 1, row=3,columnspan=2)

#buttons

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(column = 2, row=3)

add_button = Button(text="Add",width=45, command=save)
add_button.grid(column = 1, row=4,columnspan=2)




window.mainloop()