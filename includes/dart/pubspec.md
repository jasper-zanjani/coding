Dart's manifests, where project dependencies are specified, are called [pubspec files](https://dart.dev/tools/pub/pubspec) and named **pubspec.yaml**.
A package's dependencies can be resolved using the **dart** command. (1)
{: .annotate }

1.  

    ```sh
    --8<-- "includes/cmd/dart/dart-pub-get.sh"
    ```

<!-- -->

-   SDK constraints indicate a dependency on the Dart platform itself, called SDK constraints (1)
    {: .annotate }

    1.  

        ```yaml
        --8<-- "includes/dart/pubspec/sdk-constraints.yaml"
        ```

