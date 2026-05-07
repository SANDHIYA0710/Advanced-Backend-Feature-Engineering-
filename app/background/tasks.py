def send_password_reset_email(email: str, token: str):
    print("====================================")
    print(f"Password reset token for: {email}")
    print(token)
    print("====================================")