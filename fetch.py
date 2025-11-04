import os

def fetch_url(url):
    """
    Function to fetch the content of a URL using curl
    """
    command = f"curl {url}"
    os.system(command)

if __name__ == "__main__":
    user_input = input("Enter a URL to fetch: ")
    fetch_url(user_input)
