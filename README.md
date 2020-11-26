# GhApi
> A delightful and complete interface to GitHub's amazing API


`GhApi` provides 100% always-updated coverage of the entire [GitHub API](https://docs.github.com/en/free-pro-team@latest/rest). Because we automatically convert the [OpenAPI spec](https://docs.github.com/en/free-pro-team@latest/rest/overview/openapi-description) to a Pythonic API, `GhApi` is always up to date with the latest changes to GitHub APIs.

Using `GhApi`, you can do anything that you can do through the GitHub web interface or through the `git` client, such as:

- Open, list, comment on, or modify [issues](https://guides.github.com/features/issues/) or [pull requests](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-requests)
- Create, list, or modify [git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) or [GitHub releases](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/managing-releases-in-a-repository), including uploading release assets
- Configure and run GitHub [Actions](https://github.com/features/actions) and [webhooks](https://docs.github.com/en/free-pro-team@latest/developers/webhooks-and-events/about-webhooks)
- Set up GitHub [users](https://docs.github.com/en/free-pro-team@latest/rest/reference/users) and [organizations](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-organizations-and-teams/about-organizations)
- Manage your [deployments](https://docs.github.com/en/free-pro-team@latest/rest/guides/delivering-deployments)
- ...and much, much more.

## Install

Either `pip install ghapi` or `conda install -c fastai ghapi`.

## How to use

Throughout this documentation, you will see code inputs and outputs shown in this format:

```python
1+1
```




    2



We recommend reading the documentation on the [official site](https://ghapi.fast.ai/), rather than on GitHub, since not all the functionality described on this page is available through the GitHub viewer.

All of the documentation is available directly as Jupyter Notebooks, for instance the current page you're reading is available as a notebook [here](https://github.com/fastai/ghapi/blob/master/index.ipynb). To open any page as an interactive notebook in Google Colab, click the *Colab* badge at the top of the page.

To access the GitHub API, first create a `GhApi` object:

```python
api = GhApi()
```

Every part of the API includes documentation directly in the `api` object itself. For instance, here's how to explore the groups of functionality provided by the API by displaying the object:

```python
api
```




- [apps](https://docs.github.com/en/free-pro-team@latest/rest/reference/apps)
- [oauth-authorizations](https://docs.github.com/en/free-pro-team@latest/rest/reference/oauth-authorizations)
- [codes-of-conduct](https://docs.github.com/en/free-pro-team@latest/rest/reference/codes-of-conduct)
- [emojis](https://docs.github.com/en/free-pro-team@latest/rest/reference/emojis)
- [enterprise-admin](https://docs.github.com/en/free-pro-team@latest/rest/reference/enterprise-admin)
- [billing](https://docs.github.com/en/free-pro-team@latest/rest/reference/billing)
- [activity](https://docs.github.com/en/free-pro-team@latest/rest/reference/activity)
- [gists](https://docs.github.com/en/free-pro-team@latest/rest/reference/gists)
- [gitignore](https://docs.github.com/en/free-pro-team@latest/rest/reference/gitignore)
- [issues](https://docs.github.com/en/free-pro-team@latest/rest/reference/issues)
- [licenses](https://docs.github.com/en/free-pro-team@latest/rest/reference/licenses)
- [markdown](https://docs.github.com/en/free-pro-team@latest/rest/reference/markdown)
- [meta](https://docs.github.com/en/free-pro-team@latest/rest/reference/meta)
- [orgs](https://docs.github.com/en/free-pro-team@latest/rest/reference/orgs)
- [actions](https://docs.github.com/en/free-pro-team@latest/rest/reference/actions)
- [interactions](https://docs.github.com/en/free-pro-team@latest/rest/reference/interactions)
- [migrations](https://docs.github.com/en/free-pro-team@latest/rest/reference/migrations)
- [projects](https://docs.github.com/en/free-pro-team@latest/rest/reference/projects)
- [repos](https://docs.github.com/en/free-pro-team@latest/rest/reference/repos)
- [teams](https://docs.github.com/en/free-pro-team@latest/rest/reference/teams)
- [reactions](https://docs.github.com/en/free-pro-team@latest/rest/reference/reactions)
- [rate-limit](https://docs.github.com/en/free-pro-team@latest/rest/reference/rate-limit)
- [checks](https://docs.github.com/en/free-pro-team@latest/rest/reference/checks)
- [code-scanning](https://docs.github.com/en/free-pro-team@latest/rest/reference/code-scanning)
- [git](https://docs.github.com/en/free-pro-team@latest/rest/reference/git)
- [pulls](https://docs.github.com/en/free-pro-team@latest/rest/reference/pulls)
- [scim](https://docs.github.com/en/free-pro-team@latest/rest/reference/scim)
- [search](https://docs.github.com/en/free-pro-team@latest/rest/reference/search)
- [users](https://docs.github.com/en/free-pro-team@latest/rest/reference/users)



Then we can explore the endpoints provided by the API in each group, e.g. for the `git` group:

```python
api.git
```




- [create_blob](https://docs.github.com/rest/reference/git#create-a-blob)
- [get_blob](https://docs.github.com/rest/reference/git#get-a-blob)
- [create_commit](https://docs.github.com/rest/reference/git#create-a-commit)
- [get_commit](https://docs.github.com/rest/reference/git#get-a-commit)
- [list_matching_refs](https://docs.github.com/rest/reference/git#list-matching-references)
- [get_ref](https://docs.github.com/rest/reference/git#get-a-reference)
- [create_ref](https://docs.github.com/rest/reference/git#create-a-reference)
- [update_ref](https://docs.github.com/rest/reference/git#update-a-reference)
- [delete_ref](https://docs.github.com/rest/reference/git#delete-a-reference)
- [create_tag](https://docs.github.com/rest/reference/git#create-a-tag-object)
- [get_tag](https://docs.github.com/rest/reference/git#get-a-tag)
- [create_tree](https://docs.github.com/rest/reference/git#create-a-tree)
- [get_tree](https://docs.github.com/rest/reference/git#get-a-tree)



Here's how to learn about an endpoint you want to use, e.g.:

```python
api.git.get_ref
```




[git/get_ref](https://docs.github.com/rest/reference/git#get-a-reference)(ref, repo, owner): *Get a reference*



In Jupyter Notebook full tab completion, parameter lists, etc are provided for all endpoints. Endpoints are called as standard Python methods:

```python
api.git.get_ref(owner='fastai', repo='fastcore', ref='heads/master')
```




- ref: refs/heads/master
- node_id: MDM6UmVmMjI1NDYwNTk5OnJlZnMvaGVhZHMvbWFzdGVy
- url: https://api.github.com/repos/fastai/fastcore/git/refs/heads/master
- object: 
  - sha: 0b188e9a4f200c5ad93c692bb10aa6e7ceb10d4c
  - type: commit
  - url: https://api.github.com/repos/fastai/fastcore/git/commits/0b188e9a4f200c5ad93c692bb10aa6e7ceb10d4c



For access to authenticated endpoints, pass a [GitHub token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token). You can also pass any parameters you want auto-inserted into relevant methods, such as `owner` and `repo`:

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
  - sha: 0b188e9a4f200c5ad93c692bb10aa6e7ceb10d4c
  - type: commit
  - url: https://api.github.com/repos/fastai/fastcore/git/commits/0b188e9a4f200c5ad93c692bb10aa6e7ceb10d4c



Now that we've provided our token, we can use authenticated endpoints such as creating an issue:

```python
issue = api.issues.create("Remember to check out GhApi!")
```

Since we've now checked out GhApi, let's close this issue. 😎

```python
api.issues.update(issue.number, state='closed')
```
