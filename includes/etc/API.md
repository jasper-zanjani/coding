!!! info "Resources"

    **API endpoints**

    I've found a few interesting API endpoints for consumption.

    -   **https://swapi.info/api**: apparently forked from [phalt/swapi](https://github.com/phalt/swapi) which has gone unmaintained for years
    -   **https://pokeapi.co/api/v2**: recommended by the author of swapi
    -   [**https://api.toys/api**](https://api.toys/api/index) has various endpoints: /api/dice_roll, /api/rock_paper_scissors, etc.
    -   **https://api.thecatapi.com/v1/images/search** cat images

    Curated lists of public apis:
    
    -   [Public APIs](https://publicapis.dev)

    **Tutorials**

    - Real Python
        -   [Python & APIs: a winning combo for reading public data](https://realpython.com/python-api/)
        -   [Raining Outside? Build a Weather CLI App With Python](https://realpython.com/build-a-python-weather-app-cli/)


#### Basic API call

=== ":material-language-python: requests"

    ```py
    import requests

    requests.get('https://api.thecatapi.com/').text # '{"message":"The Cat API","version":"1.3.9"}'
    ```

=== ":material-bash: curl"

    ```sh
    curl -X GET \
        https://api.thecatapi.com/
    ```


<div class="grid cards" markdown>

-   #### Basic authentication

    **Basic authentication** supplies the username and password in a string of the form `username:password` encoded in BASE64.
    Public API keys associated with a user account would also be used in this way.
    This encoded string is then passed in an authorization header with the content "Basic" followed by the encoded string.
    For example the string "username:password" itself is encoded as "dXNlcjpwYXNzd29yZAo=". (1)
    { .annotate }

    1. 
    ```py
    --8<-- "includes/py/base64-encode.py"
    ```

    The TrueNAS API supports a utility method at **/core/ping** which returns "pong".

    === ":material-language-python: requests"

        ```py
        import requests

        res = requests.get('http://truenas.local/api/v2.0/core/ping',auth=(user,password))
        res.text # 'pong'
        ```

    === ":material-bash: curl"

        ```sh
        curl -X GET \
            -H 'accept: application/json' \
            -H 'Authorization: Basic YWRtaW46amFuZGo=' \
            'http://truenas.local/api/v2.0/core/ping'
        ```

-   #### Key-based authentication

    API keys are often accepted in the **Authorization** header.

    In this example, the TrueNAS endpoint accepts the API key only after "Bearer" (capitalized), and not "Token" as is often the case with other APIs.

    === ":material-language-python: requests"

        ```py
        import requests # (1)

        headers = { "Authorization": f"Bearer {api_key}"}
        res = requests.get('http://truenas.local/api/v2.0/core/ping',headers)
        ```

        1. Using [**python-dotenv**](https://github.com/theskumar/python-dotenv) to protect the API key.
        ```py
        --8<-- "includes/py/python-dotenv.py"
        ```

    === ":material-bash: curl"

        ```sh
        curl -X GET \
            -H 'accept: application/json' \
            -H "Authorization: Bearer $API_KEY" \
            'http://truenas.local/api/v2.0/core/ping' 
        ```

</div>

### AI

#### Ollama

```py
import requests
import json

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json',
}

data = {
    "model": "llama2:7b",
    "prompt": "Why is the sky blue?"
}

res = requests.post(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)

```

#### Utilities

-   [hurl](https://github.com/Orange-OpenSource/hurl) is a tool that allows API calls to be tested from the command-line by using text files defining the expected contents of responses
