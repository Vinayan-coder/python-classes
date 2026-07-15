class Point:
    def __init__(self,x=0,y=0):
            self.x = 4
            self.y = 5   
    def reset (self):
          self.x = 0
          self.y = 0
    def move (self,a,b):
          self.x = a
          self.y = b
p1 = Point()
print(p1.x,p1.y)
p1.reset()
print(p1.x,p1.y)
p1.move()
print(p1.x,p1.y)

