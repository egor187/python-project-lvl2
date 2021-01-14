from gendiff.generate_diff import generate_diff


class TestSecondProject:
    """ Create test_class. Pytest (like unittest) finds all func and methods
        which calls on test_* and run it in all finded *_test.py or
        test_*.py modules """

    def test_flat_json_stylish_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example.json',
            './gendiff/tests/fixtures/example2.json',
            formatter="stylish"
        ) == open(
            './gendiff/tests/fixtures/example_json_diff.txt', 'r').read()

    def test_flat_json_stylish_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example.json',
            './gendiff/tests/fixtures/example.json',
            formatter="stylish"
        ) == open(
            './gendiff/tests/fixtures/example_json_equal.txt', 'r').read()

    def test_flat_yaml_stylish_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example.yml',
            './gendiff/tests/fixtures/example2.yml',
            formatter="stylish"
        ) == open(
            './gendiff/tests/fixtures/example_yaml_diff.txt', 'r').read()

    def test_flat_yaml_stylish_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example2.yml',
            './gendiff/tests/fixtures/example2.yml',
            formatter="stylish"
        ) == open(
            './gendiff/tests/fixtures/example_yaml_equal.txt', 'r').read()

    def test_recurs_json_stylish_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.json',
            './gendiff/tests/fixtures/example2_recurs.json',
            formatter="stylish") \
            == open(
                './gendiff/tests/fixtures/example_recurs_json_diff.txt',
                'r'
        ).read()

    def test_recurs_yaml_stylish_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.yml',
            './gendiff/tests/fixtures/example2_recurs.yml',
            formatter="stylish") \
            == open(
                './gendiff/tests/fixtures/example_recurs_yaml_diff.txt',
                'r'
        ).read()

    def test_recurs_json_stylish_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.json',
            './gendiff/tests/fixtures/example_recurs.json',
            formatter="stylish") \
            == open(
                './gendiff/tests/fixtures/example_recurs_json_equal.txt',
                'r'
        ).read()

    def test_recurs_yaml_stylish_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.yml',
            './gendiff/tests/fixtures/example_recurs.yml',
            formatter="stylish") \
            == open(
                './gendiff/tests/fixtures/example_recurs_yaml_equal.txt',
                'r'
        ).read()

    def test_recurs_json_plain_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.json',
            './gendiff/tests/fixtures/example2_recurs.json',
            formatter="plain") \
            == open(
                './gendiff/tests/fixtures/example_recurs_json_plain.txt',
                'r'
        ).read()

    def test_recurs_json_plain_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.json',
            './gendiff/tests/fixtures/example_recurs.json',
            formatter="plain") \
            == ''

    def test_recurs_yaml_plain_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.yml',
            './gendiff/tests/fixtures/example2_recurs.yml',
            formatter="plain") \
            == open(
                './gendiff/tests/fixtures/example_recurs_yaml_plain.txt',
                'r'
        ).read()

    def test_recurs_yaml_plain_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.yml',
            './gendiff/tests/fixtures/example_recurs.yml',
            formatter="plain") \
            == ''

    def test_recurs_json_json_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.json',
            './gendiff/tests/fixtures/example2_recurs.json',
            formatter="json") \
            == open(
                './gendiff/tests/fixtures/example_recurs_json_json_diff.txt',
                'r'
        ).read()

    def test_recurs_json_json_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.json',
            './gendiff/tests/fixtures/example_recurs.json',
            formatter="json") \
            == open(
                './gendiff/tests/fixtures/example_recurs_json_json_equal.txt',
                'r'
        ).read()

    def test_recurs_yaml_json_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.yml',
            './gendiff/tests/fixtures/example2_recurs.yml',
            formatter="json") \
            == open(
                './gendiff/tests/fixtures/example_recurs_yaml_json_diff.txt',
                'r'
        ).read()

    def test_recurs_yaml_json_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/example_recurs.yml',
            './gendiff/tests/fixtures/example_recurs.yml',
            formatter="json") \
            == open(
                './gendiff/tests/fixtures/example_recurs_yaml_json_equal.txt',
                'r'
        ).read()

#    def test_recurs_json_raw_diff(self):

#    def test_recurs_json_raw_diff(self):
#        assert generate_diff(
#            './gendiff/tests/fixtures/example_recurs.json',
#            './gendiff/tests/fixtures/example2_recurs.json',
#           formatter="raw") \
#            == open(
#                './gendiff/tests/fixtures/example_recurs_json_raw.txt',
#                'r'
#                    ).read()
#
#    def test_recurs_json_raw_equal(self):
#        assert generate_diff(
#            './gendiff/tests/fixtures/example_recurs.json',
#            './gendiff/tests/fixtures/example_recurs.json', formatter="raw") \
#            == open(
#                './gendiff/tests/fixtures/example_recurs_json_raw_equal.txt',
#                'r'
#                    ).read()
#
#    def test_recurs_yaml_raw_diff(self):
#        assert generate_diff(
#            './gendiff/tests/fixtures/example_recurs.yml',
#            './gendiff/tests/fixtures/example2_recurs.yml', formatter="raw") \
#            == open(
#                './gendiff/tests/fixtures/example_recurs_yaml_raw.txt',
#                'r'
#                    ).read()
#
#    def test_recurs_yaml_raw_equal(self):
#        assert generate_diff(
#            './gendiff/tests/fixtures/example_recurs.yml',
#            './gendiff/tests/fixtures/example_recurs.yml', formatter="raw") \
#            == open(
#                './gendiff/tests/fixtures/example_recurs_yaml_raw_equal.txt',
#                'r'
#                    ).read()
