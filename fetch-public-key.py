import requests
import json
import sys

def main():
    args = sys.argv
    del args[0]
    for id in sys.argv:
        printkey(id)
        print()

def printkey(githubid):
    endpoint = "https://api.github.com"
    request  = "/users/" + githubid + "/keys"
    response = requests.get(endpoint + request)

    if (response.ok):
        result = json.loads(response.content)
        for key in result:
            print("%s key from Github user %s (ID %s)" %
                  (key["key"], githubid, key["id"]))
    else:
        print("Error connecting to " + endpoint + ": status " + response.raise_for_status())

if __name__== "__main__":
      main()
      
