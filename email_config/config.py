from sanic import Sanic
from json import load
from email_functions.routes import route_contact_us, route_intership, route_apply_job


def read_config() -> dict:
    file_handler = open("email_config/settings.json", "r")
    server_config = load(file_handler)
    file_handler.close()
    return server_config


def get_application():
    sanic_app = Sanic("KodesonAPI")
    sanic_app.config.update(
        read_config()
    )

    sanic_app.add_route(route_intership, "/api/intership", methods=["POST"], ctx_config_get=sanic_app.config.get)
    sanic_app.add_route(route_contact_us, "/api/contact", methods=["POST"], ctx_config_get=sanic_app.config.get)
    sanic_app.add_route(route_apply_job, "/api/careers", methods=["POST"], ctx_config_get=sanic_app.config.get)

    return sanic_app
