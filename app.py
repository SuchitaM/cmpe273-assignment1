import sys
from flask import Flask
from github import Github

app = Flask(__name__)

g = Github()
user = sys.argv[1].split("/", 4)[3]
rep = sys.argv[1].split("/", 4)[4]
contents = []

@app.route("/v1/<filename>")
def readf(filename):
    repo=g.get_user(user).get_repo(rep)
    if filename.endswith('.yml'):
        content = repo.get_file_contents(filename).content.decode(repo.get_contents(filename).encoding)
        return content
    else:
        return "error.. no yml file found"
    
    if filename.endswith('.json'):
        content = repo.get_file_contents(filename).content.decode(repo.get_contents(filename).encoding)
        return content
    else:
        return "error"

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
