class Print:
    def draw(self):
        print('drawing')
    
    def sketch(self):
        print('sketching')

object1 = Print()
object1.x = 10
print(object1.x)
# object1.draw()
# object1.sketch()