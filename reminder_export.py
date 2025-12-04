import json

class ReminderExporter:
    def to_json(self, reminders):
        data = []
        for r in reminders:
            data.append({
                "id": r.id_reminder,
                "title": r.title,
                "time": r.time,
                "type": r.__class__.__name__
            })
        
        with open('reminders.json', 'w') as f:
            json.dump(data, f, indent=2)
        
        print("Reminders exported to reminders.json")
        return 'reminders.json'
