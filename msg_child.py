import sysv_ipc

key = 1234  # Unique key for the message queue

# Access the existing message queue
mq = sysv_ipc.MessageQueue(key)

# Receive the message
msg, _ = mq.receive()
print(f"Child received: {msg.decode()}")
