# Release new packages 

- Set up the new functionality and commits. Travis will run the tests to ensure that the build works as expected. This may include bumping the dependencies with poetry update.
- Once everything is ready, create a new commit with the new version information. This normally includes:
    - Run poetry version {patch|minor|major|...} to bump the version. 
    ```poetry version 0.x.x```
    - Set up any manual changes, like release notes, documentation updates or internal version references.
- Commit/push and verify that the build is green in travis.
- Create a new tag (or GitHub release) with the version. Remember to push the tag to GitHub.

```git tag -a v1.4 -m "my version 1.4"```

and 

```git push --follow-tags```

- Travis will upload the new version automatically to PyPI.


## References
[poetry build](https://wrongsideofmemphis.com/2018/10/28/package-and-deploy-a-python-module-in-pypi-with-poetry-tox-and-travis/)

[git tags](https://git-scm.com/book/en/v2/Git-Basics-Tagging) 
[push tags](https://stackoverflow.com/questions/5195859/how-do-you-push-a-tag-to-a-remote-repository-using-git)
