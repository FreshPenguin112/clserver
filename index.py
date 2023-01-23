from cloudlink import cloudlink
if True:
    cl = cloudlink() # Instanciate the parent cloudlink object
    server = cl.server(logs=True) # Initialize a new server object
    server.run(
        ip = "localhost",
        port = 8080
    )
