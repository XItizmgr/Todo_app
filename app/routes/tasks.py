from flask import Blueprint, render_template, redirect, session, request, url_for, flash
from app import db
from app.models import Tasks

tasks_bp = Blueprint("tasks", __name__)



@tasks_bp.route("/view_task", methods=["GET"])
def view_task():
    current_user_id = session.get("user_id")
    if not current_user_id:
        flash("Please log in to view your task.", "error")
        return redirect(url_for("auth.login"))
    user_tasks = Tasks.query.filter_by(user_id=current_user_id).all()
    return render_template("tasks.html", task=user_tasks)  


@tasks_bp.route("/add", methods=["POST"])
def add():
    current_user_id = session.get("user_id")
    if not current_user_id:
        flash("Please log in in to view your task.", "error")
        return redirect(url_for("auth.login"))
    adding_task = request.form.get("adding_task")

    if adding_task:
        new_task = Tasks(title=adding_task, user_id=current_user_id)
        try:
            db.session.add(new_task)
            db.session.commit()
            flash("New task is added succesfully", "success")

        except:
            db.session.rollback()
            flash("Something went wrong plz try again", "error")
        return redirect(url_for("tasks.view_task"))


@tasks_bp.route("/delete/<int:task_id>")
def delete(task_id):
    current_user_id = session.get("user_id")
    if not current_user_id:
        return redirect(url_for("auth.login"))

    task_to_delete = Tasks.query.get_or_404(task_id)

    if task_to_delete.user_id == current_user_id:
        try:
            db.session.delete(task_to_delete)
            db.session.commit()
            flash("Task removed succesfull", "success")
        except:
            db.session.rollback()
            flash("Could not delete task.", "error")
    else:
        flash("You do not have permission to delete this task!", "error")

    return redirect(url_for("tasks.view_task"))


@tasks_bp.route("/status/<int:task_id>", methods=["POST"])
def status_change(task_id):
    current_user_id = session.get("user_id")
    if not current_user_id:
        return redirect(url_for("auth.login"))
    task = Tasks.query.get_or_404(task_id)
    if task.user_id == current_user_id:
        if task.status == "pending":
            task.status = "working"
        elif task.status == "working":
            task.status = "complete"
        else:
            task.status = "pending"
        db.session.commit()
        flash(f"Task status updated to {task.status}!", "success")
    else:
        flash("You do not have permission to modify this task!", "error")
    return redirect(url_for("tasks.view_task"))
