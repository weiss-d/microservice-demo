# microservice-demo
Simple demo of microservice in Flask.

Personal project for learning Flask and Docker.

The app returns a list of files and folders and some of their properties from given subdirectory of a directory specified in `cofig.py`.

HTTP request goes like this:
```
http://localhost:5000/api/meta/<folder_name>
```

Output is in JSON format:
```javascript
{
    "data":[
        {
            "name": "name",
            "type": "file",
            "time": "time"
        },
        {
            "name": "name",
            "type": "file",
            "time": "time"
        },
    ]
}
```
If specified folder doesn't exist output will be:
```javascript
{
    "error": "<Python error message>"
}
```
## Install & Run
```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python -m microservice_demo.app
```
## Docker
```bash
$ docker build . -t microservice_demo
$ docker run --rm -it -p 5000:5000 microservice_demo
```
## Questions
This is training project, but if you stumbled upon it searching for examples and have any questions - feel free to ask them through an issue.
