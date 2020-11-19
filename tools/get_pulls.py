"""
Get list of opened Pull Requests from Github API
"""
import sys

from github import Github

TOKEN = sys.argv[1]
REPO_NAME = sys.argv[2]

def get_pr_list():
    """ Return list of opened PRs """
    github_init = Github(TOKEN)
    repo = github_init.get_repo(REPO_NAME)
    pulls = repo.get_pulls(state='open', sort='created', base='master')
    pr_list = []
    for pull_request in pulls:
        pr_list.append("pr-" + str(pull_request.number))

    # print list without brackets
    print(', '.join(map(str, pr_list)))

if __name__ == "__main__":
    get_pr_list()
