# firestore-http
This is an example for using Firestore via HTTP for cases where the client lib is not available like [in my case](https://stackoverflow.com/questions/55563432/cannot-get-firestore-quickstart-to-work-in-python).

# Google REST API Reference
https://cloud.google.com/firestore/docs/reference/rest/

# Google REST API Explorer
https://developers.google.com/apis-explorer/#search/firestore/firestore/v1/

## Requirements
* Python 3
* The JSON file for the service account. The [Quickstart](https://cloud.google.com/firestore/docs/quickstart-servers#set_up_authentication) describes how to create it. Add it as `auth.json` to the root of this repo. It is already added to `.gitignore`

## Installation
```
virtualenv --python python3 env
source env/bin/activate
pip3 install -r requirements.txt
```

## Run
``` 
./test.sh
```

## Exit virtualenv
``` 
deactivate
```
