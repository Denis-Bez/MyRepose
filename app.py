from config import CONFIG
from text_library import title, expertise_name, description

from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message

application = Flask (__name__)


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
        
        try:
            mail.send(msg_client)
            status = "Подтверждение на почту отправлено"
        except:
            status = "Подтверждение на почту не отправлено"

        msg.body = (f"Имя клиента: {name}\nТелефон клиента: {phone}\nEmail заявки: {email}\nТекст заявки: {text}\nСтатус отправки письма клиенту: {status}")
        mail.send(msg)
        

    return redirect ("/")


# Verification Yandex
@application.route("/yandex_dafd13b4bd118941.html")
def yandex_verification():

    return render_template("yandex_dafd13b4bd118941.html")

# Test Rout
#@application.route("/services_new")
#def test_function():
#    return render_template("services_new.html")



# All exprertises pages

@application.route("/expertise_cabling")
def expertise_cabling():
    return render_template("expertise_cabling.html", expertise_name=expertise_name["expertise_cabling"], title=title["expertise_cabling"], description=description["expertise_cabling"])

@application.route("/expertise_inst_couplings")
def expertise_inst_couplings():
    return render_template("expertise_inst_couplings.html", expertise_name=expertise_name["expertise_inst_couplings"], title=title["expertise_inst_couplings"], description=description["expertise_inst_couplings"])

@application.route("/expertise_inst_cablestruct")
def expertise_inst_cablestruct():
    return render_template("expertise_inst_cablestruct.html", expertise_name=expertise_name["expertise_inst_cablestruct"], title=title["expertise_inst_cablestruct"], description=description["expertise_inst_cablestruct"])

@application.route("/expertise_lighting")
def expertise_lighting():
    return render_template("expertise_lighting.html", expertise_name=expertise_name["expertise_lighting"], title=title["expertise_lighting"], description=description["expertise_lighting"])

@application.route("/expertise_InstSwitchgears")
def expertise_InstSwitchgears():
    return render_template("expertise_InstSwitchgears.html", expertise_name=expertise_name["expertise_InstSwitchgears"], title=title["expertise_InstSwitchgears"], description=description["expertise_InstSwitchgears"])

@application.route("/expertise_InstGroundLoop")
def expertise_InstGroundLoop():
    return render_template("expertise_InstGroundLoop.html", expertise_name=expertise_name["expertise_InstGroundLoop"], title=title["expertise_InstGroundLoop"], description=description["expertise_InstGroundLoop"])

@application.route("/expertise_ReactCompensation")
def expertise_ReactCompensation():
    return render_template("expertise_ReactCompensation.html", expertise_name=expertise_name["expertise_ReactCompensation"], title=title["expertise_ReactCompensation"], description=description["expertise_ReactCompensation"])

@application.route("/expertise_SmoothStart")
def expertise_SmoothStart():
    return render_template("expertise_SmoothStart.html", expertise_name=expertise_name["expertise_SmoothStart"], title=title["expertise_SmoothStart"], description=description["expertise_SmoothStart"])

@application.route("/expertise_ElectricMotor")
def expertise_ElectricMotor():
    return render_template("expertise_ElectricMotor.html", expertise_name=expertise_name["expertise_ElectricMotor"], title=title["expertise_ElectricMotor"], description=description["expertise_ElectricMotor"])

@application.route("/expertise_Generator")
def expertise_Generator():
    return render_template("expertise_Generator.html", expertise_name=expertise_name["expertise_Generator"], title=title["expertise_Generator"], description=description["expertise_Generator"])

@application.route("/expertise_SystemGenerator")
def expertise_SystemGenerator():
    return render_template("expertise_SystemGenerator.html", expertise_name=expertise_name["expertise_SystemGenerator"], title=title["expertise_SystemGenerator"], description=description["expertise_SystemGenerator"])

@application.route("/expertise_Conductor")
def expertise_Conductor():
    return render_template("expertise_Conductor.html", expertise_name=expertise_name["expertise_Conductor"], title=title["expertise_Conductor"], description=description["expertise_Conductor"])

@application.route("/expertise_PowerTrans")
def expertise_PowerTrans():
    return render_template("expertise_PowerTrans.html", expertise_name=expertise_name["expertise_PowerTrans"], title=title["expertise_PowerTrans"], description=description["expertise_PowerTrans"])

@application.route("/expertise_Reactor")
def expertise_Reactor():
    return render_template("expertise_Reactor.html", expertise_name=expertise_name["expertise_Reactor"], title=title["expertise_Reactor"], description=description["expertise_Reactor"])

@application.route("/expertise_ConstructionSwitch")
def expertise_ConstructionSwitch():
    return render_template("expertise_ConstructionSwitch.html", expertise_name=expertise_name["expertise_ConstructionSwitch"], title=title["expertise_ConstructionSwitch"], description=description["expertise_ConstructionSwitch"])

@application.route("/expertise_Disconnector")
def expertise_Disconnector():
    return render_template("expertise_Disconnector.html", expertise_name=expertise_name["expertise_Disconnector"], title=title["expertise_Disconnector"], description=description["expertise_Disconnector"])


if __name__ == "__main__":
    application.run(debug=True)


