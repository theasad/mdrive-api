# Screening Project

## Technology version:
| Name                        	| Version 	    |
|-----------------------------	|-------------- |
| Python                      	| 3.6.8      	|
| Django                      	| 2.2.2       	|
| Django-rest-framework 	    | 3.9.4       	|


# Backend(API) project setup process

## [Demo](https://mdrive-app.herokuapp.com)

1. Create Virtual environment usnig python3
    ```
    python3 -m virtualenv venv
    ```

2. Active virtual environment
    ```
    source venv/bin/active (Linux)
    ```
    ```
    venv\Scripts\activate (Windows)
    ```
3. Clone project repository 
    
    [Click here to clone](https://github.com/theasad/mdrive-api.git)

4. Goto backend(API) directory
    ```
    cd screening-project/backend
    ```
    
5. Install Requirements using pip
    ```
    pip install -r requirements.txt
    ```

6. Migrate database
    ```
    python manage.py migrate
    ```

7. Run Django server on port 8000
    ```
    python manage.py runserver 
    ```
    or

    ```
    python manage.py runserver  127.0.0.1:8000
    ```

***********************************
            <HappyCodding />
***********************************

