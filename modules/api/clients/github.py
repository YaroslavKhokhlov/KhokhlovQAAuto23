import requests


class Github:
    def get_user(self, username):
        r = requests.get(f"https://api.github.com/users/{username}")
        body = r.json()

        return body

    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories",
            params={"q": name}
        )
        body = r.json()

        return body
    
    def search_emojis(self):
        r = requests.get("https://api.github.com/emojis")
        body = r.json()
        
        return body

    def user_block (self, username):
        r = requests.put(f"https://api.github.com/user/blocks/{username}")
        body = r.json()
       
        return body
    
    def limit_check (self):
        r=requests.get(" https://api.github.com/rate_limit")
        body = r.json()

        return body
  
