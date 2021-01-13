# ============== Import Statements ============== #
from flask import Blueprint, render_template

# ============== Blueprint Statement ============== #
errors = Blueprint('errors', __name__)

# ============== Error 403 Route ============== #
@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

# ============== Error 404 Route ============== #
@errors.app_errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404

# ============== Error 500 Route ============== #
@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500