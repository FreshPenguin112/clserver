from flask import Flask

app = Flask(__name__)
@app.before_request
def before_request():
    print('hi')
    from cloudlink import cloudlink
    if __name__ == "__main__":
        cl = cloudlink() # Instanciate the parent cloudlink object
        server = cl.server(logs=True) # Initialize a new server object
        server.run(
            ip = "0.0.0.0",
            port = 3000
        )
@app.route('/')
def hello_world(): 
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
