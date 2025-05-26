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

