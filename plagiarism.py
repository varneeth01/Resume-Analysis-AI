from github import Github
import requests

def check_github_plagiarism(project_text):
    g = Github("your_github_token")
    repos = g.search_repositories(query=project_text)
    return repos.totalCount > 0

def check_google_plagiarism(project_text):
    api_key = "your_google_api_key"
    cx = "your_search_engine_id"
    search_url = f"https://www.googleapis.com/customsearch/v1?q={project_text}&key={api_key}&cx={cx}"
    response = requests.get(search_url)
    results = response.json()
    return len(results['items']) > 0

project_text = "Example project description"
github_plagiarism = check_github_plagiarism(project_text)
google_plagiarism = check_google_plagiarism(project_text)
print(f"GitHub Plagiarism: {github_plagiarism}, Google Plagiarism: {google_plagiarism}")
