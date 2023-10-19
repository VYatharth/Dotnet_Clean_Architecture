# This app is created using Python3, FastAPI and SQLite


# For running from the shared image
- Run **docker run -d -p 8080:8080 vyathartha/user-app** to create and run container
- open **http://localhost:8080/docs** in browser

# For building your code on local
- Install Python3
- Create python environment **python -m venv user-app-env**
- Run **"pip install -r requirements.txt"** to install the dependencies
- Run **uvicorn app.main:app --reload**  to start server and run app

# For using on docker
- Create docker image **docker build -t user-app .**
- Run **docker run -p 8080:8080 user-app** to create and run container
- Run **uvicorn main:app --reload**  to start server and run app
- open **http://localhost:8080/docs** in browser
