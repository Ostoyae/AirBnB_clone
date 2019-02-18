#!/usr/bin/python3
"""
Unittests for the
FileStorage class
file engine.
"""
from models.engine.file_storage import FileStorage
from models.city import City
from models.review import Review
import unittest
import filecmp
import json
import pep8
import sys
import os

class TestFileStorage(unittest.TestCase):

    @classmethod
    def setUp(cls):
        """
        Creates an instance and
        checks if it is a class
        or not.
        """

        cls.fs = FileStorage()
        cls.fs.place_id = "San Francisco"
        cls.fd.user_id = "Jack Dorsey"
        cls.fs.text = "tweet"

    @classmethod
    def tearDown(self):
        """
        Cleans up and removes
        JSON file after done.
        """

        del fs

    def tearDown(self):
        """
        Removes JSON file used.
        """

        try:
            os.remove("file.json")

        except: pass

    def check_documentation(self):
        """
        Check that documentation exists
        for all classes and methods in the
        FileStorage.
        """

        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(all.__doc__)
        self.assertIsNotNone(new.__doc__)
        self.assertIsNotNone(save.__doc__)
        self.assertIsNotNone(reload.__doc__)

    def test_base_pep8(self):
        """
        Tests Base for PEP8 errors.
        """

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files([
            "tests/test_models/test_file_engine.py"])
        self.assertEqual(result.total_errors, 0, "PEP8 failure...")
        result = pep8style.check_files(["models/engine/file_storage/file_storage.py"])
        self.assertEqual(result.total_errors, 0, "PEP8 failure...")

    def test_methods_exist(self):
        """
        Test to see if methods are
        created and correct.
        """

        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_instance_created(self):
        """
        Test that instance
        and attributs created.
        """

        
        fs = FileStorage()
        self.assertIsInstance(fs, FileStorage)

    def test_all(self):
        """
        Test the `all` method fills
        values into the `__objects` dict.
        """

        fs = FileStorage()
        dic = fs.all()
        self.assertNotNone(dic)
        self.assertTrue(dic, self._FileStorage__objects)

    def test_new(self):
        """
        Test the `new` method writes
        clssname.id to `__objects`.
        """

        fs = FileStorage()
        dic = fs.all()
        subcls = City()
        subcls.state_id = "CA"
        subcls.name = "San Francisco"
        key = subcls.__class____name__ + "." + subcls.state_id
        self.assertTrue(type(key), str)
        self.assertIsNotNone(dic[key])

    def test_save(self):
        """
        Test that `save` method wrote
        `__objects` to the file.
        """

        fs = FileStorage()
        fp = self._FileStorage__file_path
        existance = os.path.isfile(self._FileStorage__file_path)
        self.assertEqual(existance, True)
        self.assertIsNotNone(fp)

    def test_reload(self):
        """
        Test that `reload` method 
        created an instance from 
        the file.
        """

        fs = FileStorage()
        fp = self._FileStorage__file_path
        existance = os.path.isfile(fp)
        self.assertEqual(existance, True)

        with open(fp, encoding="utf-8") as f:
            f.write("{}")

        with open(fp, encoding="utf-8") as f:
            for line in f:
                self.assertEqual(line, "{}")
