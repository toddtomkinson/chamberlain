import json


def load_json_file(file_path):
    with open(file_path, "r") as file_handle:
        content = file_handle.read().replace('\n', '')

    return json.loads(content)


def write_json_file(file_path, data):
    with open(file_path, "w") as file_handle:
        file_handle.write(json.dumps(data))