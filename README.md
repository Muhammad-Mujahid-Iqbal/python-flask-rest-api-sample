# python-flask-rest-api-sample

Steps to run:
1. Run the flask server using app.py
2. Post the sample user data using post api on localhost:8000/users. Post API does not need any authentication. Formrat of Post is:                        {first_name(str),last_name(str),email(str),phone(int),adress(str),password(str)}. All fields are required in POST API, else code wont work.
3. For all other APIs, first acquire the token from localhost:8000/api/token using basic authentication using email and password which you just posted
4. After acquiring token, call all APIs by sending this Bearer Token
5. Single get/patch/delete is on url localhost:8000/user/<id>
