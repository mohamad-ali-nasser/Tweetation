"""

Main application and routing logic for Tweetation

"""


from flask import Flask
from .models import DB


def create_app():
	"""Create and configure an instance of the Flask application."""
	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
	DB.init_app(app)

	@app.route('/')
	def root():
		return 'Welcome to Tweetation!'


	return app

if __name__ == "__main__":
	app = create_app()
	app.run(debug=True)
