from app import create_app
import platform

app=create_app()

if __name__ == '__main__':
    if (platform.system() == 'Linux'):
        app.run(host='172.19.91.71', port=8667, debug=app.config['DEBUG'])
    else:
        app.run(host='0.0.0.0', debug=app.config['DEBUG'])