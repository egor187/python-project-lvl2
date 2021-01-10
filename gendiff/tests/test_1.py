from gendiff.generate_diff import generate_diff
from gendiff.yaml_diff import yaml_diff


class TestSecondProject:
    """ Create test_class. Pytest (like unittest) finds all func and methods
        which calls on test_* and run it in all finded *_test.py or
        test_*.py modules """
    def test_json(self):
        assert generate_diff(
            './gendiff/tests/fixtures/file1.json',
            './gendiff/tests/fixtures/file2.json') \
            == open('./gendiff/tests/fixtures/test_json_res.txt', 'r'
                    ).read()

    def test_yml(self):
        assert yaml_diff(
            './gendiff/tests/fixtures/file1.yml',
            './gendiff/tests/fixtures/file2.yml') \
            == open('./gendiff/tests/fixtures/test_yaml_res.txt', 'r'
                    ).read()
