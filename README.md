# API Development

## Table of contents:
 1. [Introduction](https://github.com/ISTE-VESIT-ORG/API-Development-2021/blob/API-learning/README.md#introduction)
 2. [Insomnia setup](https://github.com/ISTE-VESIT-ORG/API-Development-2021/blob/API-learning/README.md#api-testing)
 3. [REST API](https://github.com/ISTE-VESIT-ORG/API-Development-2021/blob/API-learning/README.md#rest-api)
    - [GET](https://github.com/ISTE-VESIT-ORG/API-Development-2021/blob/API-learning/README.md#get)
    - [POST](https://github.com/ISTE-VESIT-ORG/API-Development-2021/blob/API-learning/README.md#post)
    - [DELETE](https://github.com/ISTE-VESIT-ORG/API-Development-2021/blob/API-learning/README.md#delete)

## Introduction
This is boilerplate for basic understanding of devloping API and understanding its types and function using Flask
 - [APIs in a nutshell](https://www.youtube.com/watch?v=s7wmiS2mSXY)
 - [APIs in depth](https://www.youtube.com/watch?v=GZvSYJDk-us&t=1293s)

To run the app
```shell
$ python app.py
```

## API Testing
API can be easily tested with many utility applications like [Insomnia](https://insomnia.rest/download), [Postman](https://www.postman.com/downloads/)...
 We will be using `Insomnia` for testing our APIs
 
After downloading Insomnia from [here](https://insomnia.rest/download), open `Insomnia.exe`
Follow the given steps:

Setting up Request collection
```java
Dashboard => Create => Request collection => Give desired name to the collection
```

![New Request collection](https://user-images.githubusercontent.com/72487782/137669703-63c5107c-e846-4815-988d-f90b06e1d006.png)

 - Click on `New Request`
 - Give desired name for the new request
 - Select ***GET***
 - Click on ***Create***

![image](https://user-images.githubusercontent.com/72487782/137670276-6971f444-c14f-4a49-85cd-8f119173c11d.png)

![image](https://user-images.githubusercontent.com/72487782/137670990-7c13aa17-eb33-4d3d-af68-7c4f61691e1b.png)

🌟Insomnia is now ready for sending requests and tests APIs!🌟

❗ _Note: By default flask app is served on `http://127.0.0.1:5000/`, so if you have made any changes make sure to use that link_ ❗

## REST API

### [GET:](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET)

```python
http://127.0.0.1:5000/
```

![image](https://user-images.githubusercontent.com/72487782/137673383-bb503a88-238e-4d3f-b737-2e1cc1ce9692.png)

```python
# Get JSON of Agents
http://127.0.0.1:5000/getAgents
```

![image](https://user-images.githubusercontent.com/72487782/137673444-fac3fb23-1cdb-4dc6-82c2-8081a1e927fe.png)

```python
# Get JSON of Weapons
http://127.0.0.1:5000/getWeapons
```

![image](https://user-images.githubusercontent.com/72487782/137673459-8f715dd5-8aaa-42d0-897b-7a4b795eacba.png)
---
### [POST:](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)

```python
# Insert a weapon in the list using POST request
http://127.0.0.1:5000/addWeopens/<name of weapon>
```

![image](https://user-images.githubusercontent.com/72487782/137673786-181253df-8689-41fc-9539-e570cf210509.png)

---

### [DELETE:](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE)

```python
# Delete a weapon in the list using DELETE request
http://127.0.0.1:5000/deleteWeapon/<name of weapon>
```

![image](https://user-images.githubusercontent.com/72487782/137673889-643b105d-e1d7-4255-aa98-6313e058fab8.png)





