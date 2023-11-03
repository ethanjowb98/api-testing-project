from dataclasses import dataclass

@dataclass
class AuthDataAssertions:
    AUTH_BAD_REQUEST_KEY = 'reason'
    AUTH_BAD_REQUEST_DATA = 'Bad credentials'
