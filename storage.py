import json
import os
from config import CONFIG_FILE, DEFAULT_CURRENT, DEFAULT_TOTAL

class Storage:
    # handles saving and loading counter data

    @staticmethod
    # loads the counter data from json file
    def load_data():
        if os.path.exists(CONFIG_FILE):
            try:
                with open(CONFIG_FILE, 'r') as f:
                    data = json.load(f)
                    return {
                        'total': data.get('total', DEFAULT_TOTAL),
                        'current': data.get('current', DEFAULT_CURRENT)
                    }
            except (json.JSONDecodeError, IOError):
                return {
                    'total': DEFAULT_TOTAL,
                    'current': DEFAULT_CURRENT
                }
        else:
            return {
                'total': DEFAULT_TOTAL,
                'current': DEFAULT_CURRENT
            }
        
    @staticmethod
    def save_data(total, current):
    # saves the counter data to a json file
        try:
            with open(CONFIG_FILE, 'w') as f:
                json.dump({'total': total, 'current': current}, f, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")