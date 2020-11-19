FROM python:3-alpine

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./tools/get_pulls.py get_pulls.py
COPY ./tools/get_pr_number.py get_pr_number.py
COPY ./tools/get_pr_comment.py get_pr_comment.py
