from gendiff.generate_diff import generate_diff


def test():
    assert generate_diff(
            '/home/egor_22_linux/python-project-lvl2/'
            'gendiff/tests/fixtures/file1.json',
            '/home/egor_22_linux/python-project-lvl2'
            '/gendiff/tests/fixtures/file2.json') \
            == open('./gendiff/tests/fixtures/test_1_res.txt', 'r'
                    ).read()
