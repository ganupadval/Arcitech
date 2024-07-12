HERE IS ASSIGNMENT WORK FOR DJANGO INTERN POSTION AT ARCITECH:

Assignment:-
E-commerce Website: Build a simple e-commerce website using Django where users can browse products, add them to cart, and make purchases.
Include features like user accounts, product categories, search functionality, and a checkout process.


Steps:
1. Setting Up the Environment:
- Setting up development envrionment is a crucial task because the different applications on the system may require different version of packages in order to operate properly
- If we install all packages globaly it might arise a problem with other working applications with diffrent versions.

- to setup python env follow these cmd:
- "python -m venv environment_name"
- after that a folder will be created in that directory with that environment name
- use "env_name/scripts/activate" to activate the environment
- once you see (env_name) in front of your env you are good to go!

2. Installing Django:
- Once you activate the environment use following cmd to install the packages:
- "pip install django"

3. Starting New Project:
- Use the following cmd to start the new django project:
- "django-admin startproject arcitech"

- 
4. Creating Apps
Create two Django apps, store and users, to handle the e-commerce functionality and user management.

python manage.py startapp store
python manage.py startapp users

5. Setting Up Models
Define the necessary models in the store and users apps. This includes models for products, categories, carts, orders, and users.

6. Writing Views
Create views to handle product listing, product detail, adding to cart, cart view, checkout process, user registration, login, and logout.

7. Configuring Settings
Update the project settings to include the store and users apps, configure the database, and set up static files and templates.

8. Creating Superuser
Create a superuser to access the Django admin interface:

Command:
python manage.py createsuperuser

9. Running the Project
Apply migrations and start the development server to run the project.

Commands:
python manage.py migrate
python manage.py runserver
