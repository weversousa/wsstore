from app.database import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    __table_args__ = (
        db.PrimaryKeyConstraint('id', name='pk_users'),
        db.UniqueConstraint('email', name='uq_users'),
        {'schema': 'public'},
    )

    def save(self):
        db.session.add(self)
        db.session.commit()
