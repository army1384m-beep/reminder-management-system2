from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from ID_generator import id_generator

class BaseReminder(ABC):
    
    @abstractmethod
    def remind(self) -> str:
        pass

@dataclass
class Reminder(BaseReminder):
    title: str
    time: str
    id_reminder: int = field(init=False)
    
    def __post_init__(self):
        self.id_reminder = id_generator.generate_id()
    
    @abstractmethod
    def remind(self) -> str:
        pass