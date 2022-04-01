from config import CONFIG

from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message

app = Flask (__name__)

title = {
    "index": "ЭНЕРГО group Экспертиза - Энергия в руках профессионалов",
    "services": "Заказать экспертизу электротехнических работ и оборудования" 
}

app.config["MAIL_DEFAULT_SENDER"] = CONFIG["MAIL_DEFAULT_SENDER"]
app.config["MAIL_PASSWORD"] = CONFIG["MAIL_PASSWORD"]
app.config["MAIL_PORT"] = 465
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = CONFIG["MAIL_USERNAME"]
mail = Mail(app)

# Main html
@app.route("/")
def index():

    return render_template("index.html", title=title["index"])

@app.route("/services")
def services():

    return render_template("services.html")

@app.route("/experts")
def experts():

    return render_template("experts.html")

@app.route("/contacts")
def contacts():

    return render_template("contacts.html")

# Invisible html
@app.route("/email", methods=["POST", "GET"])
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

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)