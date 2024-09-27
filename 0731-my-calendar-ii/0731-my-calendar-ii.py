def helper(s, e, b): 
    o = 0
    for i in b:
        if (s < i[1] and e > i[0]):
            o += 1
            if (o >= 2):
                return 1
    return 0

class MyCalendarTwo:

    def __init__(self):
        self.b = []  
    def book(self, start: int, end: int) -> bool:
        for i in self.b:
            if (start < i[1] and end > i[0]):  
                st = max(i[0], start)
                en = min(i[1], end)
                if (helper(st, en, self.b)):
                    return False

        self.b.append((start, end))
        return True
