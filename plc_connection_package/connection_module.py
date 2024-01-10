
# connection_module.py
import pyads
from plc_connection_package.gui_module import update_gui_with_value, show_error_message

def open_connection(plc_address_input, plc_port_input, variable_path, root_tk):
    plc_address = plc_address_input.get()
    plc_port = int(plc_port_input.get())
    variable_name = variable_path.get()
    
    try:
        with pyads.Connection(plc_address, plc_port) as plc:
            value = plc.read_by_name(data_name=variable_name, plc_datatype=pyads.PLCTYPE_INT) 
            print(f"Połączenie z {plc_address}:{plc_port} ustanowione.")
            update_gui_with_value(value, variable_name, root_tk)
            
            # ...
    except pyads.ADSError as e:
        print(f"Nie udało się otworzyć połączenia: {e}")
        show_error_message(f"Nie udało się otworzyć połączenia: {e}", root_tk)