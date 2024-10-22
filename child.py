import os

fifo_name = 'my_fifo'

# Read from the FIFO
with open(fifo_name, 'r') as fifo:
    msg = fifo.read()  # Read message
    print(f"Child received: {msg}")
