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

## Comments

You can see more comments about this proyect in [Comments](Comments.md) or directly in the file.

