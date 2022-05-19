# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['GH_HOST', 'GhApi', 'date2gh', 'gh2date', 'print_summary', 'EMPTY_TREE_SHA']

# Cell
from fastcore.utils import *
from fastcore.foundation import *
from fastcore.meta import *
from .metadata import funcs

import mimetypes,base64
from inspect import signature,Parameter,Signature
from urllib.request import Request
from urllib.error import HTTPError
from urllib.parse import quote
from datetime import datetime,timedelta
from pprint import pprint
import os

# Cell
GH_HOST = os.getenv('GH_HOST', "https://api.github.com")
_DOC_URL = 'https://docs.github.com/'

# Cell
def _preview_hdr(preview): return {'Accept': f'application/vnd.github.{preview}-preview+json'} if preview else {}

def _mk_param(nm, **kwargs): return Parameter(nm, kind=Parameter.POSITIONAL_OR_KEYWORD, **kwargs)
def _mk_sig_detls(o):
    res = {}
    if o[0]!=object: res['annotation']=o[0]
    res['default'] = o[1] if len(o)>1 else None
    return res
def _mk_sig(req_args, opt_args, anno_args):
    params =  [_mk_param(k) for k in req_args]
    params += [_mk_param(k, default=v) for k,v in opt_args.items()]
    params += [_mk_param(k, **_mk_sig_detls(v)) for k,v in anno_args.items()]
    return Signature(params)

# Cell
class _GhObj: pass

# Cell
class _GhVerb(_GhObj):
    __slots__ = 'path,verb,tag,name,summary,url,route_ps,params,data,preview,client,__doc__'.split(',')
    def __init__(self, path, verb, oper, summary, url, params, data, preview, client, kwargs):
        tag,*name = oper.split('/')
        name = '__'.join(name)
        name = name.replace('-','_')
        path,_,_ = partial_format(path, **kwargs)
        route_ps = stringfmt_names(path)
        __doc__ = summary
        data = {o[0]:o[1:] for o in data}
        store_attr()

    def __call__(self, *args, headers=None, **kwargs):
        headers = {**_preview_hdr(self.preview),**(headers or {})}
        d = list(self.data)
        flds = [o for o in self.route_ps+self.params+d if o not in kwargs]
        for a,b in zip(args,flds): kwargs[b]=a
        kwargs = {k:v for k,v in kwargs.items() if v is not None}
        route_p,query_p,data_p = [{p:kwargs[p] for p in o if p in kwargs}
                                 for o in (self.route_ps,self.params,d)]
        return self.client(self.path, self.verb, headers=headers, route=route_p, query=query_p, data=data_p)

    def __str__(self): return f'{self.tag}.{self.name}{signature(self)}\n{self.doc_url}'
    @property
    def __signature__(self): return _mk_sig(self.route_ps, dict.fromkeys(self.params), self.data)
    __call__.__signature__ = __signature__
    @property
    def doc_url(self): return _DOC_URL + self.url.replace(" ","_")

    def _repr_markdown_(self):
        params = ', '.join(self.route_ps+self.params+list(self.data))
        return f'[{self.tag}.{self.name}]({self.doc_url})({params}): *{self.summary}*'
    __repr__ = _repr_markdown_

# Cell
class _GhVerbGroup(_GhObj):
    def __init__(self, name, verbs):
        self.name,self.verbs = name,verbs
        for o in verbs: setattr(self, o.name, o)
    def __str__(self): return "\n".join(str(v) for v in self.verbs)
    def _repr_markdown_(self): return "\n".join(f'- {v._repr_markdown_()}' for v in self.verbs)

# Cell
_docroot = 'https://docs.github.com/rest/reference/'

# Cell
class GhApi(_GhObj):
    def __init__(self, owner=None, repo=None, token=None, jwt_token=None, debug=None, limit_cb=None, gh_host=None, **kwargs):
        self.headers = { 'Accept': 'application/vnd.github.v3+json' }
        token = token or os.getenv('GITHUB_TOKEN', None)
        jwt_token = jwt_token or os.getenv('GITHUB_JWT_TOKEN', None)
        if jwt_token: self.headers['Authorization'] = 'Bearer ' + jwt_token
        if token: self.headers['Authorization'] = 'token ' + token
        if owner: kwargs['owner'] = owner
        if repo:  kwargs['repo' ] = repo
        funcs_ = L(funcs).starmap(_GhVerb, client=self, kwargs=kwargs)
        self.func_dict = {f'{o.path}:{o.verb.upper()}':o for o in funcs_}
        self.groups = {k.replace('-','_'):_GhVerbGroup(k,v) for k,v in groupby(funcs_, 'tag').items()}
        self.debug,self.limit_cb,self.limit_rem = debug,limit_cb,5000
        self.gh_host = gh_host or GH_HOST

    def __call__(self, path:str, verb:str=None, headers:dict=None, route:dict=None, query:dict=None, data=None):
        "Call a fully specified `path` using HTTP `verb`, passing arguments to `fastcore.core.urlsend`"
        if verb is None: verb = 'POST' if data else 'GET'
        headers = {**self.headers,**(headers or {})}
        if not path.startswith(('http://', 'https://')):
            path = self.gh_host + path
        if route:
            for k,v in route.items(): route[k] = quote(str(route[k]))
        res,self.recv_hdrs = urlsend(path, verb, headers=headers or None, debug=self.debug, return_headers=True,
                                     route=route or None, query=query or None, data=data or None)
        if 'X-RateLimit-Remaining' in self.recv_hdrs:
            newlim = self.recv_hdrs['X-RateLimit-Remaining']
            if self.limit_cb is not None and newlim != self.limit_rem:
                self.limit_cb(int(newlim),int(self.recv_hdrs['X-RateLimit-Limit']))
            self.limit_rem = newlim

        return dict2obj(res)

    def __dir__(self): return super().__dir__() + list(self.groups)
    def _repr_markdown_(self): return "\n".join(f"- [{o}]({_docroot + o.replace('_', '-')})" for o in sorted(self.groups))
    def __getattr__(self,k): return self.groups[k] if 'groups' in vars(self) and k in self.groups else stop(AttributeError(k))

    def __getitem__(self, k):
        "Lookup and call an endpoint by path and verb (which defaults to 'GET')"
        a,b = k if isinstance(k,tuple) else (k,'GET')
        return self.func_dict[f'{a}:{b.upper()}']

    def full_docs(self):
        return '\n'.join(f'## {gn}\n\n{group._repr_markdown_()}\n' for gn,group in sorted(self.groups.items()))

# Cell
@patch
def create_gist(self:GhApi, description, content, filename='gist.txt', public=False):
    return api.gists.create(description, public=public, files={filename: {"content": content}})

# Cell
def date2gh(dt:datetime)->str:
    "Convert `dt` (which is assumed to be in UTC time zone) to a format suitable for GitHub API operations"
    return f'{dt.replace(microsecond=0).isoformat()}Z'

# Cell
def gh2date(dtstr:str)->datetime:
    "Convert date string `dtstr` received from a GitHub API operation to a UTC `datetime`"
    return datetime.fromisoformat(dtstr.replace('Z', ''))

# Cell
def print_summary(req:Request):
    "Print `Request.summary` with the token (if any) removed"
    pprint(req.summary('Authorization'))

# Cell
@patch
def delete_release(self:GhApi, release):
    "Delete a release and its associated tag"
    self.repos.delete_release(release.id)
    self.git.delete_ref(f'tags/{release.tag_name}')

# Cell
@patch
def upload_file(self:GhApi, rel, fn):
    "Upload `fn` to endpoint for release `rel`"
    fn = Path(fn)
    url = rel.upload_url.replace('{?name,label}','')
    mime = mimetypes.guess_type(fn, False)[0] or 'application/octet-stream'
    return self(url, 'POST', headers={'Content-Type':mime}, query = {'name':fn.name}, data=fn.read_bytes())

# Cell
@patch
def create_release(self:GhApi, tag_name, branch='master', name=None, body='',
                   draft=False, prerelease=False, files=None):
    "Wrapper for `GhApi.repos.create_release` which also uploads `files`"
    if name is None: name = 'v'+tag_name
    rel = self.repos.create_release(tag_name, target_commitish=branch, name=name, body=body,
                                   draft=draft, prerelease=prerelease)
    for file in listify(files): self.upload_file(rel, file)
    return rel

# Cell
@patch
def list_tags(self:GhApi, prefix:str=''):
    "List all tags, optionally filtered to those starting with `prefix`"
    return self.git.list_matching_refs(f'tags/{prefix}')

# Cell
@patch
def list_branches(self:GhApi, prefix:str=''):
    "List all branches, optionally filtered to those starting with `prefix`"
    return self.git.list_matching_refs(f'heads/{prefix}')

# Cell
# See https://stackoverflow.com/questions/9765453
EMPTY_TREE_SHA = '4b825dc642cb6eb9a060e54bf8d69288fbee4904'

# Cell
@patch
def create_branch_empty(self:GhApi, branch):
    t = self.git.create_tree(base_tree=EMPTY_TREE_SHA, tree = [dict(
        path='.dummy', content='ignore me', mode='100644', type='blob')])
    c = self.git.create_commit(f'create {branch}', t.sha)
    return self.git.create_ref(f'refs/heads/{branch}', c.sha)

# Cell
@patch
def delete_tag(self:GhApi, tag:str):
    "Delete a tag"
    return self.git.delete_ref(f'tags/{tag}')

# Cell
@patch
def delete_branch(self:GhApi, branch:str):
    "Delete a branch"
    return self.git.delete_ref(f'heads/{branch}')

# Cell
@patch
def get_branch(self:GhApi, branch=None):
    branch = branch or self.repos.get().default_branch
    return self.list_branches(branch)[0]

# Cell
@patch
def list_files(self:GhApi, branch=None):
    ref = self.get_branch(branch)
    res = self.git.get_tree(ref.object.sha).tree
    return {o.path:o for o in res}

# Cell
@patch
def get_content(self:GhApi, path):
    res = self.repos.get_content(path)
    return base64.b64decode(res.content)

# Cell
@patch
def update_contents(self:GhApi, path, message=None, content=None,
                    sha=None, branch=None, committer=None, author=None):
    if sha is None: sha = self.list_files()[path].sha
    if not isinstance(content,bytes): content = content.encode()
    content = base64.b64encode(content).decode()
    return self.repos.create_or_update_file_contents(path, message, content=content,
        sha=sha, branch=branch, committer=committer, author=author)

# Cell
@patch
def enable_pages(self:GhApi, branch=None, path="/"):
    "Enable or update pages for a repo to point to a `branch` and `path`."
    if path not in ('/docs','/'): raise Exception("path not in ('/docs','/')")
    r = self.repos.get()
    branch = branch or r.default_branch
    source = {"branch": branch, "path": path}
    if r.has_pages: return self.repos.update_information_about_pages_site(source=source)
    if len(self.list_branches(branch))==0: self.create_branch_empty(branch)
    return self.repos.create_pages_site(source=source)