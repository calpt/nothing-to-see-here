#!/use/bin/env python3
import argparse
import glob
import json
from os.path import join, dirname, realpath
import sys
from check_format import check_against_schema
from check_download_files import check_download
from utils import REPO_FOLDER


dir_path = dirname(realpath(__file__))
repo_path = join(dirname(dir_path), REPO_FOLDER)


with open(join(dir_path, 'schemas', 'adapter.schema.json'), 'r') as f:
        schema = json.load(f)


def check_file(file):
    has_error = check_against_schema(file, schema)
    if not has_error:
        has_error = check_download(file)
    if has_error:
        sys.exit(1)


def check_user(username):
    print(f"Checking all files of user '{username}'\n")
    files = glob.glob(join(repo_path, username, "**"))
    for file in files:
        check_file(file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Use this script to validate your adapter yaml files.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help="Specifies a file to check")
    group.add_argument('-u', '--user', type=str, help="Specifies a username for which to check all files")
    args = parser.parse_args()

    if args.file:
        check_file(args.file)
    elif args.user:
        check_user(args.user)
