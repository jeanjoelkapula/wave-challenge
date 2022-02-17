# Table of contents

- [Wave Challenge (Payroll Api)](#wave-challenge-payroll-api)
- [Features](#features)
- [Assumptions](#assumptions)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running your local server](#running-your-local-server)
- [Routes](#routes)

# Wave Challenge (Payroll Api)
This project is a simple Payroll API as a challenge set by Wave for their Full-stack Developer applicants. Click [Wave Challenge](https://github.com/wvchallenges/se-challenge-payroll) to view the original channel repository.

# Features
The application has 2 endpoints:
* **Report Upload**: this endpoint allows the submission of a time report csv file through PUT request. Each report may only be submitted once.
* **Payroll Report**: this endpoint returns a payroll report based on all of the data across all of the uploaded time reports, for all time. The report is sorted first by employee id and then by pay period start. 

    For each month of a reported year, the pay amount for each employee is reported over two periods (1 to 15 and 16 to month end).  
    
# Assumptions
It has been assumed that employees and job groups would be already created in the database. Therefore, records in those table would need to be created beforehand.

You will need to run the insert_records function provided in the util file of the payroll app in your python shell to create records to get you started. Those records are created based on the information provided in the challenge and the sample csv file. 


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

2. Requirements

    Virtual environment is recommended. 
     ```
	 pip install -r requirements.txt
	 ```
# Running your local server

 1. Ensure you have made all migrations
	```
	 python manage.py migrate
	```
3. Run the insert_records function
    from the root of the project directory
    ```
    >>> python manage.py shell
    >>> from payroll.util import insert_records
    >>> insert_records()  
    >>> exit()
	```

   
3. Start the server
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