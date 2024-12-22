!pip install pygithub
from github import Github
import requests

def check_github_plagiarism(project_text):
    try:
        g = Github("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6M")
        repos = g.search_repositories(query=f'"{project_text}" in:readme in:description')
        return repos.totalCount > 0
    except Exception as e:
        print(f"GitHub API Error: {e}")
        return False

def check_google_plagiarism(project_text):
    try:
        api_key = "NNAIzaSyBJOl-WzZQwu8KiV9gkVbrBjs1Kzi-TFbc"
        cx = "0VV3ef3ee392806488e"
        search_url = f"https://www.googleapis.com/customsearch/v1?q={project_text}&key={api_key}&cx={cx}"
        response = requests.get(search_url)
        results = response.json()
        if 'items' in results:
            return len(results['items']) > 0
        else:
            print("No results found in Google search.")
            return False
    except Exception as e:
        print(f"Google API Error: {e}")
        return False

if __name__ == "__main__":
    project_text = "Example project description"
    github_plagiarism = check_github_plagiarism(project_text)
    google_plagiarism = check_google_plagiarism(project_text)
    print(f"GitHub Plagiarism: {github_plagiarism}, Google Plagiarism: {google_plagiarism}")
