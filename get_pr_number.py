"""
Get PR number by Branch name from Github API
"""
import sys

from github import Github

TOKEN = sys.argv[1]
REPO_NAME = sys.argv[2]
BRANCH_NAME = sys.argv[3]

class EmptyPrList(Exception):
    """Exception for PR count"""
    pass

def get_pr_number():
    """Returned opened PR number from Branch name"""
    github_init = Github(TOKEN)
    repo = github_init.get_repo(REPO_NAME)
    head = f"{REPO_NAME}:{BRANCH_NAME}"

    pulls = repo.get_pulls(state='all', sort='created', base='master', head=head)
    pr_list = []
    for pull_request in pulls:
        pr_list.append(str(pull_request.number))
    if not pr_list:
        print("Error: this branch not have any pull-requests. Maybe branch is master?")
        raise EmptyPrList
    else:
        print(max(pr_list))

if __name__ == "__main__":
    get_pr_number()
