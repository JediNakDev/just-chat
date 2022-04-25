from website import create_app
from website.firebase import initialize_firebase

initialize_firebase()
app = create_app()

if __name__ == '__main__':
    app.run(debug=True,port=5001)