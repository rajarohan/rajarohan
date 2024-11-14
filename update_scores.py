import requests
from bs4 import BeautifulSoup

def fetch_leetcode_score(username):
    url = f"https://leetcode.com/RajaRohan_Reddy/"
    response = requests.get(url)
    score = "1000"  # Placeholder: Add parsing code to extract the score
    return score

def fetch_codechef_rating(username):
    url = f"https://www.codechef.com/users/raja_rohan21"
    response = requests.get(url)
    rating = "1500"  # Placeholder: Add parsing code to extract the rating
    return rating

def fetch_hackerrank_score(username):
    url = f"https://www.hackerrank.com/profile/2203a52126"
    response = requests.get(url)
    score = "1200"  # Placeholder: Add parsing code to extract the score
    return score

def update_readme(leetcode_score, codechef_rating, hackerrank_score):
    with open("README.md", "r") as file:
        content = file.readlines()

    updated_content = []
    for line in content:
        if "LeetCode Score" in line:
            line = f"LeetCode Score: {leetcode_score}\n"
        elif "CodeChef Rating" in line:
            line = f"CodeChef Rating: {codechef_rating}\n"
        elif "HackerRank Score" in line:
            line = f"HackerRank Score: {hackerrank_score}\n"
        updated_content.append(line)

    with open("README.md", "w") as file:
        file.writelines(updated_content)

leetcode_score = fetch_leetcode_score("your_leetcode_username")
codechef_rating = fetch_codechef_rating("your_codechef_username")
hackerrank_score = fetch_hackerrank_score("your_hackerrank_username")

update_readme(leetcode_score, codechef_rating, hackerrank_score)
