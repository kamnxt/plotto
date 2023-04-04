# Plotto

Plotto is a simple Python script for real-time plotting of data received over a serial port. It uses matplotlib to plot the data on a graph that updates in real-time.

## Requirements

- Python 3.6 or later
- matplotlib

## Usage

```sh
python plotto.py [-h] [-n NUM_POINTS] [-p PORT] [-b BAUD_RATE]
```


- `-n NUM_POINTS`: the number of data points to display on the graph (default 500)
- `-p PORT`: the serial port to read data from (default "/dev/ttyACM\*")
- `-b BAUD_RATE`: the baud rate of the serial port (default 115200)

Example usage: `python plotto.py -n 1000 -p /dev/ttyUSB0 -b 9600`

## Credits

Code written by ChatGPT with help from kamnxt.

Enjoy and happy plotting! UwU

