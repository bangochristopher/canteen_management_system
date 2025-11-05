import customtkinter as ctk
from database import create_tables

create_tables()  # ensure tables exist

app = ctk.CTk()
app.title("Canteen Management System")
app.geometry("500x300")

label = ctk.CTkLabel(app, text="Welcome to the Canteen System", font=("Arial", 18))
label.pack(pady=20)

app.mainloop()
