# MoneyMan

## Setup

Install dependencies:
```
poetry install
```

Create database and schema:
```
poetry run python manage.py migrate 

```

To create fake expenses:
```
poetry run python manage.py create_fake_expenses 250 
```

To create a superuser:
```
poetry run python manage.py createsuperuser 
```
## Running

To run server:
```
poetry run python manage.py runserver 
```

Enjoy: http://localhost:8000/ 




