from sqlite import DataService
from todoitem import Todoitem

import unittest


class AdvancedTestSuite(unittest.TestCase):
    testDataService = DataService()
    def testCheckTableExists(self):
        self.assertEqual(self.testDataService._checkTableExists("No table"),False)
        self.assertEqual(self.testDataService._checkTableExists("todolist"),True)
    def testToToDoArray(self):
        temp = self.testDataService._toToDoArray([('ID','test1','test','test','test',0),('ID','test2','test','test','test',1)])
        self.assertEqual(temp[0].DATE , 'test1')
        self.assertEqual(temp[1].DATE , 'test2')
    def testAddToDoItem(self):
        self.testDataService.addToDoItem(Todoitem('Date123','test','test','test','test'))
        result = self.testDataService.getAllItems()
        self.assertEqual(result[-1].DATE , 'Date123')
        self.testDataService.deleteToDoItem(result[-1].id)
    def testDeleteToDoItem(self):
        self.testDataService.addToDoItem(Todoitem('Date123','test','test','test','test'))
        result = self.testDataService.getAllItems()
        id = result[-1].id
        self.testDataService.deleteToDoItem(id)
        self.assertFalse(self.testDataService.deleteToDoItem(id))
    def testGetters(self):
        self.testDataService.addToDoItem(Todoitem('Date123','test','test','test123','unique'))
        result = self.testDataService.getByDate("Date123")
        self.assertEqual(result[0].TAG,"unique")
        result = self.testDataService.getByTag("unique")
        self.assertEqual(result[0].DATE,"Date123")
        result = self.testDataService.getByTag("unique")
        self.assertEqual(result[0].DATE,"Date123")
        result = self.testDataService.getByTask("test123")
        self.assertEqual(result[0].DATE,"Date123")
        self.testDataService.deleteToDoItem(result[0].id)
        self.assertFalse(self.testDataService.deleteToDoItem(result[0].id))
    



if __name__ == '__main__':
    unittest.main()

