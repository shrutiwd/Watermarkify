# Add Watermark to an Image

# install pillow library from cmd
# Import pillow library
# PIL - Python Imaging Library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class Watermark:
    
    ''' A class to represent the working of watermark '''
    
    def __init__(self, input_path, output_path, text, pos, text_color, size):
        
        ''' Intializing instance variables '''
        
        self.input_path = input_path
        self.output_path = output_path
        self.text = text
        self.pos = pos
        self.text_color = text_color
        self.size = size

    def wat_mark(self):
        
        ''' Allows the user to add the watermark in the desired image '''

        # Open the image path given by the user
        img = Image.open(self.input_path)

        # Add the functionalities
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(r"D:\Python full stack development\CSS\font\SinkinSans-700BoldItalic.otf", self.size)
        draw.text(self.pos,self.text, self.text_color, font)
        img.show()
        img.save(self.output_path)

# Taking inputs from the user
input_path = input("Enter the image path with image name: ")
text = input("Enter the text that should display in the image: ")
text_color = input("Enter the color of the text: ")
pos = (int(input("Enter x coordinate: ")), int(input("Enter y coordinate: ")))
print("Position: ", pos)
size = int(input("Enter the size of the text: "))
output_path = input("Enter the path in which the image should get saved with image name: ") 

# calling the method
w = Watermark(input_path, output_path, text, pos, text_color, size)
w.wat_mark()
