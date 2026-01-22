from typing import Optional


class JWTConfigurationError(RuntimeError):
    default = "JWT_SECRET_KEY is not configured"

    def __init__(self, message: Optional[str]):
        super().__init__(message if message else self.default)
