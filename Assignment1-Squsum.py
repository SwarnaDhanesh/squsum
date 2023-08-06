class Point:
 def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
 def sqSum(self):
       self.x=x**2
       self.y=y**2
       self.z=z**2      
       sum=0
       for i in x,y,z:  
        sum +=self.x+self.y+self.z
        return sum
x,y,z=[1,3,5]
SSum=Point(x,y,z)
print(SSum.sqSum())