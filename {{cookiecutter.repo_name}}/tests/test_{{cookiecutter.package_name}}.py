"""
Example unit tests for {{cookiecutter.repo_name}} package
"""
import unittest
import {{cookiecutter.package_name}}

class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.message = 'Hello, world'

    def tearDown(self):
        pass

    def test_run(self):
        foo = {{cookiecutter.package_name}}.Example(self.message)
        self.assertEqual(foo.run(), self.message)

    def test_failure(self):
        self.assertRaises(TypeError, {{cookiecutter.package_name}}.{{cookiecutter.repo_name}})
        foo = {{cookiecutter.package_name}}.Example(self.message)
        self.assertRaises(RuntimeError, foo.run, True)

if __name__ == '__main__':
    unittest.main()
