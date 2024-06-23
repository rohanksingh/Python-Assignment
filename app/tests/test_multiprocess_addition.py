import unittest
from app.utils.multiprocess_addition import add_lists, process_list_additions
from app.models.addition import AdditionRequest , AdditionResponse
from app.controllers.addition_controller import create_addition_logic
from datetime import datetime

class TestMultiprocessAddition(unittest.TestCase):

    def test_add_lists(self):
        self.assertEqual(add_lists([1,2,3,4]),10)
    
    def test_process_list_additions(self):
        list_pairs = [
            [1,2,3],
            [4,5,6]
        ]

        excepted = [
            6,
            15
        ]

        self.assertEqual(process_list_additions(list_pairs, 2), expected)

    def test_create_addition_logic(self):
        request= AdditionRequest(batchid= "id0101", payload=[[1,2],[3,4]])
        response= create_addition_logic(request)
        self.assertEqual(response.batchid, "id0101")
        self.assertEqual(response.response, [3,7])
        self.assertEqual(response.status, "complete")
        self.assertEqual(isinstance(response.started_at, datetime))
        self.assertTrue(isinstance(response.completed_at,datetime))


if __name__=="__main__":
    unittest.main()

    




