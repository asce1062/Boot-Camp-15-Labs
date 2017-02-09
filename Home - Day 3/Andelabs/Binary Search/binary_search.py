class BinarySearch(list):
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

        for i in range(self.a):
            list.append(self, self.b)
            self.b += b

        self.length = self.a

    def search(self, value):
        start = 0
        count = 0
        end = self.length - 1
        found = False
        in_list = False
        try:
            index = self.index(value)
            in_list = True
        except ValueError:
            index = -1
            in_list = False

        while start <= end and not found and in_list and value != self[end]:
            midpoint = (start + end) // 2
            mid_value = self[midpoint]
            if mid_value == value:
                found = True
                count += 1
                index = midpoint
            else:
                if value < mid_value:
                    end = midpoint - 1
                    count += 1
                else:
                    start = midpoint + 1
                    count += 1

        return {"count": count, "index": index}
