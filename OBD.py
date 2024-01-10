import customtkinter
import obd

obdScanner_app = customtkinter.CTk()
obdScanner_app.geometry("640x400")
obdScanner_app.title("OBD Scanner")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

def obdOpenScanner():
    print("Working")
    #connection = OBD.OBD() # auto-connects to USB or RF port

    #cmd = OBD.commands.SPEED # select an OBD command (sensor)

    #response = connection.query(cmd) # send the command, and parse the response
    # ecu = obd.ECU.ENGINE.real.is_integer()
    #print(response.value) # returns unit-bearing values thanks to Pint
    #print(response.value.to("mph")) # user-friendly unit conversions



if __name__ == "__main__":
    obdOpenScanner()
    obdScanner_app.mainloop()