import os

dir_path = os.path.dirname(os.path.realpath(__file__))

AVAILABLE_TYPES = ['text_task', 'text_lang']

# user contrib
ARCHITECTURE_FOLDER = "architectures"
REPO_FOLDER = "adapters"
TASK_FOLDER = "tasks"
SUBTASK_FOLDER = "subtasks"

# generated/ pre-defined
INDEX_FOLDER = "index_{}"
SCHEMA_FOLDER = os.path.join(dir_path, "schemas")
TEMPLATE_FOLDER="TEMPLATES"
