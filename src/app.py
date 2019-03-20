from flask import (
    Flask,
)

# Create the application instance
app = Flask(__name__)


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    """
    return "AdSets API root"


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run()
