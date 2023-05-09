#import os
#import random
#import string
from flask import Flask,render_template, flash,redirect,request
#(
  
   # url_for,
   # ,
   # ,
   # ,
   # session,
   # send_from_directory,
#)
from forms import (
    RegisterForm,
    LoginForm)
   # ProjectForm,
    #WorkForm,
    #EduForm,
    #SkilsForm,
    #HobForm,
    #SocialForm,
    #RefForm,
    #GolsForm,
    #ProfileForm,
    #TokForm,
    #CssForm,
    #LangForm,
    #SocForm,
    #PasForm
#)
#from cs50 import SQL
#from flask_session import Session
#from werkzeug.security import check_password_hash, generate_password_hash
#from werkzeug.utils import secure_filename
#from functools import wraps
from threading import Timer
from datetime import datetime, timedelta
#import uuid

app = Flask(__name__)
#app.config["SECRET_KEY"] = "9e5734eb4a542802b7c24415"
#app.config["UPLOAD_FOLDER"] = "/workspaces/104098487/project/uploads"
#app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024
#app.config["UPLOAD_EXTENSIONS"] = [".jpg", ".png", ".gif"]
#app.secret_key = '9e5734eb4a542802b7c24415as'

# Configure session to use filesystem (instead of signed cookies)
#app.config["SESSION_PERMANENT"] = False
#app.config["SESSION_TYPE"] = "filesystem"
#Session(app)

# Configure CS50 Library to use SQLite database
#db = SQL("sqlite:///users.db")
count = 1
"""
@app.after_request
def after_request(response):
    #Ensure responses aren't cached
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


def login_required(f):
   
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


"""
@app.route("/coderr")
def code_error():

    # create a thread timer object
    timer = Timer(120, task)
    # start the timer object
    timer.start()
    # wait for the timer to finish

    if count !=1:
        return render_template("code.html")
    else:
        return redirect(url_for("home_page"))
      
def get_read_only_info(code):

    #user_id = db.execute("SELECT user_id FROM token_add WHERE token_id = ?", code)
    #if user_id:
        #time = db.execute("SELECT exp_date FROM token_add WHERE token_id = ?", code)
  current_date = datetime.now().date()
#target_date = datetime.strptime(time[0]["exp_date"], "%Y-%m-%d").date()
        #if current_date > target_date:
          #  db.execute("DELETE FROM token_add WHERE token_id= ? ",code)
          # return False
        #else:
            #reuse= db.execute("SELECT reuse_count FROM token_add WHERE token_id = ?", code)
           # if reuse[0]["reuse_count"] >0:
           #     reuse=reuse[0]["reuse_count"]
            #    reuse = reuse -1
             #   db.execute(" UPDATE token_add SET reuse_count=? WHERE token_id = ? ",reuse,code)
             #   user_id = db.execute("SELECT user_id FROM token_add WHERE token_id = ?", code)
             #   session["user_id"]=user_id[0]["user_id"]
             #   session["token"]= code
  return True
            #else:
              #  db.execute("DELETE FROM token_add WHERE token_id= ? ",code)
               # return False
   # else:
       # return False

@app.route("/", methods=["GET", "POST"])

def home_page():
    global count
    if request.method == "POST":
        # Check if code is valid and retrieve information in read-only mode
        if get_read_only_info(request.form.get("code")):
            count=1
            return redirect(url_for("cv_page"))
        else:
            category = "danger"
            flash([f"Incorrect code please try again {count} !"], category)
            count = count+1
            if count > 3 :

                return redirect(url_for("code_error"))
            else:
                return render_template("index.html")
    else:
        if count > 3 :
            return redirect(url_for("code_error"))
        else:
            return render_template("index.html")
          
if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)
"""
@app.route("/cv", methods=["GET"])
@login_required
def cv_page():
    user_id = session["user_id"]
    data = db.execute("SELECT * FROM  users WHERE users.id= ?",user_id)
    data1 = db.execute("SELECT * FROM  work_exp WHERE user_id= ?",user_id)
    data2 = db.execute("SELECT * FROM  project WHERE user_id= ?",user_id)
    data3 = db.execute("SELECT * FROM  gols WHERE user_id= ?",user_id)
    data4 = db.execute("SELECT * FROM  skils WHERE user_id= ?",user_id)
    data5 = db.execute("SELECT * FROM  education WHERE user_id= ?",user_id)
    data6 = db.execute("SELECT * FROM  hobby WHERE user_id= ?",user_id)
    data7 = db.execute("SELECT * FROM  referances WHERE user_id= ?",user_id)
    data8 = db.execute("SELECT * FROM  social WHERE user_id= ?",user_id)
    data9 = db.execute("SELECT * FROM  hobby WHERE user_id= ?",user_id)
    data10 = db.execute("SELECT * FROM  lang WHERE user_id= ?",user_id)
    data11 = db.execute("SELECT * FROM  soc WHERE user_id= ?",user_id)

    return render_template("cv.html",data=data,data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,data6=data6,data7=data7,data8=data8,data9=data9,data10=data10,data11=data11)
"""
@app.route("/register", methods=["GET", "POST"])
def register_page():
    form = RegisterForm()
    if request.method == "POST":
        if form.validate_on_submit():
            user_to_check = db.execute(
                "SELECT * FROM users WHERE username = ?", form.username.data
            )
            if len(user_to_check) == 1:
                category = "danger"
                flash(["Please use different username !"], category)
                return render_template("register.html", form=form)
            else:
                # INSERT the new user into users, storing a hash of the user’s password, not the password itself.
                hash = generate_password_hash(
                    form.password.data, method="pbkdf2:sha256", salt_length=8
                )
                db.execute(
                    "INSERT INTO users (username,hash,email) VALUES (?,?,?)",
                    form.username.data,
                    hash,
                    form.email.data,
                )

                # Query database for id
                rows = db.execute(
                    "SELECT * FROM users WHERE username = ?", form.username.data
                )
                # Remember which user has logged in
                session["user_id"] = rows[0]["id"]
                # Redirect user to home page
                return redirect(url_for("home_page"))
        if form.errors != {}:
            for error_msg in form.errors.values():
                category = "danger"
                flash(error_msg, category)
            return render_template("register.html", form=form)
    else:
        return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if request.method == "POST":
        if form.validate_on_submit():
            # Query database for id
            rows = db.execute(
                "SELECT * FROM users WHERE username = ?", form.username.data
            )
            # Ensure username exists and password is correct
            if len(rows) != 1 or not check_password_hash(
                rows[0]["hash"], form.password.data
            ):
                category = "danger"
                flash(["Incorrect password or username please try again !"], category)
                return render_template("login.html", form=form)
            else:
                # Remember which user has logged in
                session["user_id"] = rows[0]["id"]
                # Redirect user to home page

                return redirect(url_for("cv_page"))
    else:
        return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    #Log user out

    # Forget any user_id
    session.clear()

    # Redirect user to home page
    return redirect("/")
"""

@app.route("/project", methods=["GET", "POST"])
@login_required

def project_page():
    form = ProjectForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            uploaded_file = form.image.data
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    category = "danger"
                    flash(["Please use '.jpg', '.png', '.gif' file !"], category)
                    return render_template("project.html", form=form)
                file_name = os.path.splitext(filename)[0]
                file_name = get_random_string(16)
                uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))

            db.execute(
                "INSERT INTO project VALUES (?,?,?,?,?,?,?,?,?,?)",
                user_id,
                form.project.data,
                form.project_loc.data,
                form.type.data,
                form.gool.data,
                file_name,
                form.about_project.data,
                form.start_date.data,
                form.end_date.data,
                form.link_project.data,
            )
            return redirect(url_for("project_page"))
        else:
            return render_template("project.html")
    else:
        # alow akses to data without login get user id bay pasword ?

        projects = db.execute("SELECT * FROM project WHERE user_id= ? ", user_id)

        return render_template("project.html",projects=projects)


def get_random_string(length):
    # With combination of lower and upper case
    result_str = "".join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        return None
    return "." + (format if format != "jpeg" else "jpg")

@app.route("/uploads/<filename>")
def upload(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route("/work", methods=["GET", "POST"])
@login_required

def work_page():
    form = WorkForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            uploaded_file = form.image.data
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    category = "danger"
                    flash(["Please use '.jpg', '.png', '.gif' file !"], category)
                    return render_template("work.html", form=form)
                file_name = os.path.splitext(filename)[0]
                file_name = get_random_string(14)
                uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))

            db.execute(
                "INSERT INTO work_exp  VALUES (?,?,?,?,?,?,?,?,?)",
                user_id,
                form.company.data,
                form.comp_loc.data,
                form.position.data,
                form.about_work.data,
                file_name,
                form.start_date.data,
                form.end_date.data,
                form.link_comp.data,
            )
            return redirect(url_for("work_page"))
        else:
            return render_template("work.html")
    else:
        # alow akses to data without login get user id bay pasword ?
        # render data from db

        work_exp = db.execute("SELECT * FROM work_exp WHERE user_id= ? ", user_id)
        return render_template("work.html", work_exp=work_exp)


@app.route("/edu", methods=["GET", "POST"])
@login_required

def edu_page():
    form = EduForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            uploaded_file = form.image.data
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    category = "danger"
                    flash(["Please use '.jpg', '.png', '.gif' file !"], category)
                    return render_template("education.html", form=form)
                file_name = os.path.splitext(filename)[0]
                file_name = get_random_string(14)
                uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))

            db.execute(
                "INSERT INTO education  VALUES (?,?,?,?,?,?,?,?,?,?)",
                user_id,
                form.school.data,
                form.school_loc.data,
                form.type.data,
                form.grade.data,
                file_name,
                form.about_edu.data,
                form.start_date.data,
                form.end_date.data,
                form.link_edu.data,
            )
            return redirect(url_for("edu_page"))
        else:
            return render_template("education.html")
    else:
        # alow akses to data without login get user id bay pasword ?
        # render data from db
        education = db.execute("SELECT * FROM education WHERE user_id= ? ", user_id)
        return render_template("education.html", education=education)


@app.route("/skils", methods=["GET", "POST"])
@login_required

def skils_page():
    form = SkilsForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            uploaded_file = form.image.data
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    category = "danger"
                    flash(["Please use '.jpg', '.png', '.gif' file !"], category)
                    return render_template("skils.html", form=form)
                file_name = os.path.splitext(filename)[0]
                file_name = get_random_string(14)
                uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))

            db.execute(
                "INSERT INTO skils  VALUES (?,?,?,?,?)",
                user_id,
                form.skill.data,
                form.level.data,
                file_name,
                form.about_skill.data,
            )
            return redirect(url_for("skils_page"))
        else:
            return render_template("skils.html")
    else:
        # alow akses to data without login get user id bay pasword ?
        # render data from db
        skils = db.execute("SELECT * FROM skils WHERE user_id= ? ", user_id)
        return render_template("skils.html", skils=skils)


@app.route("/gols", methods=["GET", "POST"])
def gols_page():
    form = GolsForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            uploaded_file = form.image.data
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    category = "danger"
                    flash(["Please use '.jpg', '.png', '.gif' file !"], category)
                    return render_template("gols.html", form=form)
                file_name = os.path.splitext(filename)[0]
                file_name = get_random_string(14)
                uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))

            db.execute(
                "INSERT INTO gols  VALUES (?,?,?,?,?)",
                user_id,
                form.gol_pos.data,
                file_name,
                form.about_gol.data,
                form.link.data,
            )
            return redirect(url_for("gols_page"))
        else:
            return render_template("gols.html")
    else:
        # alow akses to data without login get user id bay pasword ?
        # render data from db
        gols = db.execute("SELECT * FROM gols WHERE user_id= ? ", user_id)
        return render_template("gols.html",  gols=gols)


@app.route("/hob", methods=["GET", "POST"])
@login_required

def hob_page():
    form = HobForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            uploaded_file = form.image.data
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    category = "danger"
                    flash(["Please use '.jpg', '.png', '.gif' file !"], category)
                    return render_template("hobij.html")
                file_name = os.path.splitext(filename)[0]
                file_name = get_random_string(14)
                uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))

            db.execute(
                "INSERT INTO hobby  VALUES (?,?,?,?,?)",
                user_id,
                form.hobby.data,
                file_name,
                form.about_hobby.data,
                form.duration.data,
            )
            return redirect(url_for("hob_page"))
        else:
            return render_template("hobij.html")
    else:
        # alow akses to data without login get user id bay pasword ?
        # render data from db
        hobby = db.execute("SELECT * FROM hobby WHERE user_id= ? ", user_id)
        return render_template("hobij.html", hobby=hobby)


@app.route("/ref", methods=["GET", "POST"])
@login_required

def ref_page():
    form = RefForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            uploaded_file = form.image.data
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    category = "danger"
                    flash(["Please use '.jpg', '.png', '.gif' file !"], category)
                    return render_template("refernces.html", form=form)
                file_name = os.path.splitext(filename)[0]
                file_name = get_random_string(14)
                uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))

            db.execute(
                "INSERT INTO referances  VALUES (?,?,?,?,?,?,?,?,?,?)",
                user_id,
                form.ref_name.data,
                form.company.data,
                file_name,
                form.referance.data,
                form.mob.data,
                form.email.data,
                form.link.data,
                0,
                0,
            )
            return redirect(url_for("ref_page"))
        else:
            return render_template("refernces.html")
    else:
        # alow akses to data without login get user id bay pasword ?
        # render data from db
        referances = db.execute("SELECT * FROM referances WHERE user_id= ? ", user_id)
        return render_template("refernces.html", referances=referances)


@app.route("/social", methods=["GET", "POST"])
@login_required

def social_page():
    form = SocialForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            uploaded_file = form.image.data
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    category = "danger"
                    flash(["Please use '.jpg', '.png', '.gif' file !"], category)
                    return render_template("social.html", form=form)
                file_name = os.path.splitext(filename)[0]
                file_name = get_random_string(14)
                uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))

            db.execute(
                "INSERT INTO social  VALUES (?,?,?,?,?)",
                user_id,
                form.social.data,
                file_name,
                form.activity.data,
                form.link.data,
            )
            return redirect(url_for("social_page"))
        else:
            return render_template("social.html")
    else:
        # alow akses to data without login get user id bay pasword ?
        # render data from db
        social = db.execute("SELECT * FROM social WHERE user_id= ? ", user_id)
        return render_template("social.html", social=social)


@app.route("/profile", methods=["GET", "POST"])
@login_required

def profile_page():
    form = ProfileForm()
    form1 = ProjectForm()
    form2 = WorkForm()
    form3 = EduForm()
    form4 = SkilsForm()
    form5 = GolsForm()
    form6 = HobForm()
    form7 = RefForm()
    form8 = SocialForm()
    form9 = LangForm()
    form10= SocForm()
    form11= PasForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            uploaded_file = form.image.data
            filename = secure_filename(uploaded_file.filename)
            if filename != "":
                file_ext = os.path.splitext(filename)[1]
                if file_ext not in app.config["UPLOAD_EXTENSIONS"]:
                    category = "danger"
                    flash(["Please use '.jpg', '.png', '.gif' file !"], category)
                    return render_template("hobij.html", form=form)
                file_name = os.path.splitext(filename)[0]
                file_name = get_random_string(14)
                file = db.execute("SELECT img FROM users WHERE id= ? ", user_id)
                path = os.path.join(app.config["UPLOAD_FOLDER"], file[0]["img"])
                os.remove(path)
                uploaded_file.save(os.path.join(app.config["UPLOAD_FOLDER"], file_name))
            rows = db.execute("SELECT * FROM users WHERE id = ?", user_id)
            # Ensure username exists and password is correct
            if check_password_hash(rows[0]["hash"], form.password.data):
                db.execute(" UPDATE users SET username=?, first_name=?, last_name=?,birthday=?,gol_cv=?, family_status=?,nation=?,img=?,about_me=?,adress=?,email=?,full_mob=? WHERE id = ? ",form.username.data,form.first_name.data,form.last_name.data,form.birthday.data,form.gol_cv.data,form.family_status.data,form.nation.data,file_name,form.about_me.data,form.adress.data,form.email.data,form.full_mob.data,user_id)
                return redirect(url_for("cv_page"))
            else:
                category = "danger"
                flash(["Incorrect password"], category)
                return redirect(url_for("profile_page"))

    else:
        # alow akses to data without login get user id bay pasword ?
        # render data from db
        lang = db.execute("SELECT * FROM lang WHERE user_id= ? ", user_id)
        soc = db.execute("SELECT * FROM soc WHERE user_id= ? ", user_id)
        return render_template(
            "profile.html",lang=lang,soc=soc,
            form=form,
            form1=form1,
            form2=form2,
            form3=form3,
            form4=form4,
            form5=form5,
            form6=form6,
            form7=form7,
            form8=form8,
            form9=form9,
            form10=form10,
            form11=form11,
        )


@app.route("/token", methods=["GET", "POST"])

def tok_page():
    form = TokForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            tokengen = os.urandom(8).hex()
            db.execute(
                "INSERT INTO token_add VALUES (?,?,?,?)",
                user_id,
                tokengen,
                form.exp_date.data,
                form.reuse_count.data,
            )
            return redirect(url_for("tok_page"))
        else:
            return render_template("token.html",form=form)
    else:
        # alow akses to data without login get user id bay pasword ?
        # render data from db

        tokens = db.execute("SELECT * FROM token_add WHERE user_id= ? ", user_id)
        return render_template("token.html",form=form, tokens=tokens)

@app.route("/lang", methods=["GET", "POST"])
@login_required

def lang_page():
    form = LangForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            db.execute(
                "INSERT INTO lang VALUES (?,?,?,?)",
                user_id,
                form.lang.data,
                form.level.data,
                form.level_by.data,
            )
            return redirect(url_for("home_page"))
        else:
            return render_template("profile.html",form=form)
    else:
        return redirect(url_for("home_page"))

@app.route("/soc", methods=["GET", "POST"])
@login_required

def soc_page():
    form = SocForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():

            db.execute(
                "INSERT INTO soc VALUES (?,?,?,?,?,?)",
                user_id,
                form.web.data,
                form.f_book.data,
                form.twiter.data,
                form.instag.data,
                form.add_info.data
            )
            return redirect(url_for("home_page"))
        else:
            return render_template("profile.html",form=form)
    else:
        return redirect(url_for("home_page"))

@app.route("/del",methods=["POST"])
@login_required

def delete():
    user_id = session["user_id"]
    request.form.get("code")
    if request.method == "POST":
        item = request.form.get("item")
        if item:
            file = db.execute("SELECT img FROM project WHERE user_id= ? ", user_id)
            path = os.path.join(app.config["UPLOAD_FOLDER"], file[0]["img"])
            os.remove(path)
            db.execute("DELETE FROM project WHERE user_id= ? AND project= ? ",user_id,item)
            return redirect(url_for("project_page"))
        item1 = request.form.get("item1")
        if item1:
            file = db.execute("SELECT img FROM work_exp WHERE user_id= ? ", user_id)
            path = os.path.join(app.config["UPLOAD_FOLDER"], file[0]["img"])
            os.remove(path)
            db.execute("DELETE FROM work_exp WHERE user_id= ? AND company= ? ",user_id,item1)
            return redirect(url_for("work_page"))
        item2 = request.form.get("item2")
        if item2:
            file = db.execute("SELECT img FROM education WHERE user_id= ? ", user_id)
            path = os.path.join(app.config["UPLOAD_FOLDER"], file[0]["img"])
            os.remove(path)
            db.execute("DELETE FROM education WHERE user_id= ? AND school= ? ",user_id,item2)
            return redirect(url_for("edu_page"))
        item3 = request.form.get("item3")
        if item3:
            file = db.execute("SELECT img FROM skils WHERE user_id= ? ", user_id)
            path = os.path.join(app.config["UPLOAD_FOLDER"], file[0]["img"])
            os.remove(path)
            db.execute("DELETE FROM skils WHERE user_id= ? AND skill= ? ",user_id,item3)
            return redirect(url_for("skils_page"))
        item4 = request.form.get("item4")
        if item4:
            file = db.execute("SELECT img FROM gols WHERE user_id= ? ", user_id)
            path = os.path.join(app.config["UPLOAD_FOLDER"], file[0]["img"])
            os.remove(path)
            db.execute("DELETE FROM gols WHERE user_id= ? AND gol_pos= ? ",user_id,item4)
            return redirect(url_for("gols_page"))
        item5 = request.form.get("item5")
        if item5:
            file = db.execute("SELECT img FROM hobby WHERE user_id= ? ", user_id)
            path = os.path.join(app.config["UPLOAD_FOLDER"], file[0]["img"])
            os.remove(path)
            db.execute("DELETE FROM hobby WHERE user_id= ? AND hobby= ? ",user_id,item5)
            return redirect(url_for("hob_page"))
        item6 = request.form.get("item6")
        if item6:
            file = db.execute("SELECT img FROM referances WHERE user_id= ? ", user_id)
            path = os.path.join(app.config["UPLOAD_FOLDER"], file[0]["img"])
            os.remove(path)
            db.execute("DELETE FROM referances WHERE user_id= ? AND company= ? ",user_id,item6)
            return redirect(url_for("ref_page"))
        item7 = request.form.get("item7")
        if item7:
            file = db.execute("SELECT img FROM social WHERE user_id= ? ", user_id)
            path = os.path.join(app.config["UPLOAD_FOLDER"], file[0]["img"])
            os.remove(path)
            db.execute("DELETE FROM social WHERE user_id= ? AND social= ? ",user_id,item7)
            return redirect(url_for("soc_page"))
        item8 = request.form.get("item8")
        if item8:
            db.execute("DELETE FROM lang WHERE user_id= ? AND lang= ? ",user_id,item8)
            return redirect(url_for("cv_page"))
        item9 = request.form.get("item9")
        if item9:
            db.execute("DELETE FROM soc WHERE user_id= ? AND web= ? ",user_id,item9)
            return redirect(url_for("cv_page"))


        return redirect(url_for("cv_page"))

@app.route("/pas",methods=["POST"])
@login_required

def pas_page():
    form= PasForm()
    user_id = session["user_id"]
    if request.method == "POST":
        if form.validate_on_submit():
            rows = db.execute("SELECT * FROM users WHERE id = ?", user_id)
            # Ensure username exists and password is correct
            if check_password_hash(rows[0]["hash"], form.password1.data):
                hash_new=generate_password_hash(
                    form.password.data, method="pbkdf2:sha256", salt_length=8
                )
                db.execute(" UPDATE users SET hash=? WHERE id = ? ",hash_new,user_id)
                return redirect(url_for("logout"))
            else:
                category = "danger"
                flash(["Incorrect password"], category)
                return redirect(url_for("profile_page"))

        if form.errors != {}:
            for error_msg in form.errors.values():
                category = "danger"
                flash(error_msg, category)
            return redirect(url_for("profile_page"))

def task():
    global count
    count=1




# Route to handle password reset requests
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        # Get the user's email address from the form submission
        email = request.form['email']

        # Check if the email exists in the database
        user = db.execute('SELECT * FROM users WHERE email = ?', email)
        if user is None:
            flash('Invalid email address', 'error')
            return redirect(url_for('reset_password'))

        # Generate a unique key for password reset
        reset_key = str(uuid.uuid4())

        # Store the reset key and email in the database
        expires_at = datetime.utcnow() + timedelta(hours=1)
        db.execute('INSERT INTO password_resets (reset_key, email, expires_at) VALUES (?, ?, ?)',
                   reset_key, email, expires_at)


        # Send an email to the user with the password reset link
        password_reset_url = url_for('reset_password_confirm', reset_key=reset_key, _external=True)
        #TODO:
        # send_password_reset_email(email, password_reset_url)

        # Redirect to a page thanking the user for initiating the password reset process
        flash(['We have sent a password reset link to your email address'], 'success')
        return redirect(url_for('login_page'))

    return render_template('forget_pas.html')

# Route to handle password reset confirmation
@app.route('/reset_password_confirm/<string:reset_key>', methods=['GET', 'POST'])
def reset_password_confirm(reset_key):
    form= PasForm()
    # Check if the reset key exists in the database
    password_reset = db.execute('SELECT * FROM password_resets WHERE reset_key = ?', reset_key).fetchone()
    if password_reset is None:
        flash('Invalid password reset link', 'error')
        return redirect(url_for('login_page'))

    # Check if the reset key has expired
    if datetime.utcnow() > password_reset['expires_at']:
        flash('The password reset link has expired', 'error')
        return redirect(url_for('reset_password'))

    if request.method == 'POST':
        # Get the new password from the form submission
        password = form.password.data

        # Hash the new password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

        # Update the user's password in the database
        db.execute('UPDATE users SET hash = ? WHERE email = ?', hashed_password, password_reset['email'])


        # Remove the password reset record from the database
        db.execute('DELETE FROM password_resets WHERE reset_key = ?', reset_key)

        # Redirect to a page thanking the user for resetting their password
        flash('Your password has been reset successfully', 'success')
        return redirect(url_for('login'))

    return render_template('reset_password.html',form=form)
    """
   