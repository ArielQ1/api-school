from flask import Blueprint, request, jsonify
from app.models.studen_model import Student
from app.views.student_view import render_student_detail, render_student_list
from app.utils.decorators import roles_required, jwt_required

student_bp = Blueprint("student", __name__)

@student_bp.route("/students", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_students():
    students = Student.get_all()
    return jsonify(render_student_list(students))

@student_bp.route("/students/<int:id>", methods=["GET"])
@jwt_required
@roles_required(roles=["admin", "user"])
def get_student(id):
    student = Student.get_by_id(id)
    if student:
        return jsonify(render_student_detail(student))
    return jsonify({"error":"studen no encontrado"}), 404

@student_bp.route("/students",methods=["POST"])
@jwt_required
@roles_required(roles=["admin"])
def create_student():
    data = request.json
    name = data.get("name")
    last_name = data.get("last_name")
    age = data.get("age")
    email = data.get("email")
    school_year = data.get("school_year")
    subjects = data.get("subjects")

    if not name or not last_name or not email or not school_year or not subjects:
        return jsonify({"error":"faltan datos"}), 400
    
    student = Student(name=name, last_name=last_name, age=age, email=email, school_year=school_year, subjects=subjects)
    student.save()
    return jsonify(render_student_detail(student)),201

@student_bp.route("/students/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_student(id):
    student = Student.get_by_id(id)
    if not student:
        return jsonify({"error":"student no encontrado"}), 404
    data = request.json
    name = data.get("name")
    last_name = data.get("last_name")
    age = data.get("age")
    email = data.get("email")
    school_year = data.get("school_year")
    subjects = data.get("subjects")

    student.update(name=name, last_name=last_name, age=age, email=email, school_year=school_year, subjects=subjects)
    return jsonify(render_student_detail(student)), 200

@student_bp.route("/students/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_student(id):
    student = Student.get_by_id(id)
    if not student:
        return jsonify({"error":"student no encontrado"}), 404
    student.delete()
    return jsonify({"message":"student eliminado"}), 204
