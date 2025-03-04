from flask_mail import Message
from blog import cfg, mail
from flask import url_for

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Password Reset Request", sender=cfg.RESET_MAIL, recipients=[user.email])
    msg.body = f'''{url_for("auth_controller.reset_pass", token=token, _external=True)}
    :لاستعادة كلمة السر اضغط على الرابط التالي '''
    mail.send(msg)