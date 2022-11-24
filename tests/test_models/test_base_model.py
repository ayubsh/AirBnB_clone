import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ base model test """
    def SetUp(self):
        self.base = BaseModel()

    def test_attributes(self):
        print(self.base)
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))

if __name__ == "__main__":
    unittest.main()
