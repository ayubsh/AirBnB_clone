import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ base model test """
    def SetUp(self):
        self.base = BaseModel()

    def test_attributes(self):
        """None attribute."""
        object_test = BaseModel(None)
        self.assertTrue(hasattr(object_test, "id"))
        self.assertTrue(hasattr(object_test, "created_at"))
        self.assertTrue(hasattr(object_test, "updated_at"))

    def test_kwargs(self):
        """ check id with data """
        d = {'a': 1}

        o = BaseModel(**d)
        self.assertTrue(hasattr(o, 'id'))
        self.assertTrue(hasattr(o, 'created_at'))
        self.assertTrue(hasattr(o, 'updated_at'))
        self.assertTrue(hasattr(o, 'a'))


    def test_to_dict(self):
        """ check dict """
        object_test = BaseModel(score=300)
        n_dict = object_test.to_dict()

        self.assertEqual(n_dict['id'], object_test.id)
        self.assertEqual(n_dict['score'], 300)
        self.assertEqual(n_dict['__class__'], 'BaseModel')
        self.assertEqual(n_dict['created_at'], object_test.created_at.isoformat())
        self.assertEqual(n_dict['updated_at'], object_test.updated_at.isoformat())

        self.assertEqual(type(n_dict['created_at']), str)
        self.assertEqual(type(n_dict['created_at']), str)

    def test_str_representation(self):
        """ Test string  """
        b = BaseModel()
        self.assertEqual(str(b),
                         "[BaseModel] ({}) {}".format(b.id, b.__dict__))



if __name__ == "__main__":
    unittest.main()
