import requests
from bs4 import BeautifulSoup
import re

def fetch_leetcode_score(username):
    url = f"https://leetcode.com/{username}/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Look for the score in the page. Adjust the selector based on the actual HTML structure.
        # Here, we assume the total solved problems appear in an element with class name like 'total-solved-count'
        score_element = soup.find("div", {"class": "total-solved-count"})
        if score_element:
            return score_element.text.strip()
    return "N/A"  # Fallback if score not found

def update_readme(score):
    with open("README.md", "r+") as file:
        content = file.read()
        # Replace the placeholder with the updated score
        updated_content = re.sub(r"LeetCode Score: <!--LEETCODE_SCORE-->", f"LeetCode Score: {score}", content)
        file.seek(0)
        file.write(updated_content)
        file.truncate()

# Replace 'your_leetcode_username' with your actual LeetCode username
username = "RajaRohan_Reddy"
score = fetch_leetcode_score(username)
update_readme(score)
