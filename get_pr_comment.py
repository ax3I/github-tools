"""
Get latest comment in PR from Github API
"""
import sys

from github import Github

TOKEN = sys.argv[1]
REPO_NAME = sys.argv[2]
PR_NUMBER = sys.argv[3]

def get_latest_comment():
    """Returned latest comment in PR"""
    github_init = Github(TOKEN)
    repo = github_init.get_repo(REPO_NAME)

    pull_request = repo.get_pull(number=PR_NUMBER)
    print(pull_request)
    comments = pull_request.get_issue_comments()
    comments_list = []
    for comment in comments:
        print("comment: " + comment.body)
        comments_list.append(str(comment.body))
    print('')
    print(f"latest comment in PR {PR_NUMBER} is: {comments_list[-1]}")

if __name__ == "__main__":
    get_latest_comment()
