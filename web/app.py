from market import app
import os

# Running the application in DEBUG mode

# docker run -p 5000:5000 -e DEBUG=1 flask_app_dev
# docker run -p 5000:5000 -e DEBUG=1 <image-name>

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('DEBUG')=='1')
    # app.run(debug=os.eviron.get('DEBUG')=='1')