from flask import Flask, request, session, redirect, url_for, render_template, flash,Blueprint

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
'username': 'admin',
'password': '123'
}

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['user'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('tasks.view_tasks'))  # Assuming you have a route to view tasks
        else:
            flash('Invalid credentials. Please try again.', 'danger')
    
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login') )
