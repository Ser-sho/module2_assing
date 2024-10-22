import sysv_ipc
import time

key = 1234  # Unique key for the message queue

# Create a message queue
mq = sysv_ipc.MessageQueue(key, sysv_ipc.IPC_CREX)  # Create queue with exclusive access

# Send a message
time.sleep(1)  # Wait for the child
mq.send(b'Hello from parent!')
print("Message sent from parent.")
