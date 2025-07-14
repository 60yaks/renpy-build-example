import os
import re

with open("game/options.rpy", "r") as f:
    content = f.read()

    match = re.search(r"define\s+config.name\s*=\s*_\(\"(.+)\"\)", content)
    buildName = match.group(1)

    match = re.search(r"define\s+config.version\s*=\s*\"(.+)\"", content)
    buildVersion = match.group(1)

print(f"BUILD_NAME={buildName}")
print(f"BUILD_VERSION={buildVersion}")

with open(os.getenv("GITHUB_ENV"), "a") as envfile:
    envfile.write(f"BUILD_NAME={buildName}\n")
    envfile.write(f"BUILD_VERSION={buildVersion}\n")
