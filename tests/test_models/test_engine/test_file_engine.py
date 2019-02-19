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
    """
    Unitest for FileStorage class.
    """

    @classmethod
    def setUp(cls):
        """
        Creates an instance and
        checks if it is a class
        or not.
        """

        cls.usr = User()
        cls.usr.first_name = "Nunya"
        cls.usr.last_name = "Beezwax"
        cls.usr.email = "nyb@gmail.com"
        cls.storage = FileStorage()

    @classmethod
    def tearDown(self):
        """
        Cleans up and removes
        JSON file after done.
        """

        del cls.usr

    def tearDown(self):
        """
        Removes JSON file used.
        """

        try:
            os.remove("file.json")

        except:
            pass

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
            "models/engine/file_storage/file_storage.py"])
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
        dic = fstorage.all()
        self.assertIsNotNone(dic)
        self.assertEqual(type(dic), dict)
        self.assertIs(dic, fs._FileStorage__objects)

    def test_new(self):
        """
        Test the `new` method writes
        clssname.id to `__objects`.
        """

        fs = FileStorage()
        dic = fs.all()
        subcls = City()
        subcls.id = 94061
        subcls.name = "San Francisco"
        fs.new(subcls)
        key = subcls.__class__.__name__ + "." + subcls.state_id
        self.assertIsNotNone(dic[key])

    def test_reload(self):
        """
        Test that `reload` method
        created an instance from
        the file.
        """

        self.storage.save()
        directory = os.path.dirname(os.path.abspath("console.py"))
        fp = os.path.join(directory, "file.json")

        with open(fp, encoding="utf-8") as f:
            handler = f.readlines()

        try:
            os.remove(fp)
        except BaseException:
            pass

        self.storage.save()

        with open(fp, encoding="utf-8") as f:
            handler1 = f.readlines()
        self.assertEqual(handler, handler1)

        try:
            os.remove(pt)
        except BaseException:
            pass

        with open(fp, "w", encoding="utf-8") as w:
            w.write("{}")

        with open(fp, encoding="utf-8") as r:
            for line in r:
                self.assertEqual(line, "{}")

        self.assertIs(self.storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
