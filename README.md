# 04Academy
 04Academy Task for Ahmed Ragab

## API Endpoints Documentation:
---------------------------
## Step 2: Educational Level URLs
- Endpoint for adding an educational level: POST /EducationalLevelOp/add/ {"name": "Test Educational Level"}
- Endpoint for editing an educational level by ID: PUT /EducationalLevelOp/edit/1/ {"name": "Updated Educational Level"}
- Endpoint for deleting an educational level by ID: DELETE /EducationalLevelOp/delete/1/
- Endpoint for getting an educational level by ID: GET /GetEducationalLevelById/1/
- Endpoint for getting a list of educational levels: GET /GetEducationalLevelList/
- Endpoint for paginated list of educational levels: POST /EducationalLevelList/ {"pageNum": 2, "pageLen": 2}

## Class Level URLs
- Add, edit, delete, get by ID, and list URLs similar to Educational Level

## Curriculum URLs
- Add, edit, delete, get by ID, and list URLs similar to Educational Level

## Step 3: Subject URLs
- Add, edit, delete, get by ID, and list URLs similar to Educational Level

## Step 4, 5, 6: Other URLs (Session Frequency, Session Duration, Subscription Plan, etc.)
- Add, edit, delete, get by ID, and list URLs similar to Educational Level

## Final Step: Student Application URLs
1. Add Student Application
   - Endpoint: POST 'http://localhost:8000/StudentApplicationOp/add/'
   - Payload:
     ```json
     {
         "first_name": "John",
         "last_name": "Doe",
         "age": 25,
         "gender": "ذكر",
         "nationality": "الإمارات",
         "whatsapp_number": "123456789",
         "email": "john.doe@example.com",
         "difficulties": false,
         "educational_level": 1,
         "class_level": 2,
         "curriculum": 1,
         "subjects": [1, 2],
         "student_count": 1,
         "goals": [1, 2],
         "suitable_day": [2, 1],
         "time_period": "صباحي",
         "suitable_timing": 1,
         "session_frequency": 1,
         "session_duration": 2,
         "subscription_plan": 1,
         "card_number": "1234567890123456",
         "security_code": "123",
         "expiration_date": "12/25",
         "card_name": "John Doe"
     }
     ```
   - Response:
     ```json
     {
         "data": {
             "id": 7,
             "first_name": "John",
             "last_name": "Doe",
             "age": 25,
             "gender": "ذكر",
             "nationality": "الإمارات",
             "whatsapp_number": "123456789",
             "email": "john.doe@example.com",
             "difficulties": false,
             "notes": null,
             "time_period": "صباحي",
             "card_number": "1234567890123456",
             "security_code": "123",
             "expiration_date": "12/25",
             "card_name": "John Doe",
             "educational_level": 1,
             "class_level": 2,
             "curriculum": 1,
             "student_count": 1,
             "suitable_timing": 1,
             "session_frequency": 1,
             "session_duration": 2,
             "subscription_plan": 1,
             "subjects": [1, 2],
             "goals": [1, 2],
             "suitable_day": [1, 2]
         }
     }
   - Status Code:
     - Success: 201 Created
     - Failed: 406 Not Acceptable

2. Edit Student Application
   - Endpoint: PUT 'http://localhost:8000/StudentApplicationOp/edit/1/'
   - Payload: Same as Add Student Application
   - Response: Same as Add Student Application
   - Status Code:
     - Success: 200 OK
     - Failed: 406 Not Acceptable

3. Delete Student Application
   - Endpoint: DELETE 'http://localhost:8000/StudentApplicationOp/delete/1/'
   - Response:
     ```json
     {
         "data": "Delete successful"
     }
     ```
   - Status Code:
     - Success: 200 OK

4. Get Student Application by ID
   - Endpoint: GET 'http://localhost:8000/GetStudentApplicationGetById/1/'
   - Response: Same as Add Student Application
   - Status Code:
     - Success: 200 OK

5. Get List of Student Applications
   - Endpoint: GET 'http://localhost:8000/GetStudentApplicationList/'
   - Response: List of student applications (See example response)
   - Status Code:
     - Success: 200 OK

6. Paginated List of Student Applications
   - Endpoint: POST 'http://localhost:8000/StudentApplicationList/'
   - Payload:
     ```json
     {
         "pageNum": 5,
         "pageLen": 2
     }
     ```
   - Response: Paginated list of student applications (See example response)
   - Status Code:
     - Success: 200 OK

## Setup Instructions:
## Note: You can activate virtualenv before make project steps

## virtualenv Steps:
1. **Create a Virtual Environment:** 
     'virtualenv env'

2. **Activate the Virtual Environment:** 
     - On Windows: 'env\Scripts\activate'
     - On macOS and Linux: 'source env/bin/activate'

## Run project steps:
1. Install required packages: 'pip install -r requirements.txt'.
2. Apply database migrations: 'python manage.py makemigrations' then 'python manage.py migrate'.
3. Make admin user: 'python manage.py createsuperuser' .
4. make superuser with username: 'admin', password: 'admin' as example.
5. Run tests: 'python manage.py test setup.tests'.
6. Run the development server: 'python manage.py runserver'.
7. Access the API endpoints using the provided URLs and perform CRUD operations.

## Notes ##
- UnitTest is made only for one model and his URLs, and the other models have the same approach.
- CRUD form is also made for one model only (EducationalLevel), and the other models have the same approach.
- All URLs are available if you want to view it send me Gmail to allow it for you.

## Steps To make requests in EducationalLevel form:
1. Open 'login.html' file.
2. Enter username and password of the superuser you create to login.
3. Copy the token which is printed in the html page.
4. Paste it in line 51 of 'EducationalLevel.html' file instead of the exist token.
5. Now, you can add, edit, and delete EducationalLevel.

## You can enter the other models data using admin panel page ('http://localhost:8000/admin/') then login with superuser

## After add all the data, now you can register for student using 'index.html' file
