# ghapi
> A delightful and complete interface to GitHub's amazing API


`ghapi` provides 100% always-updated coverage of the entire [GitHub API](https://docs.github.com/en/free-pro-team@latest/rest). Because we automatically convert the [OpenAPI spec](https://docs.github.com/en/free-pro-team@latest/rest/overview/openapi-description) to a Pythonic API, `ghapi` is always up to date with the latest changes to GitHub APIs. Furthermore, because this is all done dynamically, the entire package is only 35kB in size!

Using `ghapi`, you can automate nearly anything that you can do through the GitHub web interface or through the `git` client, such as:

- Open, list, comment on, or modify [issues](https://guides.github.com/features/issues/) or [pull requests](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-requests)
- Create, list, or modify [git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) or [GitHub releases](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/managing-releases-in-a-repository), including uploading release assets
- Configure and run GitHub [Actions](https://github.com/features/actions) and [webhooks](https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/about-webhooks)
- Set up GitHub [users](https://docs.github.com/en/free-pro-team@latest/rest/reference/users) and [organizations](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-organizations-and-teams/about-organizations)
- Manage your [deployments](https://docs.github.com/en/free-pro-team@latest/rest/guides/delivering-deployments)
- ...and much, much more.

There are two ways to use `ghapi`: either through Python, or from the command line. An overview of each is provided below.

## Installation

To install, run either `pip install ghapi` or `conda install -c fastai ghapi`.

## How to use - Python

Throughout this documentation, you will see code inputs and outputs shown in this format:

```python
1+1
```




    2



We recommend reading the documentation on the [official site](https://ghapi.fast.ai/), rather than on GitHub, since not all the functionality described on this page is available through the GitHub viewer.

All of the documentation is available directly as Jupyter Notebooks, for instance the current page you're reading is available as a notebook [here](https://github.com/fastai/ghapi/blob/master/index.ipynb). To open any page as an interactive notebook in Google Colab, click the *Colab* badge at the top of the page.

To access the GitHub API, first create a `GhApi` object:

```python
from ghapi.all import GhApi
api = GhApi()
```

Every part of the API includes documentation directly in the `api` object itself. For instance, here's how to explore the groups of functionality provided by the API by displaying the object:

```python
api
```




- [actions](https://docs.github.com/en/free-pro-team@latest/rest/reference/actions)
- [activity](https://docs.github.com/en/free-pro-team@latest/rest/reference/activity)
- [apps](https://docs.github.com/en/free-pro-team@latest/rest/reference/apps)
- [billing](https://docs.github.com/en/free-pro-team@latest/rest/reference/billing)
- [checks](https://docs.github.com/en/free-pro-team@latest/rest/reference/checks)
- [code_scanning](https://docs.github.com/en/free-pro-team@latest/rest/reference/code-scanning)
- [codes_of_conduct](https://docs.github.com/en/free-pro-team@latest/rest/reference/codes-of-conduct)
- [emojis](https://docs.github.com/en/free-pro-team@latest/rest/reference/emojis)
- [enterprise_admin](https://docs.github.com/en/free-pro-team@latest/rest/reference/enterprise-admin)
- [gists](https://docs.github.com/en/free-pro-team@latest/rest/reference/gists)
- [git](https://docs.github.com/en/free-pro-team@latest/rest/reference/git)
- [gitignore](https://docs.github.com/en/free-pro-team@latest/rest/reference/gitignore)
- [interactions](https://docs.github.com/en/free-pro-team@latest/rest/reference/interactions)
- [issues](https://docs.github.com/en/free-pro-team@latest/rest/reference/issues)
- [licenses](https://docs.github.com/en/free-pro-team@latest/rest/reference/licenses)
- [markdown](https://docs.github.com/en/free-pro-team@latest/rest/reference/markdown)
- [meta](https://docs.github.com/en/free-pro-team@latest/rest/reference/meta)
- [migrations](https://docs.github.com/en/free-pro-team@latest/rest/reference/migrations)
- [oauth_authorizations](https://docs.github.com/en/free-pro-team@latest/rest/reference/oauth-authorizations)
- [orgs](https://docs.github.com/en/free-pro-team@latest/rest/reference/orgs)
- [projects](https://docs.github.com/en/free-pro-team@latest/rest/reference/projects)
- [pulls](https://docs.github.com/en/free-pro-team@latest/rest/reference/pulls)
- [rate_limit](https://docs.github.com/en/free-pro-team@latest/rest/reference/rate-limit)
- [reactions](https://docs.github.com/en/free-pro-team@latest/rest/reference/reactions)
- [repos](https://docs.github.com/en/free-pro-team@latest/rest/reference/repos)
- [scim](https://docs.github.com/en/free-pro-team@latest/rest/reference/scim)
- [search](https://docs.github.com/en/free-pro-team@latest/rest/reference/search)
- [secret_scanning](https://docs.github.com/en/free-pro-team@latest/rest/reference/secret-scanning)
- [teams](https://docs.github.com/en/free-pro-team@latest/rest/reference/teams)
- [users](https://docs.github.com/en/free-pro-team@latest/rest/reference/users)



Then we can explore the endpoints provided by the API in each group, e.g. for the `git` group:

```python
api.git
```




- [git.create_blob](https://docs.github.com/rest/reference/git#create-a-blob)(owner, repo, content, encoding): *Create a blob*
- [git.get_blob](https://docs.github.com/rest/reference/git#get-a-blob)(owner, repo, file_sha): *Get a blob*
- [git.create_commit](https://docs.github.com/rest/reference/git#create-a-commit)(owner, repo, message, tree, parents, author, committer, signature): *Create a commit*
- [git.get_commit](https://docs.github.com/rest/reference/git#get-a-commit)(owner, repo, commit_sha): *Get a commit*
- [git.list_matching_refs](https://docs.github.com/rest/reference/git#list-matching-references)(owner, repo, ref, per_page, page): *List matching references*
- [git.get_ref](https://docs.github.com/rest/reference/git#get-a-reference)(owner, repo, ref): *Get a reference*
- [git.create_ref](https://docs.github.com/rest/reference/git#create-a-reference)(owner, repo, ref, sha, key): *Create a reference*
- [git.update_ref](https://docs.github.com/rest/reference/git#update-a-reference)(owner, repo, ref, sha, force): *Update a reference*
- [git.delete_ref](https://docs.github.com/rest/reference/git#delete-a-reference)(owner, repo, ref): *Delete a reference*
- [git.create_tag](https://docs.github.com/rest/reference/git#create-a-tag-object)(owner, repo, tag, message, object, type, tagger): *Create a tag object*
- [git.get_tag](https://docs.github.com/rest/reference/git#get-a-tag)(owner, repo, tag_sha): *Get a tag*
- [git.create_tree](https://docs.github.com/rest/reference/git#create-a-tree)(owner, repo, tree, base_tree): *Create a tree*
- [git.get_tree](https://docs.github.com/rest/reference/git#get-a-tree)(owner, repo, tree_sha, recursive): *Get a tree*



Here's how to learn about an endpoint you want to use, e.g.:

```python
api.git.get_ref
```




[git.get_ref](https://docs.github.com/rest/reference/git#get-a-reference)(owner, repo, ref): *Get a reference*



In Jupyter Notebook full tab completion, parameter lists, etc are provided for all endpoints. Endpoints are called as standard Python methods:

```python
api.git.get_ref(owner='fastai', repo='fastcore', ref='heads/master')
```




- ref: refs/heads/master
- node_id: MDM6UmVmMjI1NDYwNTk5OnJlZnMvaGVhZHMvbWFzdGVy
- url: https://api.github.com/repos/fastai/fastcore/git/refs/heads/master
- object: 
  - sha: 0e3084ed009baa51db38a640ae7c23d638af2756
  - type: commit
  - url: https://api.github.com/repos/fastai/fastcore/git/commits/0e3084ed009baa51db38a640ae7c23d638af2756



To use `ghapi` to access authenticated operations (other than when running through GitHub Actions), you will need a GitHub [personal access token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token), which is a secret code used to access your account. If you don't have one, [click here](https://github.com/settings/tokens/new) to create one. You'll be asked to enter a name -- choose anything you like, for instance "*ghapi*". You'll also be asked to choose "scopes"; this limits what you'll be able to do with the API using this token. If you're not sure, click "*repo*" "*gist*", "*notifications*", and "*workflow*". Then click "Generate Token" at the bottom of the screen, and copy the token (the long string of letters and numbers shown). You can easily do that by clicking the little clipboard icon next to the token.

Rather than pasting that token into every script, it's easiest to save it as an environment variable. If you save it as `$GITHUB_TOKEN` then it will be most convenient, so add this to the end of your `.bashrc` or `.zshrc` file:

    export GITHUB_TOKEN=xxx

...replacing the `xxx` with the token you just copied. (Don't forget to `source` that file after you change it.), pass a [GitHub token].

As well as your `token`, you can also pass any parameters you want auto-inserted into relevant methods, such as `owner` and `repo`:

```python
api = GhApi(owner='fastai', repo='fastcore', token=github_token)
```

We can now repeat the previous method, but only need to pass `ref`:

```python
api.git.get_ref('heads/master')
```




- ref: refs/heads/master
- node_id: MDM6UmVmMjI1NDYwNTk5OnJlZnMvaGVhZHMvbWFzdGVy
- url: https://api.github.com/repos/fastai/fastcore/git/refs/heads/master
- object: 
  - sha: 0e3084ed009baa51db38a640ae7c23d638af2756
  - type: commit
  - url: https://api.github.com/repos/fastai/fastcore/git/commits/0e3084ed009baa51db38a640ae7c23d638af2756



Now that we've provided our token, we can use authenticated endpoints such as creating an issue:

```python
issue = api.issues.create("Remember to check out GhApi!")
```

Since we've now checked out GhApi, let's close this issue. 😎

```python
api.issues.update(issue.number, state='closed')
```

## How to use - command line

You can use `GhApi` via the command line, and can access nearly everything in the [GitHub API](https://docs.github.com/en/free-pro-team@latest/rest). We provide an overview here of one of the command line programs, `ghapi` -- see the full CLI docs page for details on all the programs available.

We strongly recommend enabling tab completion for `ghapi`, which you can do by placing the following command at the end of your `~/.bashrc` or `~/.zshrc` file:

```bash
eval "$(completion-ghapi --install)"
```

To get started with the `ghapi` command, first find the name of the operation you wish to perform, for instance by searching the [full API reference](https://ghapi.fast.ai/fullapi.html).

To use `ghapi`, pass the method name (exactly the same as you'd use in the Python API) as the first parameter, followed by any positional parameters required, and then keyword arguments with "`--`" before each parameter name.

For instance, [git.get_ref](https://ghapi.fast.ai/fullapi.html#git) takes three parameters: `owner`, `repo`, and `ref`. If we wish to pass the first two as positional parameters, and the last as a named argument, then we'd call:

```bash
ghapi git.get_ref fastai ghapi-test --ref heads/master
```

If you have enabled tab completion, then after you've typed `ghapi g` try pressing <kbd>Tab</kbd>, and you'll see all the operation groups available in the GitHub API that start with `g`. If you keep typing, e.g. `ghapi git.`, and hit <kbd>Tab</kbd> again, you'll now see all the operations available in the `git` group, i.e:

```
git.create_blob git.create_commit git.create_ref git.create_tag git.create_tree git.delete_ref git.get_blob git.get_commit git.get_ref git.get_tag git.get_tree git.list_matching_refs git.name git.update_ref git.verbs
```

If you pass just `--help` after the operation name, you'll see a full list of all parameters accepted, and a link to the official GitHub documentation.

```bash
ghapi --help
> >> git.get_ref(owner, repo, ref)
>>> https://docs.github.com/rest/reference/git#get-a-reference```

In addition to `--help` and the GitHub operation parameters, you can also pass the following:

- `--headers`: A list of extra headers to pass, JSON-encoded
- `--token`: A GitHub authentation token
- `--debug`: Print requests before sending them
