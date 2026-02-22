
class Counter:
    def __init__(self):
        self.value = 1

    def count_up(self):
        self.value += 1
    
    def count_down(self):
        self.value -= 1
    
    def __str__(self):
        return f"Counter = {self.value}"
    
    def __add__(self, other): #It looks to whetever is on the right side of operation
        return self.value + other.value

def main():
    count1 = Counter()
    count2 = Counter()

    count1.count_up()
    count2.count_down()

    print(count1, count2)
    print(count1 + count2)

if __name__=="__main__":
    main()

