from flask import Blueprint, render_template, redirect, url_for, request, flash,session
from werkzeug.security import generate_password_hash ,check_password_hash 
from app import db                                    
from app.models import User                          

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('tasks.view_task'))
    
    return redirect(url_for('auth.login'))
@auth_bp.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get('password')
        
        hashed_password = generate_password_hash(password, method='scrypt')
        
        new_user = User(username=username, password=hashed_password)
        
        try:
            db.session.add(new_user)  
            db.session.commit()      
            flash("Account created successfully! Please login.", "success")
            return redirect(url_for('auth.login')) 
        except Exception as e:
            db.session.rollback()    
            flash("Username already exists or something went wrong.", "error")
            
    return render_template('register.html') 

@auth_bp.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = User.query.filter_by(username=username).first()
    
        if user and check_password_hash(user.password,password):
            session['user'] = user.username
            session['user_id'] = user.id
            flash(f"welcome Back,{user.username}!","success")
            return  redirect(url_for("tasks.view_task"))
        else:
             flash("Incorrect passoword or username!","error")
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop("user",None)
    session.pop("user_id",None)
    return redirect(url_for("auth.login"))