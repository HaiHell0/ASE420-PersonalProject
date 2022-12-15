from adapter import Adapter
import unittest
class Test(unittest.TestCase):
    testAdapter = Adapter()
    def testVerifyDate(self):
        self.assertTrue(self.testAdapter.verifyDate("today"))
        self.assertTrue(self.testAdapter.verifyDate("toDaY"))
        self.assertTrue(self.testAdapter.verifyDate("2000/1/1"))
        self.assertFalse(self.testAdapter.verifyDate("asdfasdf"))
        self.assertFalse(self.testAdapter.validateDateValue("2000/1/1"))
    def testVerifyTime(self):
        self.assertTrue(self.testAdapter.verifyTime("10:40"))
        self.assertTrue(self.testAdapter.verifyTime("10:40AM"))
        self.assertFalse(self.testAdapter.verifyTime("24:40AM"))
        self.assertFalse(self.testAdapter.verifyTime("24:40PM"))
        self.assertFalse(self.testAdapter.verifyTime("24:40"))
        self.assertTrue(self.testAdapter.verifyTime("10:40PM"))
        self.assertFalse(self.testAdapter.verifyTime("10:40PMasfasdf"))
        self.assertFalse(self.testAdapter.verifyTime("cc:40PM"))
        self.assertFalse(self.testAdapter.verifyTime("40:ccPM"))
    def testValidate(self):
        self.assertFalse(self.testAdapter.validateDateValue("2000/1/1"))
        self.assertTrue(self.testAdapter.validateDateValue("2200/1/1"))
        self.assertFalse(self.testAdapter.validateTo("10:40","10:40"))
        self.assertTrue(self.testAdapter.validateTo("10:40","10:41"))
        self.assertTrue(self.testAdapter.validateTo("10:40AM","10:40PM"))
    def testInterpret(self):
        self.assertEqual(self.testAdapter.interpretDate("2000/1/1"),"2000/1/1")
        self.assertEqual(self.testAdapter.interpretTime("10:40"),"10:40")
        self.assertEqual(self.testAdapter.interpretTime("10:40AM"),"10:40")
        self.assertEqual(self.testAdapter.interpretTime("10:40PM"),"22:40")
if __name__ == '__main__':
    unittest.main()

