import json
from json.decoder import JSONDecodeError
import os
from os.path import join
import sys
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import yaml
from config import *


def _violation(s):
    print("VIOLATION:", s)


def check_adapter_format(adapter_file, schema):
    """Checks if the given adapter description file meets some requirements.
    """
    print("-"*5, f"Checking {adapter_file}", "-"*5)
    # 1. load to dict
    with open(adapter_file, 'r') as f:
        try:
            file_dict = yaml.load(f, yaml.FullLoader)
        except yaml.YAMLError as e:
            _violation("[{}]: {}".format(e.__class__.__name__, e))
            return True
    # 2. validate against schema
    try:
        validate(file_dict, schema)
    except ValidationError as e:
        _violation("[{}]: {}".format(e.__class__.__name__, e.message))
        return True
    # 3. check type
    has_error = False
    if file_dict['type'] not in AVAILABLE_TYPES:
        _violation(f"Invalid adapter type '{file_dict['type']}' used.")
        has_error = True
    # 4. check config
    # -> identifier verified in generate.py
    # 5. check meta section
    # -> duplicate check in generate.py
    # 6. check files
    if not file_dict['default_version'] in [file['version'] for file in file_dict['files']]:
        _violation(f"Specified default_version is not in files.")
        has_error = True
    return has_error


def check_architecture_format(file, schema):
    print("-"*5, f"Checking {file}", "-"*5)
    # 1. load to dict
    with open(file, 'r') as f:
        try:
            file_dict = yaml.load(f, Loader=yaml.FullLoader)
        except yaml.YAMLError as e:
            _violation("[{}]: {}".format(e.__class__.__name__, e))
            return True
    # 2. validate against schema
    try:
        validate(file_dict, schema)
    except ValidationError as e:
        _violation("[{}]: {}".format(e.__class__.__name__, e.message))
        return True
    return False


if __name__ == "__main__":
    # get the type of files we want to check
    file_type = sys.argv[1]
    if file_type == "adapter":
        files = [f for f in sys.argv[2:] if f.startswith(REPO_FOLDER)]
        check_func = check_adapter_format
    elif file_type == "architecture":
        files = [f for f in sys.argv[2:] if f.startswith(ARCHITECTURE_FOLDER)]
        check_func = check_architecture_format
    elif file_type == "task":
        files = [f for f in sys.argv[2:] if f.startswith(TASK_FOLDER)]
    elif file_type == "subtask":
        files = [f for f in sys.argv[2:] if f.startswith(SUBTASK_FOLDER)]
    else:
        sys.exit("Invalid file_type '{}'".format(file_type))
    # load schema
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(join(dir_path, 'schemas', '{}.schema.json'.format(file_type)), 'r') as f:
        schema = json.load(f)
    # check files
    for file in files:
        has_error = check_func(file, schema)
        if has_error:
            sys.exit(f"FAILED: {file}!")
        else:
            print(f"PASSED: {file}.")
            print("")
