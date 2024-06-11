def render_student_list(students):
    return [
        {
            "id": student.id,
            "name": student.name,
            "last_name": student.last_name,
            "age": student.age,
            "email": student.email,
            "school_year": student.school_year,
            "subjects": student.subjects,
        }
        for student in students
    ]

def render_student_detail(student):
    return {
        "id": student.id,
        "name": student.name,
        "last_name": student.last_name,
        "age": student.age,
        "email": student.email,
        "school_year": student.school_year,
        "subjects": student.subjects,
    }