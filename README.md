# Django Custom JWT Authentication with Username or Phone Number

- You can check my article about this topic on Medium by clicking on [here](https://medium.com/codex/django-rest-framework-custom-jwt-authentication-backend-17bbd178b4fd).
- [Also it is available on Youtube :)](https://youtu.be/goTIo3g4gGQ)

# Structure

- [`management`](src/apps/management/) folder holds the core functions for authentication and models.
- [`authentication.py`](src/apps/management/authentication.py) holds the custom authentication logic.
- [`views.py`](src/apps/management/views.py) have pure Django views for password change.
- [`views.py`](src/apps/management/api/views.py) holds Django Rest Framework views for management endpoints.
- [`serializers.py`](src/apps/management/api/serializers.py) holds serializer classes.


# Business Logic

- In this app, one user can hold only one pair of email and phone_number
- In this app, username is the same with email (in User model)
- Users can be logged-in with username or phone_number


# Custom Commands

- `python manage.py load_countries_states`
  - Loads countries and states data by parsing a JSON from web.
  - You can inspect the [`load_countries_states.py`](src/apps/management/management/commands/load_countries_states.py) file.

# Postman

You can easily import [Postman collection](postman/endpoints-collection.json) into Postman and test the project.