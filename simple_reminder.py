from dataclasses import dataclass, field
from .ID_generator import id_generator  

@dataclass
class SimpleReminder:
    
    title: str  
    time: str   
    id_reminder: int = field(init=False)  
    def __post_init__(self):
        self.id_reminder = id_generator.generate_id()
    
    def remind(self) -> str:
        return f"It is time: {self.title}"
    
    def __str__(self) -> str:
        return f"SimpleReminder: {self.title}"