from app import db




class Course(db.Model):
    course_id=db.Column(db.Integer,primary_key=True)
    course_name=db.Column(db.String)
    course_author=db.Column(db.String)
    course_endpoint=db.Column(db.String,unique=True)


 