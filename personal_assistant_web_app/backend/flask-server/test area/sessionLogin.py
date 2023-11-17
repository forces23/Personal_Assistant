import requests

# Set the login page URL and the credentials
login_url = 'https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fbard.google.com%2Fchat%3Fhl%3Den&ec=GAZAkgU&followup=https%3A%2F%2Fbard.google.com%2Fchat%3Fhl%3Den&hl=en&ifkv=AVQVeyyeCZdt8J7Gi8GQHtKH4zRBVlH2dcejVAZzlEieOFnn04vXbcIAqNrjRPFu54DrgQl6Dt4S7g&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1292534524%3A1700109429695414&theme=glif'
login_payload = {
    'username': 'bobby.lawson17@gmail.com',
    'password': 'undercoveranon2023'
}

# Create a session to persist the login state
with requests.Session() as session:
    # Send a GET request to the login page to get any necessary cookies or tokens
    response = session.get(login_url)

    # Extract any required tokens or cookies from the response (if needed)

    # Send a POST request to the login endpoint with the credentials
    response = session.post(login_url, data=login_payload)

    print(f"resp text: {response.text}")
    # Check if the login was successful (you may need to inspect the response)
    if 'Login successful' in response.text:
        print('Login successful')
    else:
        print('Login failed')

    # Now, you can use the session object for subsequent requests, and it will maintain the login state
    # For example, you can make requests to other pages that require authentication
    # response = session.get('https://example.com/dashboard')