from dataclasses import dataclass


@dataclass
class UserDTO:
    name: str
    mobile_number: str
    password: str
