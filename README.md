# microservice-demo
Simple demo of microservice in Flask.

Personal project for learning Flask and Docker.

The app returns a list of files and folders in given directory in JSON format as a result of /api/meta/ GET request.
```javascript  
{
    “data”:[
        {
            “name”: ”name”,
            “type”: “file”,
            “time”: “time”
        },
        {
            “name”: ”name”,
            “type”: “file”,
            “time”: “time”
        },
    ]
} 
```  
