import os
import sys
import argparse
import tomli as tomllib
from pathlib import Path


def get_config():
    directory = os.path.abspath("./")
    config_path = Path(os.path.join(directory, "pyproject.toml"))

    with open(config_path, "rb") as conf:
        config_toml = tomllib.load(conf)
    config = config_toml["tool"]["towncrier"]
    return config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--content', default='',
        help='Enter the contents for the news fragment to modify.'
    )
    parser.add_argument(
        '--fragments', nargs='+', type=str,
        help='Enter the list of fragment types for the new fragment you want to modify.'
    )

    args = parser.parse_args()
    if not args.content:
        print("::error ::No contents given from args.")
        sys.exit(1)
    if not args.fragments:
        print("::error ::No fragment types given from args.")
        sys.exit(1)

    config = get_config()
    fragment_dir = config.get("directory")
    try:
        files = os.listdir(fragment_dir)
    except FileNotFoundError as e:
        raise Exception()
    for basename in files:
        parts = basename.split(".")
        if len(parts) != 3 or parts[1] not in args.fragments:
            continue
        output_path = Path(os.path.join(fragment_dir, basename))
        output_path.write_text(args.content)
        print(
            f'\n### {parts[1].title()}\n * {args.content} ({basename})', file=sys.stderr)
    print('Successfully updated the news fragment found by towncrier.', file=sys.stderr)


if __name__ == '__main__':
    main()
