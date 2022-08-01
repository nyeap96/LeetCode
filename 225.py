import queue

class MyStack:
    # okay so queus are last in first out while stacks are first in last out
    # so for this you have two queues everytime you wnat to insert into a queue what you do is insert into the empty queue first
    # then pop everything out of your other queue and insert into the queue
    
    # okay so its actually difficult to do this because then i can't update my top value correctly
    # so maybe we'll only do the queue switch when it is demanded which is when popping the values
    
    # okay actually the best is to use q1 as a sort of intermediary instead
    # if we push we first just push to q1
    # then if we push again and something is in q1 we take that and push to q2
    def __init__(self):
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()
        self.qTop = []
    def push(self, x: int) -> None:
        self.qTop.append(x)
        if self.q1.empty() == True:
            self.q1.put(x)
            while self.q2.empty() == False:
                temp = self.q2.get()
                self.q1.put(temp)
        else:
            self.q2.put(x)
            while self.q1.empty() == False:
                temp = self.q1.get()
                self.q2.put(temp)
        return
    
    def pop(self) -> int:
        if self.q1.empty() == True:
            temp = self.q2.get()
        else:
            temp = self.q1.get()
        
        self.qTop.pop()
        return temp
    
    def top(self) -> int:
            return self.qTop[len(self.qTop) - 1]
        
    def empty(self) -> bool:
        return self.q1.empty() and self.q2.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()