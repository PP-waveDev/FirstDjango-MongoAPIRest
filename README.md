# Basic API Rest written in Python
This API has been created following [Bezkoder's tutorial](https://bezkoder.com/django-mongodb-crud-rest-framework/).
It consists in a single model with its CRUD functions implemented.

### Technologies Used
* [Python 3](https://www.python.org/download/releases/3.0/)
* [DJango](https://www.djangoproject.com/)
* [MongoDB](mongodb.com)
* [DJango Rest Framework](https://www.django-rest-framework.org/)

## Getting Ready (Instalation)
 Optional: It is very usual to work with DJango using virtual environments.
 
 1. Install Python
 ``` shell
 pip install python
 ```
 2. Install DJango
 ``` shell
 pip install DJango
 ```
 3. Install DJango Rest Framework
 ``` shell
 pip install djangorestframework
 ```
 
 After that, We just have to migrate:
 ``` shell
 python manage.py migrate
 ```
 
 Finally, It would be a good idea to fill the table with some data. Import data from 'datosEjemplo.json' inside the folder 'Datos de ejemplo'. 
 
 **And that's It, We are ready to go!**
 
 ## Initializing the service
 To do so, it is as easy as executing the following:
 ``` shell
 python manage.py runserver
 ```

 ## About the model
 We are storing a collection of tutorials.

 ## Supported opperations
Consult PostMan for further details.
