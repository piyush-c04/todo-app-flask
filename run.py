from app import create_app,db
from app.models import Task

app = create_app()

with app.app_context(): #important to use app context for database operations
    db.create_all()  # Create database tables if they don't exist
    
if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application in debug mode