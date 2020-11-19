FROM python:3-alpine

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY get_pulls.py get_pulls.py
COPY get_pr_number.py get_pr_number.py
COPY get_pr_comment.py get_pr_comment.py
