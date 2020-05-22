### Definitions

- `<id>`: 24-char unique identifier describing the model architecture, the adapter architecture and the adapter type.
- `<task>`: the name of the task the adapter is categorized under (e.g. `sentiment`, `question_answering`, `nli` for task adapters or `en`, `de` for language adapters).
- `<dataset>`: the dataset or domain the adapter was trained on (e.g. `multinli`, `squad1.1`, `wiki`)
- `weights_name` (of an adapter): the name under which adapter weights are saved in the weights file. Given in the `name` attribute of the adapter config and required for reloading. (This name originates from calling `model.add_adapter(<weights_name>, <type>)`).
- `<config>`: either an identifier for an adapter architecture (e.g. `pfeiffer`) or a complete config dict.
- `<type>`: the adapter type (e.g. `text_task`).
- `<org_name>`: name of the orga., GH user... that maintains the adapter.

### Loading

Adapters are loaded with: `model.load_adapter(<specifier>, <type>, config=<config>, version=<version>)`.

`<specifier>` can be one of the following iff globally unique:
- `<task>`
- `<task>/<dataset>`
- `<dataset>`
- `<task>@<org_name>`
- `<task>/<dataset>@<org_name>`
- `<dataset>@<org_name>`

### File structure

#### Index files

Placed in `/<index>/<type>.json`.

```
{
    <task>: {
        <dataset>: {
            <id>: {
                "default": "<org_name>-<custom_name>",
                "versions": {
                    <org_name>: "<org_name>/<file_name>.json"
                    ...
                }
            }
            ...
        }
        ...
    }
    ...
}
```

#### Config files

Placed in `/repo/<org_name>/<file_name>.json`.

```
{
    "_meta": {
        "id": <id>,
        ...
        "task": <task>,
        "dataset": <dataset>
        ...
    }
    "config": <config>,
    ...
    "name": <weights_name>,
    "type": <type>
}
```
