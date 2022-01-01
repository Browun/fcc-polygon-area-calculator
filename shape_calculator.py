class Rectangle:
    def __init__(self, width: int, height: int):
        self.width: int = width
        self.height: int = height

    def set_width(self, width: int):
        '''Set the width property of the Rectangle.'''
        self.width = width

    def set_height(self, height: int):
        '''Set the height property of the Rectangle.'''
        self.height = height

    def get_area(self):
        '''Returns: width * height.'''
        return self.width * self.height

    def get_perimeter(self):
        '''Returns: 2 * width + 2 * height'''
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        '''Returns: (width ** 2 + height ** 2) ** .5'''
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        '''
        Returns a string representing the shape of the Rectangle. Comprised of "*" matching the width and height, returning "Too big for picture." if width/height is > 50.
        '''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        return ''.join("*" * self.width + "\n" for n in range(0, self.height))

    def get_amount_inside(self, shape: "Rectangle" or "Square"):
        '''
        Returns the number of times the inputted shape fits in to the current instance of Rectangle, with no rotations.
        '''
        width_times: int = self.width // shape.width
        height_times: int = self.height // shape.height

        if width_times > 0 and height_times > 0:
            return width_times * height_times

        return max(width_times, height_times)

    def __str__(self):
        '''
        Returns the string representation of the Rectangle instance, with it's given width and height.
        '''
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

    def set_width(self, size):
        self.set_side(size)

    def set_height(self, size):
        self.set_side(size)

    def set_side(self, size: int):
        '''
        Sets the size of the sides for the Square, leveraging the inherited set_width and set_height methods of the Rectangle class.
        '''
        self.width = size
        self.height = size

    def __str__(self):
        '''
        Returns the string representation of the Rectangle instance, with it's given width and height.
        '''
        return f"Square(side={self.width})"
