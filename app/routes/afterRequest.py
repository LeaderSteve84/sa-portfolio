#!/usr/bin/env python3
"""After request for refresh token"""

from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token, get_jwt, \
    get_jwt_identity, set_access_cookies


def refresh_expiring_jwts(response):
    """refresh jwt that are expiring"""
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=30))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        # Case where there is not a valid JWT.
        # Just return the original response
        return response
