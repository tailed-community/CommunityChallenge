import requests
from urllib.parse import urlparse

def convert_to_raw_url(github_url: str) -> str:
    """
    Converts a GitHub file URL to the raw content URL.
    """
    if "github.com" not in github_url or "/blob/" not in github_url:
        raise ValueError("URL must be a GitHub file link containing '/blob/'")

    parts = github_url.replace("https://github.com/", "").split("/blob/")
    repo_part = parts[0]  # user/repo
    file_part = parts[1]  # branch/path/to/file.py

    raw_url = f"https://raw.githubusercontent.com/{repo_part}/{file_part}"
    return raw_url

def fetch_github_file(github_url: str) -> str:
    """
    Fetches the raw content of a file from GitHub.
    """
    raw_url = convert_to_raw_url(github_url)
    response = requests.get(raw_url)
    response.raise_for_status()  # Raise an error for 4xx/5xx responses
    return response.text

if __name__ == "__main__":
    github_file_url = input("Enter GitHub file URL: ").strip()
    try:
        content = fetch_github_file(github_file_url)
        print("\n--- FILE CONTENT START ---\n")
        print(content)
        print("\n--- FILE CONTENT END ---\n")
    except Exception as e:
        print(f"Error: {e}")