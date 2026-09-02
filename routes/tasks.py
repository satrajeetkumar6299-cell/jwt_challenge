from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from services.task_service import TaskService


tasks_bp = Blueprint("tasks", __name__)
task_service = TaskService()


@tasks_bp.get("")
@jwt_required()
def get_tasks():
    user_id = int(get_jwt_identity())

    tasks = task_service.get_user_tasks(user_id)

    return jsonify([task.to_dict() for task in tasks]), 200


@tasks_bp.post("")
@jwt_required()
def create_task():
    user_id = int(get_jwt_identity())

    data = request.get_json(silent=True)

    if not data:
        return jsonify({"message": "Invalid JSON"}), 400

    title = data.get("title")
    description = data.get("description", "")

    if not title:
        return jsonify({"message": "title is required"}), 400

    task = task_service.create_task(
        user_id,
        title,
        description
    )

    return jsonify(task.to_dict()), 201


@tasks_bp.put("/<int:task_id>")
@jwt_required()
def update_task(task_id):
    user_id = int(get_jwt_identity())
    data = request.get_json(silent=True)

    if not data:
        return jsonify({"message": "Invalid JSON"}), 400

    task, status = task_service.update_task(
        task_id,
        user_id,
        data
    )

    if status == 404:
        return jsonify({"message": "Task not found"}), 404

    if status == 403:
        return jsonify({"message": "Forbidden"}), 403

    return jsonify(task.to_dict()), 200


@tasks_bp.delete("/<int:task_id>")
@jwt_required()
def delete_task(task_id):
    user_id = int(get_jwt_identity())

    status = task_service.delete_task(task_id, user_id)

    if status == 404:
        return jsonify({"message": "Task not found"}), 404

    if status == 403:
        return jsonify({"message": "Forbidden"}), 403

    return "", 204
