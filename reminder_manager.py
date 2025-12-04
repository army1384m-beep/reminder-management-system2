import logging
import re
import datetime

class ReminderManager:
    def __init__(self):
        self.reminders = {}
        self._setup_logger()  
        self.logger.info("Reminder management system launched")
    
    def _setup_logger(self):
        self.logger = logging.getLogger('reminder_system')
        self.logger.setLevel(logging.DEBUG)
        
        if self.logger.handlers:
            return
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_format = logging.Formatter('%(levelname)s → %(message)s')
        console_handler.setFormatter(console_format)
        self.logger.addHandler(console_handler)
        
        file_handler = logging.FileHandler('reminder.log', mode='a', encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_format = logging.Formatter(
            '%(asctime)s - %(levelname)s → %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(file_format)
        self.logger.addHandler(file_handler)
    
    def _validate_time_format(self, time_str: str) -> bool:
        pattern = r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$'
        return bool(re.match(pattern, time_str))
    
    def add_reminder(self, reminder):
        if not reminder.title or reminder.title.strip() == "":
            self.logger.error("Add reminder failed: empty title")
            return False
        
        if not reminder.time or reminder.time.strip() == "":
            self.logger.error("Add reminder failed: empty time")
            return False
        
        if not self._validate_time_format(reminder.time.strip()):
            self.logger.error(f"Add reminder failed: invalid time format '{reminder.time}'. Use HH:MM")
            return False
        
        self.reminders[reminder.id_reminder] = reminder
        self.logger.info(f"Reminder added - ID: {reminder.id_reminder}")
        return True
    
    def remove_reminder(self, reminder_id):
        if reminder_id in self.reminders:
            del self.reminders[reminder_id]
            self.logger.warning(f"Reminder deleted - ID: {reminder_id}")
            return True
        self.logger.warning(f"Reminder with ID {reminder_id} not found")
        return False
    
    def list_reminders(self):
        self.logger.info(f"Reminders list - number: {len(self.reminders)}")
        return list(self.reminders.values())
    
    def get_reminder_by_id(self, reminder_id):
        reminder = self.reminders.get(reminder_id)
        if reminder:
            self.logger.info(f"Reminder found - ID: {reminder_id}")
        else:
            self.logger.warning(f"Reminder with ID {reminder_id} not found")
        return reminder
    
    def execute_all(self):
        self.logger.info("Start running all reminders")
        results = []
        
        for reminder_id, reminder in self.reminders.items():
            try:
                result = reminder.remind()
                results.append(result)
                self.logger.info(f"Reminder executed - ID: {reminder_id}")
            except Exception as e:
                error_msg = f"Error executing reminder {reminder_id}: {str(e)}"
                results.append(error_msg)
                self.logger.error(error_msg)
        
        self.logger.info(f"End of execution - {len(results)} reminder executed")
        return results