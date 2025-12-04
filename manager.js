class ReminderManager {
    constructor() {
        this.reminders = [];
    }
    
    add(reminder) {
        this.reminders.push(reminder);
    }
    
    list() {
        return this.reminders;
    }
}
module.exports = ReminderManager;
