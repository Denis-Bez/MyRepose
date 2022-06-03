import re

from text_library import title, expertise_name, description, spam_filter, pages, background

from config import CONFIG
from flask import Flask, render_template, redirect, flash, request, url_for
from flask_mail import Mail, Message

application = Flask (__name__)

application.config["SECRET_KEY"] = CONFIG["SECRET_KEY"]
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

@application.route("/privacy")
def privacy():
    return render_template("privacy.html", title=title["privacy"])

# Invisible html
@application.route("/email", methods=["POST", "GET"])
def email():

    if request.method == "POST":
        name = request.form.get("name")
        phone = request.form.get("phone")
        email = request.form.get("email")
        text = request.form.get("text")

        msg = Message("Заявка на экспертизу", recipients=["v417459@yandex.ru", "expert@eg59.ru"])
        msg_client = Message("Заявка успешно отправлена", recipients=[email])
        msg_client.body = (f"Мы получили заявку на экспертизу. Свяжемся с вами в ближайшее время для уточнения информации")

        # Spam filter
        try:
            for spam_name in spam_filter["name"]:
                if re.search(spam_name, name):
                    flash("Заявка распознана системой как спам! Попробуйте написать нам на почту expert@eg59.ru или позвонить по телефону +7 963 882 0233", category="danger")
                    return redirect ("/")
        except:
            print("name: 'None'")

        try:
            for spam_text in spam_filter["text"]:
                if re.search(spam_text, text):
                    flash("Заявка распознана системой как спам! Попробуйте написать нам на почту expert@eg59.ru или позвонить по телефону +7 963 882 0233", category="danger")
                    return redirect ("/")
        except:
            print("text: 'None'")

        # Sending mail
        try:
            mail.send(msg_client)
            status = "Подтверждение на почту отправлено"
        except:
            status = "Подтверждение на почту не отправлено"

        msg.body = (f"Имя клиента: {name}\nТелефон клиента: {phone}\nEmail заявки: {email}\nТекст заявки: {text}\nСтатус отправки письма клиенту: {status}")
        
        try:
            mail.send(msg)
            flash("Заявка успешно отправлена! Мы свяжемся с Вами в ближайшее время", category="success")
        except:
            flash("Произошла ошибка при отправке заявки. Попробуйте написать нам на почту expert@eg59.ru или позвонить по телефону +7 963 882 0233", category="danger")
        
    return redirect ("/")

# Sitemap route
@application.route("/sitemap.xml")
def sitemap():
    return render_template("sitemap.xml")


# Verification Yandex
@application.route("/yandex_dafd13b4bd118941.html")
def yandex_verification():
    return render_template("yandex_dafd13b4bd118941.html")


# Test Rout
#@application.route("/services_new")
#def test_function():
#    return render_template("services_new.html")


# All exprertises pages. Нужна ли защита от атаки 'внедрения'. М.б. попробовать самому взломать 

@application.route('/services/<name>')
def many_pages(name):
    try:
        page = pages[name]
        return render_template('/services/' + page + '.html', 
            expertise_name=expertise_name[page], title=title[page], description=description[page], 
            background=background[page])
    except:
        return render_template('services.html')


if __name__ == "__main__":
    application.run(debug=True)


