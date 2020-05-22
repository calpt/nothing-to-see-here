import json
import sys
from transformers import AutoConfig, AutoModel
from generate import REPO_FOLDER


def _violation(s):
    print("VIOLATION:", s)


def check_download(adapter_file):
    """Checks if the download links of the given adapter description file are valid.
    """
    print("-"*5, f"Checking {adapter_file}", "-"*5)
    with open(adapter_file, 'r') as f:
        adapter_dict = json.load(f)
    config = AutoConfig.for_model(
        adapter_dict['model_type'],
        hidden_size=adapter_dict['hidden_size']
    )
    model = AutoModel.from_config(config)
    for version, file in adapter_dict['_meta']['files'].items():
        try:
            # TODO add support for other checksums
            model.load_adapter(
                file['url'],
                adapter_dict['type'],
                load_as=version,
                checksum=file['sha1']
            )
        except Exception as e:
            _violation("[{}]: {}".format(e.__class__.__name__, e))
            return True
    return False


if __name__ == "__main__":
    files = [f for f in sys.argv[1:] if f.startswith(REPO_FOLDER)]
    for file in files:
        has_error = check_download(file)
        if has_error:
            sys.exit(f"FAILED: {file}!")
        else:
            print(f"PASSED: {file}.")
            print("")
