import os
import time

fifo_name = 'my_fifo'

# Create a named pipe (FIFO) 
if not os.path.exists(fifo_name):
    os.mkfifo(fifo_name)

# Write to the FIFO
with open(fifo_name, 'w') as fifo:
    time.sleep(1)  # Wait for the child 
    fifo.write("Hello from parent!")  # Send message
