class Queue():
    """A basic implementation of a Queue data structure"""
    
    def __init__(self):
        """Create an empty queue"""
        self.myQueue = []
        
    def insert(self, e):
        """Puts an element into the queue"""
        self.myQueue.append(e)
        
    def remove(self):
        """Removes an element from the queue"""
        try:
            newList = []
            for i in range(1, len(self.myQueue)):
                newList.append(self.myQueue[i])
            a = self.myQueue[0]
            self.myQueue = newList
            return a  
        except:
            raise ValueError()   
                    