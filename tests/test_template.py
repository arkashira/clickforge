import pytest
import json
from template import Template, load_env_file

def test_template_render():
    template = Template("example", {"VARIABLE": "value"})
    assert template.render() == "Template example with env vars: {'VARIABLE': 'value'}"

def test_load_env_file_valid_json():
    with open("test_env.json", "w") as file:
        json.dump({"VARIABLE": "value"}, file)
    env_vars = load_env_file("test_env.json")
    assert env_vars == {"VARIABLE": "value"}

def test_load_env_file_invalid_json():
    with open("test_env.json", "w") as file:
        file.write("Invalid JSON")
    env_vars = load_env_file("test_env.json")
    assert env_vars == {}

def test_load_env_file_file_not_found():
    env_vars = load_env_file("non_existent_file.json")
    assert env_vars == {}

def test_main_with_env_file():
    with open("test_env.json", "w") as file:
        json.dump({"VARIABLE": "value"}, file)
    import sys
    import io
    import argparse
    from contextlib import redirect_stdout
    with redirect_stdout(io.StringIO()) as f:
        sys.argv = ["template.py", "--env-file", "test_env.json"]
        from src.template import main
        main()
    assert f.getvalue().strip() == "Template example with env vars: {'VARIABLE': 'value'}"

def test_main_without_env_file():
    import sys
    import io
    import argparse
    from contextlib import redirect_stdout
    with redirect_stdout(io.StringIO()) as f:
        sys.argv = ["template.py"]
        from src.template import main
        main()
    assert f.getvalue().strip() == "Template example with env vars: {}"
