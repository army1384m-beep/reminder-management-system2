class IdGenerator:
    
    def __init__(self):
        self.next_id = 1  
    
    def generate_id(self) -> int:
        current_id = self.next_id
        self.next_id += 1 
        return current_id


id_generator = IdGenerator()