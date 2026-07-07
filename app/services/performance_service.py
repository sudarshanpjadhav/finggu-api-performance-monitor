from app.models import FingguApiPerformance
from app import finggu_db


def finggu_get_performance_metrics():
    fingguVar_metrics = finggu_db.session.query(FingguApiPerformance).all()
    return [{'endpoint': metric.endpoint, 'response_time': metric.response_time, 'timestamp': metric.timestamp} for metric in fingguVar_metrics]
