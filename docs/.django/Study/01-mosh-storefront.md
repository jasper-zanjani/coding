# Mosh's Storefront

Creating new views (i.e. request handlers) such that we can return a response at a specified route.

-   First a stub view function is created, which will return a `HttpResponse` object. (1)
    {: .annotate }

    1.  

        ```py title="playground/views.py" hl_lines="5-6"
        --8<-- "includes/django/mosh-storefront/01/playground/views.py"
        ```


-   Then the file **urls.py** (1) is created and the view function is associated with the specified route by creating a list named "urlpatterns".
    Note that the views module is imported from the current module.
    The `path` function returns a `URLPattern`.
    {: .annotate }

    1.  

        ```py title="playground/urls.py"
        --8<-- "includes/django/mosh-storefront/01/playground/urls.py"
        ```


-   This then has to be added to the main URLConf for the project. (1)
    {: .annotate }

    1.  

        ```py title="storefront/urls.py" hl_lines="22"
        --8<-- "includes/django/mosh-storefront/01/storefront/urls.py"
        ```

A more elaborate response using HTML can be implemented by creating a new **templates** directory with a new template file (1) and then implementing the view function with `render` (2).
{: .annotate }

1.  

    ```html title="playground/templates/hello.html"
    --8<-- "includes/django/mosh-storefront/02/playground/templates/hello.html"
    ```

2.  

    ```py hl_lines="2 6" title="playground/views.py"
    --8<-- "includes/django/mosh-storefront/02/playground/views.py"
    ```


