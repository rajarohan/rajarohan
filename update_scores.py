import requests
import re

def fetch_leetcode_score(username):
    url = f"https://leetcode-stats-api.herokuapp.com/RajaRohan_Reddy"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("totalSolved", "N/A")  # Modify based on the actual key in the API response
    return "N/A"

def update_readme(score):
    with open("README.md", "r+") as file:
        content = file.read()
        # Replace the placeholder with the updated score
        updated_content = re.sub(r"LeetCode Score: <!--LEETCODE_SCORE-->", f"LeetCode Score: {score}", content)
        file.seek(0)
        file.write(updated_content)
        file.truncate()

# Replace 'your_leetcode_username' with your actual LeetCode username
username = "your_leetcode_username"
score = fetch_leetcode_score(username)
update_readme(score)
