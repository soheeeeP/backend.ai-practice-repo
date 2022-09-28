from operator import le
import os
import tomli as tomllib

pr_n_title, pr_labels = "", []

directory = os.path.abspath("./")
pyproject_toml = os.path.join(directory, "pyproject.toml")

with open(pyproject_toml, "rb") as conf:
    bconfig = tomllib.load(conf)

config = bconfig["tool"]["towncrier"]
fragment_types = [t["directory"] for t in config.get("type")]
fragment_dir = config.get("directory")
try:
    files = os.listdir(fragment_dir)    # ['5.feature.md', 'template.md', '5.doc.md']
except FileNotFoundError as e:
    raise Exception()

for basename in files:
    parts = basename.split(".")
    if len(parts) != 3 or parts[1] not in pr_labels:
        continue
    # Update news fragment file content if there is matching label.
    with open(parts, "rb") as f:
        ## update file content...
        pass
