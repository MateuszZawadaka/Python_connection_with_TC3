import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def calculate_output(self, setpoint, process_variable):
        error = setpoint - process_variable
        self.integral += error
        derivative = error - self.prev_error

        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative

        self.prev_error = error
        return output

def simulate_system(pid_controller, setpoint, initial_value, time_end, time_step):
    time_values = np.arange(0, time_end, time_step)
    process_variable_values = []
    current_value = initial_value

    for time in time_values:
        control_signal = pid_controller.calculate_output(setpoint, current_value)

        # Simulate the system (here we assume a simple first-order system)
        process_variable_change = 0.1 * (control_signal - current_value)
        current_value += process_variable_change

        process_variable_values.append(current_value)

    return time_values, process_variable_values

def setpointGenerator():
    plt.clf()
    plt.plot(time_values, process_variable_change, label="setpointGenerator")
    plt.legend()
    fig, ax = plt.subplots()
    animation = FuncAnimation(fig, update, frames=range(400), interval=100)
    plt.show()
def main():
    # PID controller parameters
    Kp = 6
    Ki = 0.02
    Kd = 0.004

    # Simulation parameters
    setpoint = 200
    initial_value = 36
    time_end = 420
    time_step = 0.1

    pid_controller = PIDController(Kp, Ki, Kd)

    time_values, process_variable_values = simulate_system(pid_controller, setpoint, initial_value, time_end, time_step)

    # Plotting the results
    plt.plot(time_values, process_variable_values, label='Process Variable')
    plt.axhline(y=setpoint, color='r', linestyle='--', label='Setpoint')
    plt.xlabel('Time')
    plt.ylabel('Process Variable')
    plt.title('PID Control Simulation')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    setpointGenerator()
    main()
    