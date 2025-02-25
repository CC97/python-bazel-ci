load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "rules_python",
    url = "https://github.com/bazelbuild/rules_python/releases/download/0.23.0/rules_python-0.23.0.tar.gz",
    strip_prefix = "rules_python-0.23.0",
    sha256 = "b8c3d8cc50f9b4dc2ba7c26b6df2387396137b17ed5f6199092da2ec07e6f2ab",
)

load("@rules_python//python:repositories.bzl", "py_repositories")
py_repositories()
