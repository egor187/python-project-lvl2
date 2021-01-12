from gendiff.generate_diff import generate_diff


class TestSecondProject:
    """ Create test_class. Pytest (like unittest) finds all func and methods
        which calls on test_* and run it in all finded *_test.py or
        test_*.py modules """

    def test_common_json_sim(self):
        assert generate_diff(
            './gendiff/tests/fixtures/file3.json',
            './gendiff/tests/fixtures/file4.json', formatter="stylish") \
            == open(
                './gendiff/tests/fixtures/result_for_test_json_stylish.txt',
                'r'
                    ).read()

    def test_common_yaml_sim(self):
        assert generate_diff(
            './gendiff/tests/fixtures/file3.yml',
            './gendiff/tests/fixtures/file4.yml', formatter="stylish") \
            == open(
                './gendiff/tests/fixtures/result_for_test_yaml_stylish.txt',
                'r'
                    ).read()

    def test_common_json_sim_raw(self):
        assert generate_diff(
            './gendiff/tests/fixtures/file3.json',
            './gendiff/tests/fixtures/file4.json', formatter="raw") \
            == open(
                './gendiff/tests/fixtures/result_for_test_json_raw.txt',
                'r'
                    ).read()

    def test_common_yaml_sim_raw(self):
        assert generate_diff(
            './gendiff/tests/fixtures/file3.yml',
            './gendiff/tests/fixtures/file4.yml', formatter="raw") \
            == open(
                './gendiff/tests/fixtures/result_for_test_yaml_raw.txt',
                'r'
                    ).read()

    def test_common_json_sim_plain(self):
        assert generate_diff(
            './gendiff/tests/fixtures/file3.json',
            './gendiff/tests/fixtures/file4.json', formatter="plain") \
            == open(
                './gendiff/tests/fixtures/result_for_test_json_plain.txt',
                'r'
                    ).read()

    def test_common_yaml_sim_plain(self):
        assert generate_diff(
            './gendiff/tests/fixtures/file3.yml',
            './gendiff/tests/fixtures/file4.yml', formatter="plain") \
            == open(
                './gendiff/tests/fixtures/result_for_test_yaml_plain.txt',
                'r'
                    ).read()

    def test_common_json_sim_json(self):
        assert generate_diff(
            './gendiff/tests/fixtures/file3.json',
            './gendiff/tests/fixtures/file4.json', formatter="json") \
            == open(
                './gendiff/tests/fixtures/result_for_test_json_json.txt',
                'r'
                    ).read()

    def test_common_yaml_sim_json(self):
        assert generate_diff(
            './gendiff/tests/fixtures/file3.yml',
            './gendiff/tests/fixtures/file4.yml', formatter="json") \
            == open(
                './gendiff/tests/fixtures/result_for_test_yaml_json.txt',
                'r'
                    ).read()
