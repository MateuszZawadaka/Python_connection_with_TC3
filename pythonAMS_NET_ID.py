import pyads
import customtkinter


root_tk = customtkinter.CTk()
root_tk.geometry("1920x1080")
root_tk.title("Twincat connection")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

plc_address_input = customtkinter.CTkEntry(master=root_tk, width=190, height=20, corner_radius=5, placeholder_text="PLC AMS_NET_ID:")
plc_address_input.place(relx=0.1, rely=0.15, anchor=customtkinter.CENTER)
plc_port_input = customtkinter.CTkEntry(master=root_tk, width=190, height=20, corner_radius=5, placeholder_text="PLC PORT:" )
plc_port_input.place(relx=0.1, rely=0.2, anchor=customtkinter.CENTER)
variabe_name = customtkinter.CTkEntry(master=root_tk, width=190, height=20, corner_radius=5, placeholder_text="Variable name:")
variabe_name.place(relx=0.1, rely=0.25, anchor=customtkinter.CENTER)
#plc_address= "192.168.17.156.1.1"
#, plc_port= 851
#variable_name = "GvlInputs.iVar"
def open_connection():
    plc_address = plc_address_input.get()
    plc_port = int(plc_port_input.get())
    variable_name = variabe_name.get()
    try:
        # Open a connection to the TwinCAT PLC
        with pyads.Connection(plc_address, plc_port) as plc:
            plc.open()
            # Your code here (e.g., read/write operations)
            value =  plc.read_by_name(data_name = variable_name, plc_datatype = pyads.PLCTYPE_INT) 
            print(f"Connection to {plc_address}:{plc_port} established.")
            variable_value = customtkinter.CTkLabel(master=root_tk, text=(f"Value of {variable_name}: {value}"), width=120, height=20, corner_radius=8, text_color="white", bg_color="blue")   
            variable_value.place(relx=0.4, rely=0.2, anchor=customtkinter.CENTER)
            
            # ...
    except pyads.ADSError as e:
        print(f"Failed to open connection: {e}")
        error_message_label = customtkinter.CTkLabel(master=root_tk, text=f"Failed to open connection: {e}", width=120, height=20, corner_radius=1, text_color="white", bg_color="red")
        error_message_label.place(relx=0.4, rely=0.05, anchor=customtkinter.CENTER)
        #clear_error_message_button = customtkinter.CTkButton(master=root_tk, text="Delete error message", corner_radius=10, command=error_message_label.after(1000, error_message_label.destroy()))
        #clear_error_message_button.place(relx = 0.4, rely = 0.1)

def button_pressed():
    open_connection()
    

def select_plc_parameters():
    print("Address: ",plc_address_input.get())
    print("Port: ", plc_port_input.get())

if __name__ == "__main__":
    select_plc_parameters_button = customtkinter.CTkButton(master=root_tk, text="Select PLC paramters", corner_radius=10, command=select_plc_parameters)
    select_plc_parameters_button.place(relx = 0.08, rely = 0.3, anchor=customtkinter.CENTER)
    button = customtkinter.CTkButton(master=root_tk, text="Read variable value", corner_radius=10, command=button_pressed)
    button.place(relx = 0.8, rely = 0.2, anchor=customtkinter.CENTER)
    
    root_tk.mainloop()


