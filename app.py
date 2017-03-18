import sys
import json
import yaml
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
    fn = filename.split(".")[0]

    if filename.endswith('.yml'):
        content = repo.get_file_contents(fn+".yml").content.decode(repo.get_contents(fn+".yml").encoding)
        return content
    
    elif filename.endswith('.json'):
        content = json.dumps(yaml.load(repo.get_file_contents(fn+".yml").content.decode(repo.get_contents(fn+".yml").encoding)))
        return content
        
    else:
        return "error"

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
