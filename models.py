from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class InstanceConfig(db.Model):
    __tablename__ = 'instance_config'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    role = db.Column(db.String(20))
    lastCheckTime = db.Column(db.DateTime)

    # email = db.Column(db.String(50), unique=True)
    # password = db.Column(db.String(128))

    def __repr__(self):
        return f'<User {self.name}>'



#