#!/usr/bin/python3
"""
Contains the TestFileStorageDocs classes
"""

from datetime import datetime
import inspect
import models
from models.engine import file_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
FileStorage = file_storage.FileStorage
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class TestFileStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of FileStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.fs_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pep8_conformance_file_storage(self):
        """Test that models/engine/file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_file_storage(self):
        """Test tests/test_models/test_file_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_file_storage.py'])

    def test_file_storage_module_docstring(self):
        """Test for the file_storage.py module docstring"""
        self.assertIsNot(file_storage.__doc__, None,
                         "file_storage.py needs a docstring")
        self.assertTrue(len(file_storage.__doc__) >= 1,
                        "file_storage.py needs a docstring")

    def test_file_storage_class_docstring(self):
        """Test for the FileStorage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         "FileStorage class needs a docstring")
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        "FileStorage class needs a docstring")

    def test_fs_func_docstrings(self):
        """Test for the presence of docstrings in FileStorage methods"""
        for func in self.fs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))

    def test_count_method_docstring(self):
        """Test for the presence of docstring in FileStorage.count() method"""
        self.assertIsNot(FileStorage.count.__doc__, None,
                         "count method needs a docstring")
        self.assertTrue(len(FileStorage.count.__doc__) >= 1,
                        "count method needs a docstring")

    def test_get_method_docstring(self):
        """Test for the presence of docstring in FileStorage.get() method"""
        self.assertIsNot(FileStorage.get.__doc__, None,
                         "get method needs a docstring")
        self.assertTrue(len(FileStorage.get.__doc__) >= 1,
                        "get method needs a docstring")

    def test_count_method(self):
        """Test the FileStorage.count() method"""
        state1 = State(name="California")
        state2 = State(name="New York")
        file_storage = FileStorage()
        file_storage.new(state1)
        file_storage.new(state2)
        file_storage.save()

        all_objects_count = file_storage.count()

        state_count = file_storage.count(State)

        non_existent_count = file_storage.count(Review)

    def test_get_method(self):
        """Test the FileStorage.get() method"""
        state1 = State(name="California")
        state2 = State(name="New York")
        file_storage = FileStorage()
        file_storage.new(state1)
        file_storage.new(state2)
        file_storage.save()

        state1_id = state1.id
        retrieved_state = file_storage.get(State, state1_id)
        self.assertEqual(retrieved_state, state1)

        non_existent_id = "non_existent_id"
        non_existent_state = file_storage.get(State, non_existent_id)
        self.assertIsNone(non_existent_state)
