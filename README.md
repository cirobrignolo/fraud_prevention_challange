# Fraud Prevention Challange

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    
2. Run the migration:
     ```bash
    python manage.py migrate
    ```

3. Create superuser:
     ```bash
    python manage.py createsuperuser
    ```

4. Run the application:
    ```bash
    python manage.py runserver
    ```
    
## API Endpoints

- `GET /api/fraud-check/<user_id>/`: Check information about fraud prevention.

## Tests

There are test for models, serializers and views. To run the test use the command:

    python manage.py test

## Steps to run code

1. First, you need to access the admin panel through http://127.0.0.1:8000/admin/ or the corresponding associated IP, and log in using the superuser created earlier.

2. Then, create at least one user and the necessary payments as needed.

3. Finally, through any means to make API calls, use the URL http://127.0.0.1:8000/api/fraud-check/:user_id/ or the corresponding associated IP along with the ID of the created user to obtain the response from the call.


## Comments

You can see more comments about this proyect in [Comments](Comments.md) or directly in the file.

