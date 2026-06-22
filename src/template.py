import argparse
import json
from dataclasses import dataclass

@dataclass
class Template:
    name: str
    env_vars: dict

    def render(self):
        return f"Template {self.name} with env vars: {self.env_vars}"

def load_env_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File {file_path} not found")
        return {}
    except json.JSONDecodeError:
        print(f"Invalid JSON in file {file_path}")
        return {}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env-file', help='Path to environment variables file')
    args = parser.parse_args()
    env_vars = load_env_file(args.env_file) if args.env_file else {}
    template = Template("example", env_vars)
    print(template.render())

if __name__ == "__main__":
    main()
