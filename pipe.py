import os

# Create a pipe
r, w = os.pipe()

# Fork a child process
if os.fork() == 0:  # This block is executed by the child process
    os.close(w)  
    r = os.fdopen(r) 
    msg = r.read()  
    print(f"Child received: {msg}")
else:  # This block is executed by the parent process
    os.close(r)  
    w = os.fdopen(w, 'w')  
    w.write("Hello from parent!")  
    w.close()  
