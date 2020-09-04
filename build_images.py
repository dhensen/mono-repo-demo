import subprocess

services = ['nginx', 'portaal_backend', 'portaal_frontend', 'postgres']

git_diff_per_dir = 'git diff --quiet HEAD {ref} -- {directory}'


def is_changed_since(last_change_ref, directory):
    command = git_diff_per_dir.format(ref=last_change_ref, directory=directory)
    subprocess.run()


for service in services:
    print(service)
