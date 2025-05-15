# Overview

Flutter (1) is an open-source UI toolkit for creating native mobile applications.
{: .annotate }

1.  === "Resources"

        -   Flutter Docs
            -   [Start building Flutter native desktop apps on Linux](https://docs.flutter.dev/get-started/install/linux/desktop)

        -   [Solido/awesome-flutter](https://github.com/Solido/awesome-flutter)
        -   [antz22/ultimate-guide-to-flutter](https://github.com/antz22/ultimate-guide-to-flutter)
        -   [Zaiste Programming :material-youtube: - Flutter in Practice](https://www.youtube.com/playlist?list=PLhXZp00uXBk5TSY6YOdmpzp1yG3QbFvrN)


    === "Installation"

        -   Install from Google:
            -   [Flutter SDK](https://docs.flutter.dev/get-started/install/linux/desktop)
            -   [Android Studio](https://developer.android.com/studio/index.html)

                -   Install "Android SDK Command-line Tools" from Settings > Android SDK > SDK Tools

        -   Enable hardware VM acceleration by installing KVM

        -   Other dependencies

            === ":material-fedora: Fedora"

                ```sh
                dnf install -y clang cmake gtk3-devel ninja-build pkg-config
                ```

        -   Verify installation with `flutter doctor`

    === "Command reference"

        --8<-- "includes/cmd/flutter/flutter.md"

---

Dart (1)
Valid Dart [project names](https://dart.dev/tools/pub/pubspec#name) are alphanumeric and in [snake case](https://en.wikipedia.org/wiki/Snake_case).
{: .annotate }

1.  === "Resources"

        -   [Dart Docs](https://dart.dev/language)

    === "Command reference"

        --8<-- "includes/cmd/dart/dart.md"

#### Packaging

The Dart ecosystem uses the pub package manager to find and publish packages.
