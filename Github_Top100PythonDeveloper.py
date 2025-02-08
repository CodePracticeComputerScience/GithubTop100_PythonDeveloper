import requests
import pandas as pd

# GitHub API setup
access_token = '---'  # Use GitHub OAuth token
base_url = 'https://api.github.com/search/users'

# Search for Python developers
params = {
    'q': 'language:Python',  # Search query: Python language
    'per_page': 1000,  # Limit to 1000 results
    'sort': 'followers',  # Sort by most followers
}

headers = {
    'Authorization': f'Bearer {access_token}'
}

response = requests.get(base_url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    users = data['items']

    # Prepare the data for DataFrame
    user_data = []
    for user in users:
        user_data.append({
            'Name': user['login'],
            'Profile': user['html_url']
        })
    
    # Create a DataFrame
    df = pd.DataFrame(user_data)
    
    # Save to Excel
    df.to_excel('github_python_developers.xlsx', index=False)
    print("Data saved to 'github_python_developers.xlsx'")
else:
    print(f"Error: {response.status_code}, {response.text}")
