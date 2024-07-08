### Python Assignment
To set up a FastAPI project and create an endpoint with request and response validation using Pydantic models. Implement the logic to perform addition on input lists of integers using Python's multiprocessing pool, with appropriate error handling and logging for debugging and monitoring activities. Write unit tests for all edge cases and scenarios.



#### Directory structure : 

![image](https://github.com/rohanksingh/Python-Assignment/assets/31317534/9311fb89-8b26-4478-b8a5-3f882858d4f5)


app/main.py --> file initializes the FASTAPI app and includes the routing.

app/models/addition_request.py and addition_response.py --> Here define the Pydantic models.

app/controllers/addition_controller.py --> Here business logic performed.

app/views/addition_view.py --> Here deine the routes and call the controller logic.

app/utils/multiprocess_addition.py --> Here define the utility functions using multiprocessing. (test cases with wide scenarios covered)

app/tests/test_addition.py --> Perform unit test for the multiprocessing logic.

app/config.py --> For centralized place to manage configuration settings for application.

requirements.txt --> List of all dependencies.

run.py --> This file is th eentry point to run the FASTAPI application.

.env  --> This is to define environment-specific settings, can be used for different configurations for development, testing, and production environments without changing.


#### For Running the application

1. Install the dependencies 
pip install -r requirements.txt

2. Run the application
   python run.py

3. Run the tests
   pytest

![image](https://github.com/rohanksingh/Python-Assignment/assets/31317534/5d463ea6-eab0-4bc4-ba6a-0a8de02eaddb)

 
