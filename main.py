from email_config.config import get_application

kodeson_app = get_application()

if __name__ == "__main__":
    kodeson_app.run(host='0.0.0.0', port=4000, fast=True)
