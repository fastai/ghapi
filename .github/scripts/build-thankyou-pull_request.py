from fastcore.all import *
from ghapi import *

def reply_thanks():
    payload = context_github.event
    if payload.action != 'opened': return
    api = GhApi(owner='fastai', repo='ghapi', token=github_token())
    api.issues.create_comment(issue_number=payload.number, body='Thank you for your *valuable* contribution')

reply_thanks()
