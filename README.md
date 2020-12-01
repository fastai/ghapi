# GhApi
> A delightful and complete interface to GitHub's amazing API


`GhApi` provides 100% always-updated coverage of the entire [GitHub API](https://docs.github.com/en/free-pro-team@latest/rest). Because we automatically convert the [OpenAPI spec](https://docs.github.com/en/free-pro-team@latest/rest/overview/openapi-description) to a Pythonic API, `GhApi` is always up to date with the latest changes to GitHub APIs. Furthermore, because this is all done dynamically, the entire package is only 35kB in size!

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

```
1+1
```




    2



We recommend reading the documentation on the [official site](https://ghapi.fast.ai/), rather than on GitHub, since not all the functionality described on this page is available through the GitHub viewer.

All of the documentation is available directly as Jupyter Notebooks, for instance the current page you're reading is available as a notebook [here](https://github.com/fastai/ghapi/blob/master/index.ipynb). To open any page as an interactive notebook in Google Colab, click the *Colab* badge at the top of the page.

To access the GitHub API, first create a `GhApi` object:

```
api = GhApi()
```

Every part of the API includes documentation directly in the `api` object itself. For instance, here's how to explore the groups of functionality provided by the API by displaying the object:

```
api
```




- [actions](https://docs.github.com/en/free-pro-team@latest/rest/reference/actions)
- [activity](https://docs.github.com/en/free-pro-team@latest/rest/reference/activity)
- [apps](https://docs.github.com/en/free-pro-team@latest/rest/reference/apps)
- [billing](https://docs.github.com/en/free-pro-team@latest/rest/reference/billing)
- [checks](https://docs.github.com/en/free-pro-team@latest/rest/reference/checks)
- [code_scanning](https://docs.github.com/en/free-pro-team@latest/rest/reference/code_scanning)
- [codes_of_conduct](https://docs.github.com/en/free-pro-team@latest/rest/reference/codes_of_conduct)
- [emojis](https://docs.github.com/en/free-pro-team@latest/rest/reference/emojis)
- [enterprise_admin](https://docs.github.com/en/free-pro-team@latest/rest/reference/enterprise_admin)
- [gists](https://docs.github.com/en/free-pro-team@latest/rest/reference/gists)
- [git](https://docs.github.com/en/free-pro-team@latest/rest/reference/git)
- [gitignore](https://docs.github.com/en/free-pro-team@latest/rest/reference/gitignore)
- [interactions](https://docs.github.com/en/free-pro-team@latest/rest/reference/interactions)
- [issues](https://docs.github.com/en/free-pro-team@latest/rest/reference/issues)
- [licenses](https://docs.github.com/en/free-pro-team@latest/rest/reference/licenses)
- [markdown](https://docs.github.com/en/free-pro-team@latest/rest/reference/markdown)
- [meta](https://docs.github.com/en/free-pro-team@latest/rest/reference/meta)
- [migrations](https://docs.github.com/en/free-pro-team@latest/rest/reference/migrations)
- [oauth_authorizations](https://docs.github.com/en/free-pro-team@latest/rest/reference/oauth_authorizations)
- [orgs](https://docs.github.com/en/free-pro-team@latest/rest/reference/orgs)
- [projects](https://docs.github.com/en/free-pro-team@latest/rest/reference/projects)
- [pulls](https://docs.github.com/en/free-pro-team@latest/rest/reference/pulls)
- [rate_limit](https://docs.github.com/en/free-pro-team@latest/rest/reference/rate_limit)
- [reactions](https://docs.github.com/en/free-pro-team@latest/rest/reference/reactions)
- [repos](https://docs.github.com/en/free-pro-team@latest/rest/reference/repos)
- [scim](https://docs.github.com/en/free-pro-team@latest/rest/reference/scim)
- [search](https://docs.github.com/en/free-pro-team@latest/rest/reference/search)
- [teams](https://docs.github.com/en/free-pro-team@latest/rest/reference/teams)
- [users](https://docs.github.com/en/free-pro-team@latest/rest/reference/users)



Then we can explore the endpoints provided by the API in each group, e.g. for the `git` group:

```
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

```
api.git.get_ref
```




[git.get_ref](https://docs.github.com/rest/reference/git#get-a-reference)(owner, repo, ref): *Get a reference*



In Jupyter Notebook full tab completion, parameter lists, etc are provided for all endpoints. Endpoints are called as standard Python methods:

```
api.git.get_ref(owner='fastai', repo='fastcore', ref='heads/master')
```




- ref: refs/heads/master
- node_id: MDM6UmVmMjI1NDYwNTk5OnJlZnMvaGVhZHMvbWFzdGVy
- url: https://api.github.com/repos/fastai/fastcore/git/refs/heads/master
- object: 
  - sha: 28721554e0eab1f2974237c502912f8ba42a44a0
  - type: commit
  - url: https://api.github.com/repos/fastai/fastcore/git/commits/28721554e0eab1f2974237c502912f8ba42a44a0



For access to authenticated endpoints, pass a [GitHub token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token). You can also pass any parameters you want auto-inserted into relevant methods, such as `owner` and `repo`:

```
api = GhApi(owner='fastai', repo='fastcore', token=github_token)
```

We can now repeat the previous method, but only need to pass `ref`:

```
api.git.get_ref('heads/master')
```




- ref: refs/heads/master
- node_id: MDM6UmVmMjI1NDYwNTk5OnJlZnMvaGVhZHMvbWFzdGVy
- url: https://api.github.com/repos/fastai/fastcore/git/refs/heads/master
- object: 
  - sha: 28721554e0eab1f2974237c502912f8ba42a44a0
  - type: commit
  - url: https://api.github.com/repos/fastai/fastcore/git/commits/28721554e0eab1f2974237c502912f8ba42a44a0



Now that we've provided our token, we can use authenticated endpoints such as creating an issue:

```python
issue = api.issues.create("Remember to check out GhApi!")
```

Since we've now checked out GhApi, let's close this issue. 😎

```python
api.issues.update(issue.number, state='closed')
```

## Tab completion

You can enable tab completion for `ghapi` by placing the following command at the end of your `~/.bashrc` or `~/.zshrc` file:

```bash
eval "$(completion-ghapi --install)"
```
