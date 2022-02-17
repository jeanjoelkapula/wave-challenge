# Wave Challenge (Payroll Api)
This project is a simple Payroll API as a challenge set by Wave for their Full-stack Developer applicants. Click [Wave Challenge](https://github.com/wvchallenges/se-challenge-payroll) to view the original channel repository.

# Features
The application has 2 endpoints:
* **Report Upload**: this endpoint allows the submission of a time report csv file through PUT request. Each report may only be submitted once.
* **Payroll Report**: this endpoint returns a payroll report based on all of the data across all of the uploaded time reports, for all time. The report is sorted first by employee id and then by pay period start. 

    For each month of a reported year, the pay amount for each employee is reported over two periods (1 to 15 and 16 to month end).  
# Tech Stack
* Python (Django / Django Rest Framework)

# Requirements
* asgiref==3.5.0
* Django==4.0.2
* djangorestframework==3.13.1
* greenlet==1.1.2
* importlib-metadata==4.11.1
* Markdown==3.3.6
* pytz==2021.3
* SQLAlchemy==1.4.31
* sqlparse==0.4.2
* tzdata==2021.5
* zipp==3.7.0

# Installation
 1. Clone repository
       ```
		 git clone https://github.com/jeanjoelkapula/wave-challenge.git
	 ```

2. Install Requirements

    Virtual environment is recommended. 
     ```
			 pip install -r requirements.txt
	 ```
# Running your local server

 1. Ensure you have made all migrations
	```
	 python manage.py migrate
	```
1. Start the server
	```
	 python manage.py runserver
	```

# Routes
* The payroll report endpoint is at '/'

    Below is a sample report:
    ```
        {
          "payrollReport": {
            "employeeReports": [
              {
                "employeeId": "1",
                "payPeriod": {
                  "startDate": "2023-01-01",
                  "endDate": "2023-01-15"
                },
                "amountPaid": "$300.00"
              },
              {
                "employeeId": "1",
                "payPeriod": {
                  "startDate": "2023-01-16",
                  "endDate": "2023-01-31"
                },
                "amountPaid": "$80.00"
              },
              {
                "employeeId": "2",
                "payPeriod": {
                  "startDate": "2023-01-16",
                  "endDate": "2023-01-31"
                },
                "amountPaid": "$90.00"
              }
            ]
          }
        }
    ```
   
   * The file upload route for the time report is at '/upload'.
   
    The API is browsable. You may upload your file through the provided interface
    
    ![image](https://user-images.githubusercontent.com/44115772/154522237-10b56df8-fc6f-4e65-b3b6-4e150b526486.png)