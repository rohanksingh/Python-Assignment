### Python Assignment
To set up a FastAPI project and create an endpoint with request and response validation using Pydantic models. Implement the logic to perform addition on input lists of integers using Python's multiprocessing pool, with appropriate error handling and logging for debugging and monitoring activities. Write unit tests for all edge cases and scenarios.



#### Directory structure : 

![image](https://github.com/rohanksingh/Python-Assignment/assets/31317534/91b18d53-13e9-40cb-bf4e-5674cb125764)

app/main.py --> file inittializes the FASTAPI app and includes the routing.

app/models/addition.py --> Here define the Pydantic models.

app/controllers/addition_controller.py --> Here business logic performed.

app/views/addition_view.py --> Here deine the routes and call the controller logic.

app/utils/multiprocess_addition.py --> Here define the utility functions using multiprocessing.

app/tests/test_multiprocess_addition.py --> Perform unit test for the multiprocessing logic.

run.py --> This file is th eentry point to run the FASTAPI application.

requirements.txt --> List of all depndencies.

#### For Running the application

1. Install the dependencies 
pip install -r requirements.txt

2. Run the application
   python run.py

3. Run the tests
curl -X POST "http://127.0.0.1:8000/additions/" -H "Content-Type: application/json" -d '{"batchid": "id0101", "payload": [[1,2], [3,4]]}'
or can use interactive documentation : http://127.0.0.1:8000/docs
 
