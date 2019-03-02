class Dates():
    def __init__(self):
        self.list = []

    def add(self, date):
        self.list.append(date)

    def find(self, d):
        for date in self.list:
            print(date.date)
            if date.date == d:
                return date
        return None

class Date():
    def __init__(self, date, guard = False):
        self.date = date
        self.guard_on_duty = guard
        self.entries = []

    def add_entry(self, dt):
        self.entries.append(dt)

class Guards():
    def __init__(self):
        self.list = []

    def add(self, guard):
        self.list.append(guard)

    def find(self, id):
        for guard in self.list:
            if guard.id == id:
                return guard
        return None

class Guard():
    instances = []

    def __init__(self, id):
        self.id = id
        Guard.instances.append(self)

    def __str__(self):
        return self.id
