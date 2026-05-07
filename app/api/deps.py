from fastapi import Depends, HTTPException

from app.core.security import oauth2_scheme, decode_token


def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_token(token)
    return payload


def role_required(allowed_roles: list):
    def checker(current_user: dict = Depends(get_current_user)):
        role = current_user.get("role")

        if role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="Access denied"
            )

        return current_user

    return checker