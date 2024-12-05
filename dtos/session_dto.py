from dataclasses import dataclass


@dataclass
class SessionDTO:
    session_id: str
    user_id: int
    