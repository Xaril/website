# Main file used to start the interface

from app import app

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=80, use_reloader=False)
