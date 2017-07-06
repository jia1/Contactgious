from flask_mail import Mail, Message
import configparser, jinja2, re

# ENQUIRY TYPES
# Connect
# 0   General enquiry
# 1   General feedback
# Partnership
# 2   Collaboration and partnership
# 3   Marketing and sponsorship
# 4   Student-alumni relations
# Outreach
# 5   Event publicity
# 6   Recruitment notice
# Help
# 7   Academic advisory
# 8   Locker enquiry
# 9   IT support

enquiries = {
    '0': 'General enquiry',
    '1': 'General feedback',
    '2': 'Collaboration and partnership',
    '3': 'Marketing and sponsorship',
    '4': 'Student-alumni relations',
    '5': 'Event publicity',
    '6': 'Recruitment notice',
    '7': 'Academic advisory',
    '8': 'Locker enquiry',
    '9': 'IT support'
}

recipients = {
    '0': ['jiayeerawr@gmail.com'],
    '1': ['jiayeerawr@gmail.com'],
    '2': ['akashayami@yahoo.com.sg'],
    '3': ['akashayami@yahoo.com.sg'],
    '4': ['akashayami@yahoo.com.sg'],
    '5': ['jia10@u.nus.edu'],
    '6': ['jia10@u.nus.edu'],
    '7': ['l-jiayee@comp.nus.edu.sg'],
    '8': ['l-jiayee@comp.nus.edu.sg'],
    '9': ['infotech@nuscomputing.com', 'l-jiayee@comp.nus.edu.sg']
}

required_fields = ['enquiry', 'name', 'email', 'subject', 'message']
optional_fields = ['phone']

email_regex = re.compile(r"[^@]+@[^@]+")

validators = {
    'enquiry':  lambda x: x and len(x) == 1 and x.isdigit(),
    'name':     lambda x: x and 2 <= len(x) <= 32,
    'email':    lambda x: x and 6 <= len(x) <= 32 and email_regex.match(x),
    'phone':    lambda x: not x or 8 <= len(x) <= 16 and x.isdigit(),
    'subject':  lambda x: x and 4 <= len(x) <= 32,
    'message':  lambda x: x and 8 <= len(x) <= 500
}

def emeow(app, data):
    insider = configparser.ConfigParser()
    insider.read('himitsu.ini')

    app.config['MAIL_SERVER'] =     insider['emeow'].get('server')
    app.config['MAIL_PORT'] =       insider['emeow'].getint('port')
    app.config['MAIL_USERNAME'] =   insider['emeow'].get('sender')
    app.config['MAIL_PASSWORD'] =   insider['emeow'].get('password')
    app.config['MAIL_USE_SSL'] =    insider['emeow'].getboolean('ssl')
    app.config['MAIL_USE_TLS'] =    insider['emeow'].getboolean('tls')

    mailer = Mail(app)

    validated = is_valid(data)
    if validated:
        enquiry_id = data['enquiry']

        # flask_mail.Message(
        #    subject, recipients, body, html, sender, cc, bcc, reply_to,
        #    date, charset, extra_headers, mail_options, rcpt_options
        # )
        mail = Message(
            subject = "Connect: %s" % data['subject'],
            recipients = recipients[enquiry_id],
            sender = insider['emeow'].get('sender')
        )

        template = jinja2.Environment(
            trim_blocks = True,
            lstrip_blocks = True,
            autoescape = True,
            loader = jinja2.FileSystemLoader('templates')
        ).get_template('meow.html.j2')

        data['enquiry'] = enquiries[enquiry_id]
        mail.html = template.render(data)
        mailer.send(mail)
        return 'emeow: OK'
    else:
        return 'is_valid returns %s: %s' % validated
    

def is_valid(data):
    if data is None or type(data) is not dict:
        return (False, "Data is either None or not a dict.")
    else:
        for field in required_fields:
            if field not in data:
                return (False, "Missing field: %s." % field)
            elif not validate(field, data[field]):
                return (False, "Invalid value for the field: %s." % field)
        for field in optional_fields:
            if field not in data:
                continue
            elif not validate(field, data[field]):
                return (False, "Invalid value for the field: %s." % field)
        return (True, "Data is valid.")

def validate(field, value):
    return validators[field](value)
