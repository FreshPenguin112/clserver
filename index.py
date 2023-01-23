from flask import Flask
app = Flask(__name__)
import threading

threading.Thread(target=lambda a: app.run())
from cloudlink import cloudlink
if __name__ == "__main__":
    cl = cloudlink() # Instanciate the parent cloudlink object
    server = cl.server(logs=True) # Initialize a new server object
    
    # Do configuration here
    
    server.run(
        ip = "127.0.0.1", # Defaults to 127.0.0.1, use 0.0.0.0 to host on all interfaces
        port = 5000 # Defaults to port 3000
    )
