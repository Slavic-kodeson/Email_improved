from sanic import json
from email_functions.compose_email import email_intership, email_applyjob, email_contact
from smtp_and_safe_calls.safe_call import safe_call, async_safe_call
from smtp_and_safe_calls.smpt_file import send_email


async def route_apply_job(request):
    emailMessage, mail_status_code = safe_call(email_applyjob, request, request.route.ctx.config_get)

    if not mail_status_code == 200:
        return json({"description": "Composing EmailObject failed.", "status": mail_status_code, "error": True})

    _, request_status_code = await async_safe_call(send_email, emailMessage, request.route.ctx.config_get)

    if not request_status_code == 200:
        return json({"description": "Request failed to SMTP API.", "status": request_status_code, "error": True})

    return json({"description": None, "status": request_status_code, "error": False})


async def route_contact_us(request):
    emailMessage, mail_status_code = safe_call(email_contact, request, request.route.ctx.config_get)

    if not mail_status_code == 200:
        return json({"description": "Composing EmailObject failed.", "status": mail_status_code, "error": True})

    _, request_status_code = await async_safe_call(send_email, emailMessage, request.route.ctx.config_get)

    if not request_status_code == 200:
        return json({"description": "Request failed to SMTP API.", "status": request_status_code, "error": True})

    return json({"description": None, "status": request_status_code, "error": False})


async def route_intership(request):
    emailMessage, mail_status_code = safe_call(email_intership, request, request.route.ctx.config_get)

    if not mail_status_code == 200:
        return json({"description": "Composing EmailObject failed.", "status": mail_status_code, "error": True})

    _, request_status_code = await async_safe_call(send_email, emailMessage, request.route.ctx.config_get)

    if not request_status_code == 200:
        return json({"description": "Request failed to SMTP API.", "status": request_status_code, "error": True})

    return json({"description": None, "status": request_status_code, "error": False})
