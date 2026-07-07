from flask_sqlalchemy import SQLAlchemy

finggu_db = SQLAlchemy()

class FingguApiPerformance(finggu_db.Model):
    __tablename__ = 'finggu_api_performance'
    id = finggu_db.Column(finggu_db.Integer, primary_key=True)
    endpoint = finggu_db.Column(finggu_db.String(255), nullable=False)
    response_time = finggu_db.Column(finggu_db.Float, nullable=False)
    timestamp = finggu_db.Column(finggu_db.DateTime, server_default=finggu_db.func.now())
