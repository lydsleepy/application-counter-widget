from storage import Storage

class Counter: 
    # manages counter state & logic

    def __init__(self):
        data = Storage.load_data()
        self.total = data['total']
        self.current = data['current']

    def increment(self):
    # increments the current count by 1
    # not limited to the total count
        self.current += 1
        self._save()
        return True
    
    def decrement(self):
    # decrements the current count by 1
        if self.current > 0:
            self.current -= 1
            self._save()
            return True
        return False

    def set_current(self, value):
    # sets current value with validation
        try:
            value = int(value)
            if value >= 0:
                self.current = value
                self._save()
                return True
        except (ValueError, TypeError):
            pass
        return False

    def set_total(self, value):
    # sets total value with validation
        try:
            value = int(value)
            if value >= 0:
                self.total = value
                self._save()
                return True
        except (ValueError, TypeError):
            pass
        return False
    
    def get_remaining(self):
    # calculates remaining count
        return self.total - self.current

    def get_progress_text(self):
    # formatted progress string
        return f"{self.current} / {self.total}"

    def get_remaining_text(self):
    # formatted remaining string
        if remaining > 0:
            return f"{abs(remaining)} OVER THE GOAL!!!"
        elif remaining == 0:
            return "LETS GOOO YOU DID IT!!!"
        elif remaining == 1:
            return "YOU'RE LITERALLY SO CLOSE"
        else:
            return f"{remaining} left, lock tf in"

    def _save(self):
    # save state
        Storage.save_data(self.total, self.current)