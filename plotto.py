import serial
import argparse
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Real-time data plotter for Arduino serial output, written by ChatGPT with help from kamnxt.

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Plot data from Arduino')
parser.add_argument('-n', '--num-points', type=int, default=500,
                    help='number of data points to show on the plot')
parser.add_argument('-p', '--port', type=str, default=None,
                    help='serial port to use (default: use first available ttyACM port)')
parser.add_argument('-b', '--baud-rate', type=int, default=115200,
                    help='baud rate (default: 115200)')
args = parser.parse_args()

# Find serial port
if args.port is None:
    import glob
    ports = glob.glob('/dev/ttyACM*')
    if len(ports) == 0:
        print('No ttyACM ports found!')
        exit()
    port = ports[0]
else:
    port = args.port

# Set up serial connection
ser = serial.Serial(port, args.baud_rate)

# Set up plot
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_ylim(0, 1023)
ax.set_xlim(0, args.num_points)

# Define update function for animation
def update(frame):
    global data
    while ser.in_waiting:
        value = ser.readline().decode('utf-8').rstrip()
        data.append(float(value))
    data = data[-args.num_points:]
    line.set_data(range(len(data)), data)
    return line,

# Start animation
data = []
ani = FuncAnimation(fig, update, frames=None, blit=True, interval=50)

# Show plot
plt.show()

