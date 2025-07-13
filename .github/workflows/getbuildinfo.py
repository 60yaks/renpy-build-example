import os
import re

env_file = os.getenv("GITHUB_ENV")

with open(env_file, "a") as envfile:
    with open("game/options.rpy", "r") as f:
        content = f.read()

        match = re.search(r"define\s+config.name\s*=\s*_\(\"(.+)\"\)", content)
        if match:
            envfile.write(f"BUILD_NAME={match.group(1)}\n")

        match = re.search(r"define\s+config.version\s*=\s*\"(.+)\"", content)
        if match:
            envfile.write(f"BUILD_VERSION={match.group(1)}\n")
