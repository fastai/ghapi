from fastcore.all import *
from ghapi import *

def reply_thanks():
    payload = context_github.event
    if 'workflow' in payload: issue = 1
    else:
        if payload.action != 'opened': return
        api = GhApi(owner='fastai', repo='ghapi', token=github_token())
        issue = payload.number
    api.issues.create_comment(issue_number=issue, body='Thank you for your *valuable* contribution')

reply_thanks()

