import json
import logging
import sys
import yaml
from transformers import AutoConfig, AutoModel
from generate import REPO_FOLDER


def _violation(s):
    print("VIOLATION:", s)


def check_download(adapter_file):
    """Checks if the download links of the given adapter description file are valid.
    """
    print("-"*5, f"Checking {adapter_file}", "-"*5)
    with open(adapter_file, 'r') as f:
        adapter_dict = yaml.load(f, yaml.FullLoader)
    config = AutoConfig.from_pretrained(adapter_dict['model_name'])
    if not config.model_type == adapter_dict['model_type']:
        _violation(
            f"Specified model_type '{adapter_dict['model_type']}' does not match loaded model_type '{config.model_type}'."
        )
        return True
    model = AutoModel.from_config(config)
    for file in adapter_dict['files']:
        try:
            # TODO add support for other checksums
            model.load_adapter(
                file['url'],
                adapter_dict['type'],
                config=adapter_dict['config'],
                load_as=file['version'],
                checksum=file['sha1']
            )
        except Exception as e:
            _violation("[{}]: {}".format(e.__class__.__name__, e))
            return True
    return False


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)

    files = [f for f in sys.argv[1:] if f.startswith(REPO_FOLDER)]
    for file in files:
        has_error = check_download(file)
        if has_error:
            sys.exit(f"FAILED: {file}!")
        else:
            print(f"PASSED: {file}.")
            print("")
