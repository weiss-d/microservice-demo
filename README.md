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
