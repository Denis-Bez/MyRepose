from config import CONFIG

from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message

application = Flask (__name__)

title = {
    "index": "ЭНЕРГО group Экспертиза - Энергия в руках профессионалов",
    "services": "Заказать экспертизу электротехнических работ и оборудования",
    "experts": "Эксперты в области электротехнических работ",
    "contacts": "Отправьте заявку и мы с вами свяжемся"
}

application.config["MAIL_DEFAULT_SENDER"] = CONFIG["MAIL_DEFAULT_SENDER"]
application.config["MAIL_PASSWORD"] = CONFIG["MAIL_PASSWORD"]
application.config["MAIL_PORT"] = 465
application.config["MAIL_SERVER"] = "mail.eg-expert.ru"
application.config["MAIL_USE_TLS"] = False
application.config["MAIL_USE_SSL"] = True
application.config["MAIL_USERNAME"] = CONFIG["MAIL_USERNAME"]
mail = Mail(application)

# Main html
@application.route("/")
def index():

    return render_template("index.html", title=title["index"])

@application.route("/services")
def services():

    return render_template("services.html", title=title["services"])

@application.route("/experts")
def experts():

    return render_template("experts.html", title=title["experts"])

@application.route("/contacts")
def contacts():

    return render_template("contacts.html", title=title["contacts"])

# Invisible html
@application.route("/email", methods=["POST", "GET"])
def email():

    name = request.form.get("name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    text = request.form.get("text")

    if request.method == "POST":
        msg = Message("Заявка на экспертизу", recipients=['v417459@yandex.ru'])
        msg_client = Message("Заявка успешно отправлена", recipients=[email])
        msg.body = (f"Имя клиента: {name}\nТелефон клиента: {phone}\nEmail заявки: {email}\nТекст заявки: {text}")
        msg_client.body = (f"Мы получили заявку на экспертизу. Свяжемся с вами в ближайшее время для уточнения информации по экспертизе")
        mail.send(msg)
        mail.send(msg_client)

    return redirect ("/")


if __name__ == "__main__":
    application.run(debug=True)