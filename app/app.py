from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)

@app.route("/")
def dashboard():

    stats = database.dashboard_stats()

    servers = database.get_servers()

    return render_template(

        "dashboard.html",

        stats=stats,

        servers=servers[:5]

    )

@app.route("/inventory")
def inventory():

    servers = database.get_servers()

    return render_template(

        "inventory.html",

        servers=servers

    )

@app.route("/add", methods=["GET","POST"])

def add_server():

    if request.method=="POST":

        server = {

            "server_name": request.form["server_name"],
            "server_role": request.form["server_role"],
            "environment": request.form["environment"],
            "operating_system": request.form["operating_system"],
            "ip_address": request.form["ip_address"],
            "owner": request.form["owner"],
            "status": request.form["status"]

        }

        database.add_server(server)

        return redirect(url_for("inventory"))

    return render_template("add_server.html")

@app.route("/delete/<int:id>")

def delete(id):

    database.delete_server(id)

    return redirect(url_for("inventory"))

if __name__=="__main__":

    app.run(

        host="0.0.0.0",
        port=5000,
        debug=True

    )