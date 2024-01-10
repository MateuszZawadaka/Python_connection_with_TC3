import pyads
import customtkinter
import time

root_tk = customtkinter.CTk()
root_tk.geometry("1920x1080")
root_tk.title("Twincat connection")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

plc_address_input = customtkinter.CTkEntry(master=root_tk, width=190, height=20, corner_radius=5, placeholder_text="PLC AMS_NET_ID:")
plc_address_input.place(relx=0.1, rely=0.15, anchor=customtkinter.CENTER)
plc_port_input = customtkinter.CTkEntry(master=root_tk, width=190, height=20, corner_radius=5, placeholder_text="PLC PORT:" )
plc_port_input.place(relx=0.1, rely=0.2, anchor=customtkinter.CENTER)
variable_path = customtkinter.CTkEntry(master=root_tk, width=190, height=20, corner_radius=5, placeholder_text="Variable name:")
variable_path.place(relx=0.1, rely=0.25, anchor=customtkinter.CENTER)

motor_velocity_variable_path = "Motor velocity variable path"
heater_temperature_variable_path = "Heater temperature variable path"
start_button_variable_path = "Start button variable path"
stop_button_variable_path = "Stop button variable path"

#value_to_write_input = customtkinter.CTkEntry(master=root_tk, width=190, height=20, corner_radius=5, placeholder_text="Value to wirite")
#value_to_write_input.place(relx=0.9, rely=0.27, anchor=customtkinter.CENTER)
motor_velocity_value_to_write = customtkinter.CTkEntry(master=root_tk, width=190, height=20, corner_radius=5, placeholder_text="Motor velocity: ")
motor_velocity_value_to_write.place(relx=0.8, rely=0.35)


def open_connection():
    plc_address = plc_address_input.get()
    plc_port = int(plc_port_input.get())
    variable_name = variable_path.get()
    try:
        with pyads.Connection(plc_address, plc_port) as plc:
            plc.open()
            value =  plc.read_by_name(data_name = variable_name, plc_datatype = pyads.PLCTYPE_INT) 
            print(f"Connection to {plc_address}:{plc_port} established.")
            variable_value = customtkinter.CTkLabel(master=root_tk, text=(f"Value of {variable_name}: {value}"), width=120, height=20, corner_radius=8, text_color="white", bg_color="blue")   
            variable_value.place(relx=0.4, rely=0.1, anchor=customtkinter.CENTER)
            
            # ...
    except pyads.ADSError as e:
        print(f"Failed to open connection: {e}")
        error_message_label = customtkinter.CTkLabel(master=root_tk, text=f"Failed to open connection: {e}", width=120, height=20, corner_radius=1, text_color="white", bg_color="red")
        error_message_label.place(relx=0.4, rely=0.05, anchor=customtkinter.CENTER)

def read_vadriable_value():
    open_connection()

def real_value_of_cpu_Usage(interval_s = 0.1):
    plc_address = "192.168.17.156.1.1" 
    plc_port = int(851)
    variable_name = "GvlOutputs.general.lrCpuUsage"
    try:
        with pyads.Connection(plc_address, plc_port) as plc:
            plc.open()
            value =  plc.read_by_name(data_name = variable_name, plc_datatype = pyads.PLCTYPE_LREAL) 
            print(f"Connection to {plc_address}:{plc_port} established.")
            cpu_suage = customtkinter.CTkLabel(master=root_tk, text=(f"Value of {variable_name}: {value}"), width=120, height=20, corner_radius=8, text_color="white", bg_color="blue")   
            cpu_suage.place(relx=0.4, rely=0.2, anchor=customtkinter.CENTER)
            time.sleep(interval_s)
    except pyads.ADSError as e:
        print(f"Failed to open connection: {e}")
        error_message_label = customtkinter.CTkLabel(master=root_tk, text=f"Failed to open connection: {e}", width=120, height=20, corner_radius=1, text_color="white", bg_color="red")
        error_message_label.place(relx=0.4, rely=0.05, anchor=customtkinter.CENTER)
    

# def write_data_to_variable():
#     plc_address = plc_address_input.get()
#     plc_port = int(plc_port_input.get())
#     variable_name = variable_path.get()
#     value_to_write = int(value_to_write_input.get())
#     try: 
#         with pyads.Connection(plc_address, plc_port) as plc:
#             plc.open()

#             result = plc.write_by_name(variable_name, int(value_to_write))

#             if result == 0:
#                 print(f"{variable_name} set to {value_to_write}")
#             else:
#                 print(f"Failed to write {variable_name}. Error code: {result}")

#     except pyads.ADSError as e:
#         print(f"Failed to open connection: {e}")
#         error_message_label = customtkinter.CTkLabel(master=root_tk, text=f"Failed to open connection: {e}", width=120, height=20, corner_radius=1, text_color="white", bg_color="red")
#         error_message_label.place(relx=0.4, rely=0.1, anchor=customtkinter.CENTER)

def write_motor_velocity():
    plc_address = plc_address_input.get()
    plc_port = int(plc_port_input.get())
    motor_velocity_variable_name = motor_velocity_variable_path
    motor_velocity_value = int(motor_velocity_value_to_write.get())
    try:
        with pyads.Connection(plc_address, plc_port) as plc:
            plc.open()

            result = plc.write_by_name(motor_velocity_variable_name, int(motor_velocity_value))
            if result == 0:
                print(f"{motor_velocity_variable_name} set to {motor_velocity_value}")
            
            else:
                print(f"Failed to write {motor_velocity_variable_name}. Error code: {result}")
    except pyads.ADSError as e:
        print(f"Failed to open connection: {e}")
        error_message_label = customtkinter.CTkLabel(master=root_tk, text=f"Failed to open connection: {e}", width=120, height=20, corner_radius=1, text_color="white", bg_color="red")
        error_message_label.place(relx=0.4, rely=0.1, anchor=customtkinter.CENTER)       


def select_plc_parameters():
    print("Address: ",plc_address_input.get())
    print("Port: ", plc_port_input.get())

def destroy():
    root_tk.destroy()

if __name__ == "__main__":
    interval = 0.1
    real_value_of_cpu_Usage(interval_s=interval)
    select_plc_parameters_button = customtkinter.CTkButton(master=root_tk, text="Select PLC paramters", corner_radius=10, command=select_plc_parameters)
    select_plc_parameters_button.place(relx = 0.1, rely = 0.3, anchor=customtkinter.CENTER)
    button = customtkinter.CTkButton(master=root_tk, text="Read variable value", corner_radius=10, command=read_vadriable_value)
    button.place(relx = 0.9, rely = 0.2, anchor=customtkinter.CENTER)
    destroy_button= customtkinter.CTkButton(master=root_tk, text="Exit", corner_radius=10, command=destroy)
    destroy_button.place(relx=0.9, rely=0.8)
    root_tk.mainloop()
