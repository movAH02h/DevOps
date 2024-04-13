from project.generate_password import generate, service, username

def store_password(service, username, password):
    if username == "user123" and service == "example.com":
        if (password != "111"):
            return "store has been done"
        else:
            return "password absolutely wrong"
    else:
        return "failed operation"


def retrieve_password(service, username):
    if username == "user123" and service == "example.com":
        return "complete retrieve"
    else:
        return "retrieve failed"



def delete_password(service, username):
    if service == "user123" and username == "example.com":
        return "successful delete"
    else:
        return "wrong user or name of service"



# Generate a new password
new_password, hashed_password = generate()

# Store the password
store_password(service, username, hashed_password)

# Retrieve the password
retrieve_password(service, username)

# Delete the password
delete_password(service, username)