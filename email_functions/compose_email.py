from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def validate_file(filename, filesize, get_config_field):
    file_extension = filename.split('.')[-1] if "." in filename else None

    valid_extension: bool = file_extension in get_config_field("extensions")
    valid_filesize: bool = filesize <= get_config_field("filesize_max")

    return valid_extension & valid_filesize, file_extension


def email_subject(subject, body):

    email_message = MIMEMultipart()
    email_message.preamble = subject
    email_message["Subject"] = subject
    email_message["From"] = "vculev@kodeson.com"
    email_message["To"] = "vculev@kodeson.com"

    email_message.attach(MIMEText(body, 'plain', 'utf-8'))
    return email_message


def email_contact(request, sanic_config_get):
    request_dict = request.form
    get_field = request_dict.get

    email_content = f'''Company: {get_field("company")}
Name: {get_field("name")}
Phone: {get_field("phone")}
Email: {get_field("email")}
Interest: {get_field("interest")}
    
{get_field("message")}
'''

    _subject = f'Contact us {get_field("company")}'

    emailMessage = email_subject(_subject, email_content)

    return emailMessage, 200


def email_intership(request, sanic_config_get):
    request_dict = request.form
    get_field = request_dict.get

    email_content = f"""Name: {get_field("name")}
Phone: {get_field("phone")}
Email: {get_field("email")}
Job: {get_field("job")}

{get_field("message")}
    """

    _subject = f'Apply for Internship from {get_field("name")}'
    emailMessage = email_subject(_subject, email_content)

    return emailMessage, 200


def email_applyjob(request, sanic_config_get):
    request_dict = request.form
    get_field = request_dict.get

    emailMessage = MIMEMultipart()

    file_ref = request.files.get("file")

    if file_ref is not None:
        file_bytes = file_ref.body
        is_file_valid, extension = validate_file(file_ref.name, len(file_bytes) / 1_048_576, sanic_config_get)
        if is_file_valid is False:
            return None, 400

        filename = f'CV {get_field("name")}.{extension}'

        emailFile = MIMEApplication(file_bytes, Name=filename)
        emailFile['Content-Disposition'] = f'attachment; filename="{filename}"'

        emailMessage.attach(emailFile)

    email_content = f"""Name: {get_field("name")}
Phone: {get_field("phone")}
Email: {get_field("email")}
Job Position: {get_field("job")}
    
{get_field("message")}
    """

    _subject = f'{get_field("name")} - Applied for Job {get_field("job")}'
    emailMessage = email_subject(_subject, email_content)

    return emailMessage, 200
