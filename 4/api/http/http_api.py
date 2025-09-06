import requests

def main():
    # GET request
    response = requests.get("https://github.com/tebellomaila/")
    print(response.status_code)     # 200 created
    print(response.json())      # Returns Response content as JSON

    # POST request
    new_post = { "title": "foo", "body": "bar", "userId": 1 }
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json = new_post)
    print(response.status_code)     # 201 created

    # With headers and authentication
    headers = {"Authorization": "Bearer YOUR_TOKEN"}
    response = requests.get("https://api.example.com/data", headers = headers)


if __name__ == "__main__":
    main()
