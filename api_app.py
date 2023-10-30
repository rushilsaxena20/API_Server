from flask import Flask, request, jsonify #jsonify formats the output properly. ie, it returns a valid json
from flask_sqlalchemy import SQLAlchemy #Sqlalchemy in an orm(object relational mapper) through this we can create and make changes in db using python.

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' #to connect to db which is present in same folder.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Just to remove a warning.
db=SQLAlchemy(app) #initialize the db

class Posts(db.Model): #created this class to tell flask what all to store in db. 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    comments = db.Column(db.String(800))

    def __repr__(self) -> str:  
        return f"{self.username} - {self.comments}" 
        
@app.route("/")
def hello_world():
    return "Hi! This is a sample API_server, to get all the data add '/posts' in the url, to get specific data of the user add '/posts/(userid eg: 1')"

@app.route("/posts")
def view_posts():
    posts = Posts.query.all()
    output = []
    for p in posts: 
        post_data = {"username" : p.username, "comments" : p.comments}
        output.append(post_data)
    return jsonify({"posts":output})

@app.route("/posts/<id>")
def get_post(id):
    post = Posts.query.get(id) #Query has a get function that supports querying by the primary key of the table, which is id, here I could also use get_or_404
    return jsonify({"name" : post.username, "comments" : post.comments})

@app.route("/posts", methods=['POST'])
def add_post():
    post = Posts(username=request.json['username'], comments=request.json['comments']) # request.json is used to get the json data from the comming request.
    db.session.add(post)
    db.session.commit()
    return {'id' : post.id}

@app.route("/posts/<id>", methods=['DELETE'])
def delete_post(id):
    post = Posts.query.get(id) #Query has a get function that supports querying by the primary key of the table, which is id.
    if post is None:
        return {"error":"Please give a valid post id"}
    db.session.delete(post)
    db.session.commit()
    return {"message":"deleted post with the given id"}

if __name__ == "__main__":
    app.run(debug=True)