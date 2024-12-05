from dataclasses import dataclass


@dataclass
class CarDTO:
    name: str
    model: str
    price: int
    mileage: int
    body_type: str
    power: int
    disk_radius: int
    transmission_type: str
    drive_type: str
    engine_type: str
    volume: float
    color: str