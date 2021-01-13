# ============== Import Statements ============== #
from flask import render_template, request, Blueprint
from flaskblog.models import Post

# ============== Blueprint Statement ============== #
main = Blueprint('main', __name__)

# ============== Main/Home Route ============== #
@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

# ============== About Route ============== #
@main.route("/about")
def about():
    return render_template('about.html', title='About')

# ============== Rankings Route ============== #
@main.route("/rankings")
def rankings():
    return render_template('rankings.html', title='Rankings')

# ============== Forum Route ============== #
@main.route("/forum")
def forum():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
    return render_template('forum.html', title='Forum', posts=posts)