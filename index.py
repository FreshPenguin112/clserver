app = "hi"
from cloudlink import cloudlink
if __name__ == "__main__":
    cl = cloudlink() # Instanciate the parent cloudlink object
    server = cl.server(logs=True) # Initialize a new server object
    
    # Do configuration here
    
    server.run(
        ip = "localhost", # Defaults to 127.0.0.1, use 0.0.0.0 to host on all interfaces
        port = 3000 # Defaults to port 3000
    )
    
    # server.run() is blocking,
    # no further code will execute unless a CTRL+C, SIGTERM, or SIGKILL is detected.
