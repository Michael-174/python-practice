from practical import DictTest as D
import unittest
#必须要用test开头写function
class TestDictTest(unittest.TestCase):

    def setUp(self): #在每个测试之前跑
        print("Im setting up! U^U")

    def tearDown(self): #在每个测试之后跑，像扫地机
        print("Im tearing down! UwU")

    def test_dict_test(self):
        d = D.Dict(a = 1, b = "test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = D.Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")

    def test_attr(self):
        d = D.Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    def test_keyError(self):
        d = D.Dict()
        with self.assertRaises(KeyError): #接下来这一小块代码，必须抛出 KeyError，否则测试失败。
            value = d['empty']

    def test_attrError(self):
        d = D.Dict()
        with self.assertRaises(AttributeError): ##接下来这一小块代码，必须抛出AttributeError，否则测试失败。
            value = d.empty

if __name__ == '__main__':
    unittest.main()
