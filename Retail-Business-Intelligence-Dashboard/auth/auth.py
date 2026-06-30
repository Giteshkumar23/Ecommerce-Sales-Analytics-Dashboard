import pandas as pd
import bcrypt
import os

USERS_FILE = "auth/users.csv"


# ===========================
# Load Users
# ===========================

def load_users():

    if not os.path.exists(USERS_FILE):

        return pd.DataFrame(
            columns=[
                "full_name",
                "email",
                "mobile",
                "username",
                "password"
            ]
        )

    return pd.read_csv(USERS_FILE)


# ===========================
# Save Users
# ===========================

def save_users(df):

    df.to_csv(
        USERS_FILE,
        index=False
    )


# ===========================
# Register User
# ===========================

def register_user(
    full_name,
    email,
    mobile,
    username,
    password
):

    users = load_users()

    if username in users["username"].values:
        return False, "Username already exists."

    if email in users["email"].values:
        return False, "Email already registered."

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    new_user = pd.DataFrame([{

        "full_name": full_name,

        "email": email,

        "mobile": mobile,

        "username": username,

        "password": hashed_password

    }])

    users = pd.concat(
        [users, new_user],
        ignore_index=True
    )

    save_users(users)

    return True, "Registration Successful."


# ===========================
# Login
# ===========================

def login_user(
    username,
    password
):

    users = load_users()

    user = users[
        users["username"] == username
    ]

    if user.empty:

        return False

    stored_password = user.iloc[0]["password"]

    return bcrypt.checkpw(

        password.encode(),

        stored_password.encode()

    )