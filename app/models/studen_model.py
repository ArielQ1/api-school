from app.database import db
import json

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(64), nullable=False)
    school_year = db.Column(db.String(64), nullable=False)
    subjects = db.Column(db.String(64), nullable=False)

    def __init__(self, name, last_name, age, email, school_year, subjects=["inf-111", "inf-112", "inf-113"]):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.school_year = school_year
        self.subjects = json.dumps(subjects)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Student.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Student.query.get(id)
    
    def update(self, name=None, last_name=None, age=None, email=None, school_year=None, subjects=None):
        if name is not None:
            self.name = name
        if last_name is not None:
            self.last_name = last_name
        if age is not None:
            self.age = age
        if email is not None:
            self.email = email
        if school_year is not None:
            self.school_year = school_year
        if subjects is not None:
            self.subjects = json.dumps(subjects)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()