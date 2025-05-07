import requests

# Replace this with the actual file link from Google Drive/Dropbox/OneDrive
file_url = "https://drive.google.com/file/d/1YuFAxzqVklSk06LSA8mSrOA6QSQlAODm/view?usp=sharing"

local_path = "abc.zip"

response = requests.get(file_url)
if response.status_code == 200:
    with open(local_path, "wb") as f:
        f.write(response.content)
    print("Folder downloaded successfully!")
else:
    print("Failed to download. Check the URL or permissions.")
