# SGE - Stock Management System 

This Django project include Frontend, backend and API RESTful, with this allow users interact with application with a friendly interface while allowing to use API to expand for other plataforms.


##  Functionality 
- Frontend: has been build with HTML, CSS, JavaScript mainly using bootstrap5
- Backedn: Busines logic and Management of data base is using Django
- API: API RESTful using CRUD operations (Create, Read, Update and Delete)
- Authentication: System has a login with control access to the users in the website and with the API with JWT Authentication


## Installation

Clone repository 

```bash
  git clone
  cd my-project
```

Create a virtual env
```bash
  python3 -m venv venv
```
Activate virtual env 
```bash
  source venv/bin/activate #linux
  venv/Scripts/activate # windows
```
Install requirements make sure the virtual envioroment is activate
```bash
  pip install requirements.txt
```

##  Config database
Create migrations
```bash
  python manage.py makemigrations
```
Apply migrations
```bash
  python manage.py migrate
```
Create a super user
```bash
  python manage.py createsuperuser
```
And finaly you can use the app 
```bash
  python manage.py runserver
```
## API Reference
You need to have made an account in the website it self 
### Get authentication

```http
  POST localhost:8000/api/v1/authentication/token/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required** |
| `password` | `string` | **Required**|

Request example
```json
  {
      "username": "your_username",
      "password": "your_password"
  }
```
Response example
```json 
  {
      "access": "<access_token>",
      "refresh": "<refresh_token>"
  }
```

## Verify token
```bash
  POST /api/v1/authentication/token/verify/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | **Required**: Access token to verify |

Request example
```json
  {
      "token": "<access_token>"
  }
```
Response:

Status Code 200: Token is valid.

Status Code 401: Token is invalid or expired.


Refresh tokken
```bash
  POST /api/v1/authentication/token/refresh/
```
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `refresh` | `string` | **Required**: Refresh token to renew access |

Sample Request:

``` json
{
    "refresh": "<refresh_token>"
}
```

Sample Response:
``` json
{
    "access": "<new_access_token>"
}
```
#### Get item

```http
  GET api/v1/brands/ # get all brands
  POST api/v1/brands/ # create a new brand
  GET api/v1/brands/1/ # get brand with Id 1
  PUT api/v1/brands/1/ # Update brand
  DELETE api/v1/brands/1/ # delete brand
```

Examples
```
 api/v1/categories/
 api/v1/inflows/
 api/v1/outflows/
 api/v1/products/
 api/v1/suppliers/
```