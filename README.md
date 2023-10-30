# API_Server
This is a fake API server which will fetch the json data and present it.

## How to run
Install all the dependencies, just clone the project and run the following command: `pip install -r requirements.txt`
Now that you have the required modules run the api_app.py file using command: `python api_app.py`

<hr>

## Getting all the Posts
After running the api_app.py file: Command: **python api_app.py**, follow the link provided and add `/posts` to view all the posts.

<hr>

## Getting a particular post from postId
Follow the above mention steps, and add `/posts/<any userid number>`, and you will be able to see only that username and comment.

<hr>

## To create a record
For the creation of a new record, you would need POSTMAN tool or you can add "Thunder Client" extension in VS Code to send GET,POST,DELETE etc requests to an api endpoint.
After installing POSTMAN, just select the POST method, give the api end point link provided by running the `api_app.py` file, select body to raw and json enter the json data which should look like:
```
{
    "username" : "test"
    "comments" : "this is for testing"
}
```
After sending the request, the server would return the id of the username.

<hr>

## To delete a record
To delte a record, simply give the 'id' with the url:`/posts/<any userid number>`, select DELETE method and send the request, the server will delte the entry and give a conformation message:
```
{
    "message": "deleted post with the given id"
}
```