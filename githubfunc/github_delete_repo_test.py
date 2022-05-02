import requests
import os
import json

token = os.environ.get("GITHUB_TOKEN")

reponame = input("Please enter the repo name you want to delete : ")
username = input("Please enter your GitHub username: ")

GITHUB_API_URL = "https://api.github.com/"
headers = {"Authorization": "token {}".format(token)}
data = {"name": "{}".format(reponame)}

r = requests.delete("https://api.github.com/repos/{}/{}".format(username, reponame), headers=headers)
print(r)