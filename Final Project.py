import tkinter as tk
import webbrowser
from tkinter import messagebox

# Set pastel color palette
pastel_colors = ["#66CDAA", "#FDE68A", "#A7F3D0", "#BFDBFE", "#C4B5FD", "#FBCFE8", "#FFA54F","#CD6839","#71C671","#FFEFD5","#EEE8AA"]

# Create the main window
window = tk.Tk()
window.geometry("600x600")
window.title("Dental with Daisha")
window.configure(bg=pastel_colors[9])

# Set header label
header_label = tk.Label(window, text="Dental with Daisha", font=("Arial", 18, "bold"), bg=pastel_colors[9])
header_label.pack(fill=tk.X)

# Set sidebar frame
# Set sidebar frame
sidebar_frame = tk.Frame(window, bg=pastel_colors[0], borderwidth=2, relief=tk.SOLID)
sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)


# Set contact card frame
contact_card_frame = tk.Frame(window, bg="white")
contact_card_frame.pack(padx=20, pady=20)

# Function for validating name (no numbers allowed)
def validate_name(text):
    if text.isdigit():
        return False
    return True

# Function for validating email (using a simple regular expression)
def validate_email(text):
    import re
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, text) is not None

# Function for validating phone number (no letters allowed)
def validate_phone_number(text):
    if text.isalpha():
        return False
    return True

# Function to handle form submission
def submit_form():
    name = name_entry.get()
    phone_number = phone_entry.get()
    email = email_entry.get()
    dental_profession = dental_entry.get()
    desired_learnings = learnings_entry.get("1.0", tk.END)

    # Validate inputs
    if not validate_name(name):
        messagebox.showerror("Validation Error", "Name should not contain numbers.")
        return
    if not validate_email(email):
        messagebox.showerror("Validation Error", "Please enter a valid email.")
        return
    if not validate_phone_number(phone_number):
        messagebox.showerror("Validation Error", "Phone number should only contain numbers.")
        return

    # Display submitted information
    messagebox.showinfo("Contact Card", f"Name: {name}\nPhone Number: {phone_number}\nEmail: {email}\nDental Profession: {dental_profession}\nDesired Learnings: {desired_learnings}")

     # Create a new top-level window for the thank you message
    thank_you_window = tk.Toplevel(window)
    thank_you_window.geometry("200x100")
    thank_you_window.configure(bg=pastel_colors[1])
    thank_you_window.title("Thank You!")

    # Display the thank you message
    thank_you_label = tk.Label(thank_you_window, text="Thank You!", font=("Arial", 14, "bold"))
    thank_you_label.pack(pady=20)

    # Close the thank you window after 2 seconds
    thank_you_window.after(2000, thank_you_window.destroy)


# Clear entry fields
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    dental_entry.delete(0, tk.END)
    learnings_entry.delete("1.0", tk.END)
# Function to create new window with a specific header
def create_new_window(header_text):
    new_window = tk.Toplevel(window)
    new_window.geometry("400x400")
    new_window.title(header_text)
    
    # Set header label for the new window
    header_label = tk.Label(new_window, text=header_text, font=("Arial", 16, "bold"), bg=pastel_colors[0])
    header_label.pack(fill=tk.X)

# Create buttons in the sidebar
button_texts = ["1 on 1", "Modules", "Forum"]
for i, text in enumerate(button_texts):
    button = tk.Button(sidebar_frame, text=text, width=15, bg=pastel_colors[i+0], command=lambda t=text: create_new_window(t))
    button.pack(pady=10)
    button.config(cursor="hand2")

# Function to open default email client with recipient as daishahemmingway@gmail.com
def send_email():
    webbrowser.open("mailto:daishahemmingway@gmail.com")

# Set contact information in the sidebar
email_label = tk.Label(sidebar_frame, text="Email: daishahemmingway@gmail.com", bg=pastel_colors[1], fg="black", cursor="hand2")
email_label.pack(side=tk.BOTTOM, anchor=tk.SW, padx=10, pady=10)
button.config(cursor="hand2")

# Bind the click event to the email label
email_label.bind("<Button-1>", lambda event: send_email())

# Create the contact card form
name_label = tk.Label(contact_card_frame, text="Name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(contact_card_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(contact_card_frame, text="Phone Number:")
phone_label.grid(row=1, column=0, sticky="w")
phone_entry = tk.Entry(contact_card_frame)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(contact_card_frame, text="Email:")
email_label.grid(row=2, column=0, sticky="w")
email_entry = tk.Entry(contact_card_frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)

dental_label = tk.Label(contact_card_frame, text="Dental Profession:")
dental_label.grid(row=3, column=0, sticky="w")
dental_entry = tk.Entry(contact_card_frame)
dental_entry.grid(row=3, column=1, padx=5, pady=5)

learnings_label = tk.Label(contact_card_frame, text="Desired Learnings:")
learnings_label.grid(row=4, column=0, sticky="w")
learnings_entry = tk.Text(contact_card_frame, width=30, height=5)
learnings_entry.grid(row=4, column=1, padx=5, pady=5)

# Create submit button
submit_button = tk.Button(contact_card_frame, text="Submit", command=submit_form)
submit_button.grid(row=5, column=0, columnspan=2, pady=10)

###from PIL import ImageTk, Image###
#Dancing Tooth Image
# Load the tooth image
#tooth_image = Image.open("tooth.png")
#tooth_image = tooth_image.resize((50, 50))  # Resize the image if necessary

# Create a PhotoImage object from the tooth image
#tooth_photo = ImageTk.PhotoImage(tooth_image)

# Create a label for the tooth image
#tooth_label = tk.Label(window, image=tooth_photo)

# Function to move the tooth image
#def move_tooth(event):
    #x = event.x
    #y = event.y
    #tooth_label.place(x=x, y=y)

# Bind the mouse motion event to move the tooth
#window.bind("<Motion>", move_tooth)

# Pack the tooth label into the main window
#tooth_label.pack()


# Start the Tkinter event loop
window.mainloop()