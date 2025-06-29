from flask import Flask, request, Blueprint, render_template, redirect, url_for, flash, session
from app import db
from app.models import Task

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/')
def view_tasks():
    if 'user' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)


@tasks_bp.route('/add', methods=['POST'])
def add_task():
    if 'user' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('auth.login'))
    
    title = request.form.get('title')
    if title:
        new_task = Task(title=title)
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
    else:
        flash('Task title cannot be empty.', 'danger')
    
    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/toggle/<int:task_id>', methods=['POST'])
def toggle_status(task_id): 
    if 'user' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('auth.login'))

    task = Task.query.get_or_404(task_id)

    if task.status == 'Pending':
        task.status = 'Working'
    elif task.status == 'Working':
        task.status = 'Completed'
    else:
        task.status = 'Pending'

    db.session.commit()
    flash(f'Task "{task.title}" status updated to {task.status}', 'info')

    return redirect(url_for('tasks.view_tasks'))

@tasks_bp.route('/clear_tasks', methods=['POST'])
def clear_tasks():
    if 'user' not in session:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('auth.login'))
    
    Task.query.delete()
    db.session.commit()
    flash('All tasks cleared!', 'success')
    
    return redirect(url_for('tasks.view_tasks'))
