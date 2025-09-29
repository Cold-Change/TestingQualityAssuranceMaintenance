import requests
import json

def main():
    github_api("richkempinski") # Provided example repository
    # github_api("Cold-Change") # My repository

def github_api(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Now 'data' contains the JSON response as a Python object
        print("-" * 45)
        for repo in data:
            commits_url = repo['commits_url'][:-6]
            commits_response = requests.get(commits_url)
            commits_data = commits_response.json()
            print(f"Repo: {repo['name']}   Commits: {len(commits_data)}")
            print("-" * 45)
    else:
        print(f"Failed to retrieve data.")

if __name__ == "__main__":
    main()