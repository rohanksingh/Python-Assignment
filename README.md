### Python Assignment
To set up a FastAPI project and create an endpoint with request and response validation using Pydantic models. Implement the logic to perform addition on input lists of integers using Python's multiprocessing pool, with appropriate error handling and logging for debugging and monitoring activities. Write unit tests for all edge cases and scenarios.



#### Directory structure : 

![image](https://github.com/rohanksingh/Python-Assignment/assets/31317534/9311fb89-8b26-4478-b8a5-3f882858d4f5)


app/main.py --> file inittializes the FASTAPI app and includes the routing.

app/models/addition_request.py and addition_response.py --> Here define the Pydantic models.

app/controllers/addition_controller.py --> Here business logic performed.

app/views/addition_view.py --> Here deine the routes and call the controller logic.

app/utils/multiprocess_addition.py --> Here define the utility functions using multiprocessing.

app/tests/test_addition.py --> Perform unit test for the multiprocessing logic.

app/config.py --> 

requirements.txt --> List of all depndencies.

run.py --> This file is th eentry point to run the FASTAPI application.


#### For Running the application

1. Install the dependencies 
pip install -r requirements.txt

2. Run the application
   python run.py

3. Run the tests
curl -X POST "http://127.0.0.1:8000/additions/" -H "Content-Type: application/json" -d '{"batchid": "id0101", "payload": [[1,2], [3,4]]}'
or can use interactive documentation : http://127.0.0.1:8000/docs
 
