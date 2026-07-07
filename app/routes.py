from flask import jsonify, request
from app import finggu_app
from app.services.performance_service import finggu_get_performance_metrics

@finggu_app.route('/api/performance', methods=['GET'])
def finggu_performance():
    fingguVar_metrics = finggu_get_performance_metrics()
    return jsonify(fingguVar_metrics)
