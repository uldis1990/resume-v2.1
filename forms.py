from flask_wtf import FlaskForm
from wtforms import TextAreaField,IntegerField,StringField,PasswordField,SubmitField,validators
from wtforms.fields import DateField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_uploads import UploadSet, IMAGES

images = UploadSet('images', IMAGES)

class RegisterForm(FlaskForm):
    username = StringField('Username:',[validators.Length(min=2,max=30), validators.DataRequired()])
    email = StringField('E-mail: ',[validators.Email(),validators.DataRequired()])
    password = PasswordField('Password: ',[validators.DataRequired()])
    password2 = PasswordField('Re-enter password: ',[validators.EqualTo('password'),validators.DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username:',[validators.DataRequired()])
    password = PasswordField('Password: ',[validators.DataRequired()])
    login = SubmitField('Login')

class ProjectForm(FlaskForm):
    project = StringField('Project title:',[validators.DataRequired()])
    project_loc = StringField('Location:',[validators.DataRequired()])
    type = StringField('Type: ',[validators.DataRequired()])
    gool = StringField('Project goals: ',[validators.DataRequired()])
    image = FileField('Project image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    about_project = TextAreaField('About: ',[validators.DataRequired()])
    start_date = DateField('Start date:',[validators.DataRequired()])
    end_date = DateField('End date:')
    link_project = StringField('Links:',[validators.DataRequired()])
    add = SubmitField('Submit')


class WorkForm(FlaskForm):
    company = StringField('Company:',[validators.DataRequired()])
    comp_loc = StringField('Location: ',[validators.DataRequired()])
    position = StringField('Position: ',[validators.DataRequired()])
    about_work = TextAreaField('About: ',[validators.DataRequired()])
    image = FileField('Company image:', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    start_date = DateField('Start date:',[validators.DataRequired()])
    end_date = DateField('End date:')
    link_comp = StringField('Links:',[validators.DataRequired()])
    add = SubmitField('Submit')


class EduForm(FlaskForm):
    school = StringField('School:',[validators.DataRequired()])
    school_loc = StringField('Location: ',[validators.DataRequired()])
    type = StringField('Type: ',[validators.DataRequired()])
    grade = StringField('Grade: ',[validators.DataRequired()])
    image = FileField('School image:', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    about_edu = TextAreaField('About: ',[validators.DataRequired()])
    start_date = DateField('Start date:',[validators.DataRequired()])
    end_date = DateField('End date:')
    link_edu = StringField('Links:',[validators.DataRequired()])
    add = SubmitField('Submit')

class SkilsForm(FlaskForm):
    skill = StringField('Skill:',[validators.DataRequired()])
    level = StringField('Level: ',[validators.DataRequired()])
    image = FileField('Skill image:', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    about_skill = TextAreaField('About: ',[validators.DataRequired()])
    add = SubmitField('Submit')

class HobForm(FlaskForm):
    hobby = StringField('Hobby:',[validators.DataRequired()])
    image = FileField('Hobby image:', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    about_hobby = TextAreaField('About: ',[validators.DataRequired()])
    duration = StringField('Duration: ',[validators.DataRequired()])
    add = SubmitField('Submit')

class SocialForm(FlaskForm):
    social = StringField('Social:',[validators.DataRequired()])
    image = FileField('Social image:', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    activity = TextAreaField('Activity: ',[validators.DataRequired()])
    link = StringField('Link: ',[validators.DataRequired()])
    add = SubmitField('Submit')

class RefForm(FlaskForm):
    ref_name = StringField('Name:',[validators.DataRequired()])
    company = StringField('Company:',[validators.DataRequired()])
    image = FileField('References image:', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    referance = TextAreaField('References: ',[validators.DataRequired()])
    mob = StringField('Company phone: ',[validators.DataRequired()])
    email = StringField('Company e-mail: ',[validators.DataRequired()])
    link = StringField('Company link: ',[validators.DataRequired()])
    add = SubmitField('Submit')

class GolsForm(FlaskForm):
    gol_pos = StringField('Gols:',[validators.DataRequired()])
    image = FileField('Gols image:', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    about_gol = TextAreaField('About:',[validators.DataRequired()])
    link = StringField('Link: ',[validators.DataRequired()])
    add = SubmitField('Submit')

#make generator for token
class TokForm(FlaskForm):

    exp_date = DateField('End date:',[validators.DataRequired()])
    reuse_count =IntegerField('Reuse count:',[validators.DataRequired()])
    add = SubmitField('Submit')

class CssForm(FlaskForm):
    element_id = IntegerField('ElementId:')
    css_class = TextAreaField('CSS class:')
    add = SubmitField('Submit')

class ProfileForm(FlaskForm):
    username = StringField('Username:',[validators.DataRequired()])
    first_name = StringField('Name: ',[validators.DataRequired()])
    last_name = StringField('Surname: ',[validators.DataRequired()])
    birthday = DateField('Birthday:',[validators.DataRequired()])
    gol_cv = StringField('Profession: ',[validators.DataRequired()])
    family_status = StringField('Family status: ',[validators.DataRequired()])
    nation = StringField('Nationality: ',[validators.DataRequired()])
    image = FileField('Profile picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    about_me = TextAreaField('About: ',[validators.DataRequired()])
    adress = StringField('Adress: ',[validators.DataRequired()])
    email = StringField('E-mail: ',[validators.Email(),validators.DataRequired()])
    full_mob = StringField('Mob: ',[validators.DataRequired()])
    password = PasswordField('Password: ',[validators.DataRequired()])
    cheing = SubmitField('Submit')

class LangForm(FlaskForm):
    lang = StringField('Language:',[validators.DataRequired()])
    level = StringField('Level: ',[validators.DataRequired()])
    level_by = StringField('Level by: ',[validators.DataRequired()])
    add = SubmitField('Submit')

class SocForm(FlaskForm):
    web = StringField('Web link:',[validators.DataRequired()])
    f_book = StringField('Facebook link: ',[validators.DataRequired()])
    twiter = StringField('Twiter link: ',[validators.DataRequired()])
    instag = StringField('Instagram link: ',[validators.DataRequired()])
    add_info = TextAreaField('ADITION DETALS:',[validators.DataRequired()])
    add = SubmitField('Submit')

class PasForm(FlaskForm):
    password1 = PasswordField('Old password: ',[validators.DataRequired()])
    password = PasswordField('New password: ',[validators.DataRequired()])
    password2 = PasswordField('Re-enter new password: ',[validators.EqualTo('password'),validators.DataRequired()])
    create = SubmitField('Change')
