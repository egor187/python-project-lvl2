#!usr/bin/env python

import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    parser.parse_args()
    """Access to args from namespace obj is
    like calls attr of class instance - by '.'"""
    print(
            generate_diff(
                parser.parse_args().first_file, parser.parse_args().second_file
                )
            )


if __name__ == "__main__":
    main()
