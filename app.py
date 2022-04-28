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



# All exprertises pages

@application.route("/services/cabling")
def cabling():
    return render_template("/services/cabling.html", expertise_name=expertise_name["cabling"], title=title["cabling"], description=description["cabling"])

@application.route("/services/inst_couplings")
def inst_couplings():
    return render_template("/services/inst_couplings.html", expertise_name=expertise_name["inst_couplings"], title=title["inst_couplings"], description=description["inst_couplings"])

@application.route("/services/inst_cablestruct")
def inst_cablestruct():
    return render_template("/services/inst_cablestruct.html", expertise_name=expertise_name["inst_cablestruct"], title=title["inst_cablestruct"], description=description["inst_cablestruct"])

@application.route("/services/lighting")
def lighting():
    return render_template("/services/lighting.html", expertise_name=expertise_name["lighting"], title=title["lighting"], description=description["lighting"])

@application.route("/services/inst_switchgears")
def inst_switchgears():
    return render_template("/services/inst_switchgears.html", expertise_name=expertise_name["inst_switchgears"], title=title["inst_switchgears"], description=description["inst_switchgears"])

@application.route("/services/inst_ground_loop")
def inst_ground_loop():
    return render_template("/services/inst_ground_loop.html", expertise_name=expertise_name["inst_ground_loop"], title=title["inst_ground_loop"], description=description["inst_ground_loop"])

@application.route("/services/react_compensation")
def react_compensation():
    return render_template("/services/react_compensation.html", expertise_name=expertise_name["react_compensation"], title=title["react_compensation"], description=description["react_compensation"])

@application.route("/services/smooth_start")
def smooth_start():
    return render_template("/services/smooth_start.html", expertise_name=expertise_name["smooth_start"], title=title["smooth_start"], description=description["smooth_start"])

@application.route("/services/electric_motor")
def electric_motor():
    return render_template("/services/electric_motor.html", expertise_name=expertise_name["electric_motor"], title=title["electric_motor"], description=description["electric_motor"])

@application.route("/services/generator")
def generator():
    return render_template("/services/generator.html", expertise_name=expertise_name["generator"], title=title["generator"], description=description["generator"])

@application.route("/services/system_generator")
def system_generator():
    return render_template("/services/system_generator.html", expertise_name=expertise_name["system_generator"], title=title["system_generator"], description=description["system_generator"])

@application.route("/services/conductor")
def conductor():
    return render_template("/services/conductor.html", expertise_name=expertise_name["conductor"], title=title["conductor"], description=description["conductor"])

@application.route("/services/power_trans")
def power_trans():
    return render_template("/services/power_trans.html", expertise_name=expertise_name["power_trans"], title=title["power_trans"], description=description["power_trans"])

@application.route("/services/reactor")
def reactor():
    return render_template("/services/reactor.html", expertise_name=expertise_name["reactor"], title=title["reactor"], description=description["reactor"])

@application.route("/services/construction_switch")
def construction_switch():
    return render_template("/services/construction_switch.html", expertise_name=expertise_name["construction_switch"], title=title["construction_switch"], description=description["construction_switch"])

@application.route("/services/disconnector")
def disconnector():
    return render_template("/services/disconnector.html", expertise_name=expertise_name["disconnector"], title=title["disconnector"], description=description["disconnector"])

@application.route("/services/isolator")
def isolator():
    return render_template("/services/isolator.html", expertise_name=expertise_name["isolator"], title=title["isolator"], description=description["isolator"])

@application.route("/services/busbar_support")
def busbar_support():
    return render_template("/services/busbar_support.html", expertise_name=expertise_name["busbar_support"], title=title["busbar_support"], description=description["busbar_support"])

@application.route("/services/busbar_flex")
def busbar_flex():
    return render_template("/services/busbar_flex.html", expertise_name=expertise_name["busbar_flex"], title=title["busbar_flex"], description=description["busbar_flex"])

@application.route("/services/switchgears")
def switchgears():
    return render_template("/services/switchgears.html", expertise_name=expertise_name["switchgears"], title=title["switchgears"], description=description["switchgears"])

@application.route("/services/cable")
def cable():
    return render_template("/services/cable.html", expertise_name=expertise_name["cable"], title=title["cable"], description=description["cable"])

@application.route("/services/cell_protection")
def cell_protection():
    return render_template("/services/cell_protection.html", expertise_name=expertise_name["cell_protection"], title=title["cell_protection"], description=description["cell_protection"])

@application.route("/services/transfer_devices")
def transfer_devices():
    return render_template("/services/transfer_devices.html", expertise_name=expertise_name["transfer_devices"], title=title["transfer_devices"], description=description["transfer_devices"])

@application.route("/services/transfer_panel")
def transfer_panel():
    return render_template("/services/transfer_panel.html", expertise_name=expertise_name["transfer_panel"], title=title["transfer_panel"], description=description["transfer_panel"])

@application.route("/services/protection_panel")
def protection_panel():
    return render_template("/services/protection_panel.html", expertise_name=expertise_name["protection_panel"], title=title["protection_panel"], description=description["protection_panel"])

@application.route("/services/emergency_panel")
def emergency_panel():
    return render_template("/services/emergency_panel.html", expertise_name=expertise_name["emergency_panel"], title=title["emergency_panel"], description=description["emergency_panel"])

@application.route("/services/automation_panel")
def automation_panel():
    return render_template("/services/automation_panel.html", expertise_name=expertise_name["automation_panel"], title=title["automation_panel"], description=description["automation_panel"])


if __name__ == "__main__":
    application.run(debug=True)


