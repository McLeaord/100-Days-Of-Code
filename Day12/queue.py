class Queue:

	def __init__(self):
		self.elements = []

	def enqueue(self, data):
		self.elements.append(data)
		return data

	def dequeue(self):
		return self.elements.pop(0)

	def rear(self):
		return self.elements[-1]

	def front(self):
		return self.elements[0]

	def is_empty(self):
		return len(self.elements) == 0

if __name__ == '__main__':
	queue = Queue()

	

queue.enqueue("apple")
queue.enqueue("banana")
queue.enqueue("mango")
queue.enqueue("orange")
queue.enqueue("grapes")

	

print(queue.front())
print(queue.rear())

queue.dequeue()
    
    
print(queue.dequeue())

	