from dataclasses import dataclass, field
from uuid import UUID, uuid4


@dataclass
class User:
    id: UUID = field(default_factory=uuid4)
    name: str = "Mario"
    surname: str = "Rossi"

    def to_dict(self):
        _dict = self.__dict__.copy()
        _dict["id"] = str(self.id)
        return _dict
