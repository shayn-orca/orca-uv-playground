# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "gitpython==3.1.42",
# ]
# ///
import git


def print_current_branch():
    repo = git.Repo(search_parent_directories=True)
    branch = repo.active_branch
    print(f"Current branch: {branch}")


print_current_branch()
