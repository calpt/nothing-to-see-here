from collections import defaultdict
from glob import glob
import json
import os
from os.path import join
import sys


AVAILABLE_TYPES = ['text_task', 'text_lang', 'vision_task']


def generate_index(files, dist_folder="dist"):
    """Generates index files.
    """
    index = defaultdict(
        lambda: defaultdict(
            lambda: defaultdict(
                lambda: defaultdict(dict))))
    # add all files to index
    for file in files:
        with open(file, 'r') as f:
            adapter_dict = json.load(f)
        path_split = file.split(os.sep)
        a_type = adapter_dict['type']
        a_task = adapter_dict['_meta']['task']
        a_name = adapter_dict['_meta']['dataset']
        a_id = adapter_dict['_meta']['id']
        org_name = path_split[-2]
        if a_type not in AVAILABLE_TYPES:
            raise ValueError("Invalid type '{}'.".format(a_type))
        id_dict = index[a_type][a_task][a_name][a_id]
        if "versions" not in id_dict:
            id_dict["versions"] = {}
        id_dict["versions"][org_name] = file
        # TODO change default version to something more useful
        index[a_type][a_task][a_name][a_id]["default"] = org_name
    # write index files to disc
    for a_type, adapters in index.items():
        with open(join(dist_folder, a_type+".json"), 'w') as f:
            json.dump(adapters, f, indent=4, sort_keys=True)
    return index


if __name__ == "__main__":
    repo_glob = join(sys.argv[1], "**", "*")
    dist_folder = sys.argv[2] if len(sys.argv) > 2 else "dist"
    files = glob(repo_glob)
    generate_index(files, dist_folder=dist_folder)
