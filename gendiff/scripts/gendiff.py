#!usr/bin/env python

import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    # parser.add_argument(
    #        "-n", "--no_colors", action="store_true",
    #        help="Print non colored result"
    #        )
    parser.add_argument(
            "-f", "--format", help="set format of output",
            default='stylish',
            choices=['stylish', 'plain', 'json', 'raw'],
            action='store',
            )
    # This func return container Namespace (obj), which will built up from
    # attributes parsed out of the command line
    parser.parse_args()
    # Access to args from namespace obj is like calls attr of
    # class instance - by '.'

    # no_colors = parser.parse_args().no_colors
    formatter = parser.parse_args().format

    print(
            generate_diff(
                parser.parse_args().first_file,
                parser.parse_args().second_file,
                formatter
                ),
            # no_colors
            )


if __name__ == "__main__":
    main()
