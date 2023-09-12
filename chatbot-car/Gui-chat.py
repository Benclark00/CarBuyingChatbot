'''Gui for car chatbot'''
import customtkinter
import chat.py

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x300")

def chat():
    print("Test")
    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label=customtkinter.CTkLabel(master=frame, text="Car Chatbot")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame)
entry1.pack(side= "bottom", anchor ="w", pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Send", command=respond)
button.pack(side="bottom", anchor="e", padx=8, pady=8)

root.mainloop()