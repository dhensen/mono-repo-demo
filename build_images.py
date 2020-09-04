import subprocess
import json
from typing import Union

services = ['nginx', 'portaal_backend', 'portaal_frontend', 'postgres']

git_diff_per_dir = 'git diff --quiet HEAD {ref} -- {directory}'

versions = {}


def run(command) -> subprocess.CompletedProcess:
    return subprocess.run(
        command,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )


def get_commit_hash(ref='HEAD') -> str:
    res = run(f'git rev-parse --short {ref}')
    return res.stdout.strip()


def is_changed_since(last_change_ref, directory):
    command = git_diff_per_dir.format(ref=last_change_ref, directory=directory)
    res = run(command)
    return res.returncode == 1


def build(service, version):
    res = run(
        "docker build -f services/{service}/Dockerfile -t demo/{service}:{version} ."
        .format(service=service, version=version))
    save_version(service, version)


def save_version(service, version):
    global versions
    with open('versions.json', mode='w') as versions_file:
        versions[service] = version
        json.dump(versions, versions_file)


def get_version(service) -> Union[str, None]:
    global versions
    if not versions:
        try:
            with open('versions.json', mode='r') as versions_file:
                versions = json.load(versions_file)
        except FileNotFoundError:
            pass

    return versions.get(service, None)


current_commit_hash = get_commit_hash()
print(f'current commit hash: {current_commit_hash}')

for service in services:
    last_service_version = get_version(service)
    print(f'- {service}:')

    if not last_service_version or is_changed_since(last_service_version,
                                                    f'src/{service}'):
        print(f'\tservice {service} requires a build')
        build(service, current_commit_hash)
    else:
        print(f'\tservice {service} is not changed')
