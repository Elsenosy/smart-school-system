## Requirements
- Django 

    ``` $ pip install Django ``` 

- Rest framework

    ``` $ pip install djangorestframework ```

    ``` $ pip install markdown ``` # Markdown support for the browsable API.

    ``` $ pip install django-filter  ``` 

- Mysql client

    ``` $ pip install mysqlclient ``` 

- Django core headers

    ``` $ pip install django-cors-headers ``` 

## Run the project 
- Create a new database and change the connection parameters in ``` SmartSchoolProject/setting.py```

- Run Database migrations:

    ``` $ cd SmartSchoollProject/ ```

    ``` $ python manage.py makemigrations ```

    ``` $ python manage.py migrate ```
- Create a super user with token
    ``` $ python manage.py createsuperuser --username <username> --email <email> ```

   ** Enter the password

    - Create token for the user 

        ``` $ python manage.py drf_create_token <username> ``` 


- Run the project server using the following commands: 

    ``` $ python manage.py runserver```

- Go to the browser and launch 
    ``` http://127.0.0.1:8000/admin ```


### Have a nice coding time :) 

