from fetchdata import Fetchdata
from distance import CalculateDistance
import unittest,json
from deletecontent import Delete
from unittest.mock import Mock
from dataPreparation import DataPreparation

class TestCustomer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass 

    @classmethod
    def tearDownClass(cls):
        pass
    
    
    def tearDown(self):
        pass 


    def test_distance(self):
        with open("C:\\Users\\Vishal\\Desktop\\workarea\\Intercom\\test2vs.json", "r") as read_file:
            data = json.load(read_file)
            data1 = CalculateDistance.distance(data)
        
        result1="file sucessfully created"
        
        # assert the result
        self.assertEqual(data1,result1)

    def test_delete(self):
        data2=Delete.deleteContent()
        
        result2="content successfully deleted"
        
        self.assertEqual(data2,result2)

    
        