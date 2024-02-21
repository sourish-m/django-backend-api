# Codemonk-api-backend
Codemonk is a Django-based project that provides APIs for text processing and user registration.



# Key Components
- api/ - This directory contains the main application logic.
- api/models.py - This file contains the data models for the application.
- api/serializers.py - This file contains the serializers for the data models.
- api/views.py - This file contains the views for the application.
- codemonk/settings.py - This file contains the settings for the Django project.
- codemonk/urls.py - This file contains the URL configurations for the project.
- manage.py - This is the command-line utility for administrative tasks.

# API Endpoints
- /split/ - This endpoint accepts a POST request with a text and splits it into paragraphs and words.
- /search/ - This endpoint accepts a GET request with a word and returns paragraphs containing that word, sorted by word count.
- /register/ - This endpoint accepts a POST request with user details (username, password, email, and optional date of birth) and registers a new user.

# Usage:

1. http://127.0.0.1:8000/register/

    Send a post request (using POSTMAN or curl) to the above url with these fields in the body as shown below:

    <screenshot>

    A token will be returned:

    <screenshot>