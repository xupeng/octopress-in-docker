Octopress in Docker
-------------------

octopress-in-docker is a helper utility for using octopress in docker, which is for anyone who was struggling for maintaining an environment for octopress, with docker it's much easier than ever before.

octopress-in-docker consisits of two parts, a docker image (xupeng/octopress) and a helper script for easier usage, you need Python, pip and docker to use it.

How?

```
pip install git+https://github.com/xupeng/octopress-in-docker.git#egg=octopress-in-docker
```

Suppose your octopress source is in directory `/octopress` (`$OCTOPRESS`), then you can run any octopress supported commands with `oid`, which is the helper script for easier docker usage, for example:

```
oid -r $OCTOPRESS rake generate
```

to generate HTML files, and

```
oid -r $OCTOPRESS rake preview
```

for live preview and there is a HTTP service listening on port 4000.

Please run `oid --help` for further information, and keep http://octopress.org/ as reference.
