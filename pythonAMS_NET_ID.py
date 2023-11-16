import pyads
import customtkinter


root_tk = customtkinter.CTk()
root_tk.geometry("1024x700")
root_tk.title("Twincat connection")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

plc_address_input = customtkinter.CTkEntry(master=root_tk, width=190, height=20, corner_radius=5, placeholder_text="PLC AMS_NET_ID:")
plc_address_input.place(relx=0.1, rely=0.1, anchor=customtkinter.CENTER)
plc_port_input = customtkinter.CTkEntry(master=root_tk, width=190, height=20, corner_radius=5, placeholder_text="PLC PORT:" )
plc_port_input.place(relx=0.1, rely=0.2, anchor=customtkinter.CENTER)

def open_connection(plc_address= "192.168.17.156.1.1", plc_port= 851, variable_name = "GvlInputs.iVar"):
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
def button_pressed():
    open_connection()

def select_plc_parameters():
    print("Address: ",plc_address_input.get())
    print("Port: ", plc_port_input.get())

if __name__ == "__main__":
    select_plc_parameters_button = customtkinter.CTkButton(master=root_tk, text="Select PLC paramters", corner_radius=10, command=select_plc_parameters)
    select_plc_parameters_button.place(relx = 0.4, rely = 0.5, anchor=customtkinter.CENTER)
    button = customtkinter.CTkButton(master=root_tk, text="Read variable value", corner_radius=10, command=button_pressed)
    button.place(relx = 0.8, rely = 0.2, anchor=customtkinter.CENTER)
    root_tk.mainloop()
    # Replace '127.0.0.1.1.1' and 851 with the actual PLC IP address and port
    #open_connection(plc_address, plc_port)
    #read_twinCAT_variable(variable_name = "GvlInpus.iVar", plc_address = plc_address, plc_port = plc_port )


