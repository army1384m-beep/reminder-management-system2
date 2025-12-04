class ReminderAnalytics:
    def get_stats(self, reminders):
        stats = {"total": len(reminders), "types": {}}
        
        for r in reminders:
            type_name = r.__class__.__name__
            stats["types"][type_name] = stats["types"].get(type_name, 0) + 1
        
        return stats
    
    def show_stats(self, stats):
        print("=== Statistics ===")
        print(f"Total: {stats['total']}")
        for t, count in stats['types'].items():
            print(f"{t}: {count}")
