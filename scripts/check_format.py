import json
from json.decoder import JSONDecodeError
import os
from os.path import join
import sys
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from generate import AVAILABLE_TYPES


def _violation(s):
    print("VIOLATION:", s)


def check_format(adapter_file, schema):
    """Checks if the given adapter description file meets some requirements.
    """
    print("-"*5, f"Checking {adapter_file}", "-"*5)
    # 1. load to json dict
    with open(adapter_file, 'r') as f:
        try:
            file_dict = json.load(f)
        except JSONDecodeError as e:
            _violation("[{}]: {}".format(e.__class__.__name__, e.msg))
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
    # TODO verify config identifier
    # 5. check meta section
    # TODO verify some of the values
    meta_dict = file_dict['_meta']
    # 6. check files
    if not meta_dict['default_version'] in meta_dict['files']:
        _violation(f"Specified default_version is not in files.")
        has_error = True
    return has_error


if __name__ == "__main__":
    # load schema
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(join(dir_path, 'adapter.schema.json'), 'r') as f:
        schema = json.load(f)
    files = sys.argv[1:]
    for file in files:
        has_error = check_format(file, schema)
        if has_error:
            sys.exit(f"FAILED: {file}!")
        else:
            print(f"PASSED: {file}.")
            print("")
