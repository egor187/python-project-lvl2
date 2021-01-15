from gendiff.gendiff import generate_diff


class TestSecondProject:
    """ Create test_class. Pytest (like unittest) finds all func and methods
        which calls on test_* and run it in all finded *_test.py or
        test_*.py modules """

    def test_flat_json_stylish_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/flat.json',
            './gendiff/tests/fixtures/flat2.json',
            formatter="stylish"
        ) == open(
                './gendiff/tests/fixtures/result_flat_json_diff.txt',
                'r').read().rstrip()

    def test_flat_json_stylish_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/flat.json',
            './gendiff/tests/fixtures/flat.json',
            formatter="stylish"
        ) == open(
            './gendiff/tests/fixtures/result_flat_json_equal.txt',
            'r').read().rstrip()

    def test_flat_yaml_stylish_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/flat.yml',
            './gendiff/tests/fixtures/flat2.yml',
            formatter="stylish"
        ) == open(
            './gendiff/tests/fixtures/result_flat_yaml_diff.txt',
            'r').read().rstrip()

    def test_flat_yaml_stylish_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/flat2.yml',
            './gendiff/tests/fixtures/flat2.yml',
            formatter="stylish"
        ) == open(
            './gendiff/tests/fixtures/result_flat_yaml_equal.txt',
            'r').read().rstrip()

    def test_recurs_json_stylish_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/recursion.json',
            './gendiff/tests/fixtures/recursion2.json',
            formatter="stylish") \
            == open(
                './gendiff/tests/fixtures/result_recursion_json_diff.txt',
                'r'
        ).read().rstrip()

    def test_recurs_yaml_stylish_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/recursion.yml',
            './gendiff/tests/fixtures/recursion2.yml',
            formatter="stylish") \
            == open(
                './gendiff/tests/fixtures/result_recursion_yaml_diff.txt',
                'r'
        ).read().rstrip()

    def test_recurs_json_stylish_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/recursion.json',
            './gendiff/tests/fixtures/recursion.json',
            formatter="stylish") \
            == open(
                './gendiff/tests/fixtures/result_recursion_json_equal.txt',
                'r'
        ).read().rstrip()

    def test_recurs_yaml_stylish_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/recursion.yml',
            './gendiff/tests/fixtures/recursion.yml',
            formatter="stylish") \
            == open(
                './gendiff/tests/fixtures/result_recursion_yaml_equal.txt',
                'r'
        ).read().rstrip()

    def test_recurs_json_plain_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/recursion.json',
            './gendiff/tests/fixtures/recursion2.json',
            formatter="plain") \
            == open(
                './gendiff/tests/fixtures/result_recursion_json_diff_plain.'
                'txt',
                'r'
        ).read().rstrip()

    def test_recurs_json_plain_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/recursion.json',
            './gendiff/tests/fixtures/recursion.json',
            formatter="plain") \
            == ''

    def test_recurs_yaml_plain_diff(self):
        assert generate_diff(
            './gendiff/tests/fixtures/recursion.yml',
            './gendiff/tests/fixtures/recursion2.yml',
            formatter="plain") \
            == open(
                './gendiff/tests/fixtures/result_recursion_yaml_diff_plain.'
                'txt',
                'r'
        ).read().rstrip()

    def test_recurs_yaml_plain_equal(self):
        assert generate_diff(
            './gendiff/tests/fixtures/recursion.yml',
            './gendiff/tests/fixtures/recursion.yml',
            formatter="plain") \
            == ''
