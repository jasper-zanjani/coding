!!! info "Installation"

    Installation of the [Dart Sass executable](https://github.com/sass/dart-sass/) is rather strange.
    The tarball contains a **sass** executable (shell script) and a **src** directory which **must accompany** the script.
    The src directory contains a version of the Dart executable as well as an [AOT snapshot](https://dart.dev/tools/dartaotruntime), a precompiled Dart application.

    If the script is not able to find the correct prebundled version of Dart, the version of Dart present on the system will throw an error mentioning "dartaotruntime", a binary which is no longer included with the Dart SDK.
