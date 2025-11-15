from flask import Flask , render_template , request , session
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/aboutus")
def aboutus():
    return render_template("about.html")


@app.route("/admin" )
def admin():
    return render_template("admin.html")

@app.route("/contactus")
def contactus():
    return render_template("contactus.html")

@app.route("/admindashbord", methods=["post"])
def admindashbord():
    u = request.form["txtusername"]
    p = request.form["txtpassword"]
    if (u == "admin" and p == "anshul"):
        session["name"]="ram"
        return render_template("admin_dashbord.html")
    else:
        msg = "invalid username and password."
        return render_template("admin.html", message=msg)


@app.route("/addemp")
def addemp():
    return render_template("addemp.html")

@app.route("/searchemp")
def searchemp():
    return render_template("searchemp.html")





# yhan humne data base ka connection kra hai
from flask_mysqldb import MySQL
app.secret_key="anshu@123"
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]="anshu@123"
app.config["MYSQL_DB"]="erpsystem"

con= MySQL(app)

#yhan humne add employye page se submit kra data or registration succusfully ka mtlb data date base mai add ho gya
@app.route("/regsuccess" , methods=["post"])
def save():
    n = request.form["txtname"]
    i = request.form["txtemail"]
    m = request.form["txtmobile"]
    d = request.form["txtdesignation"]
    s = request.form["txtsalary"]

    cur = con.connection.cursor() #database connection
    cur.execute("INSERT INTO employee (name, email, mobile, designation, salary) VALUES (%s, %s, %s, %s, %s)",
                (n, i, m, d, s)) # insert data in database
    con.connection.commit()# data confirmation and save in database
    cur.close() # to close the connection of database

    return render_template("admin_reg_suc.html")

# yhan humne jo data abhi addemp page mai likhr kr database mai show kra tha usko database se showdata page mai show kr rhe hai
@app.route("/showdata")
def showdata():
    cur = con.connection.cursor()
    cur.execute("SELECT * FROM employee")
    emplist = cur.fetchall()
    cur.close()

    return render_template("showemployee.html" , recordlist=emplist)


# yhan hum view button pe click krke kisi bhi empoyee ka specific data dhek rhe hai
@app.route("/profile")
def profile():
    id = request.args.get("Id")
    cur = con.connection.cursor()  # database connection
    cur.execute( "select * from employee where id =" +id)  # insert data in database
    emplist = cur.fetchall()
    return render_template("adminprofile.html" , recordlist=emplist)

@app.route("/adminempupdate" , methods=["post"])
def adminempupdate():

    n = request.form["txtname"]
    i = request.form["txtemail"]
    m = request.form["txtmobile"]
    d = request.form["txtdesignation"]
    s = request.form["txtsalary"]
    empid = request.form["txtId"]

    cur = con.connection.cursor()  # database connection
    cur.execute( "update employee set name= %s , email=%s , mobile=%s , designation=%s , salary=%s where id=%s",(n,i,m,d,s,empid))

              # insert data in database
    con.connection.commit()  # data confirmation and save in database
    cur.close()  # to close the connection of database
    return render_template("adminempupdate.html")


#  for delete data from database
@app.route("/admin_emp_delete")
def admin_emp_delete():
    i = request.args.get("id")  # use form for POST data
    cur = con.connection.cursor()  # database connection
    cur.execute(" delete from employee where id=%s", (i,))
    con.connection.commit()  # data confirmation and save in database
    cur.close()  # to close the connection of database

    return render_template("admin_emp_delete_success.html")


@app.route("/admin_emp_searchprocess", methods=["POST"])
def admin_emp_searchprocess():
    n = request.form["txtname"]
    print(n)
    cur = con.connection.cursor()
    q = "SELECT * FROM employee WHERE name LIKE %s"
    cur.execute(q, (n + "%",))
    emplist = cur.fetchall()
    cur.close()
    return render_template("admin_emp_searchresult.html", recordlist=emplist)

@app.route("/logout")
def logout():
    session ["name"]=None
    return render_template("admin.html")













app.run( debug = True)