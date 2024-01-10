# gui_module.py
import customtkinter

def update_gui_with_value(value, variable_name, root_tk):
    variable_value = customtkinter.CTkLabel(master=root_tk, text=f"Wartość {variable_name}: {value}", width=120, height=20, corner_radius=8, text_color="white", bg_color="blue")   
    variable_value.place(relx=0.4, rely=0.1, anchor=customtkinter.CENTER)

def show_error_message(message, root_tk):
    error_message_label = customtkinter.CTkLabel(master=root_tk, text=message, width=120, height=20, corner_radius=1, text_color="white", bg_color="red")
    error_message_label.place(relx=0.4, rely=0.05, anchor=customtkinter.CENTER)