from typing import List


class Rectangle:
    """ A rectangle with a width and height. """

    def __init__(self, w: int, h: int) -> None:
        """Create a new rectangle of width w and height h.
        >>> r = Rectangle(1, 2)
        >>> r.width
        1
        >>> r.height
        2
        """

        self.width = w
        self.height = h

    def get_area(self) -> int:
        """Return the area of this rectangle.
        >>> r = Rectangle(10, 20)
        >>> r.get_area()
        200
        """

        return self.width * self.height


class RectangleCollection:

    def __init__(self) -> None:
        """
        >>> rc = RectangleCollection()
        >>> rc.rectangles
        []
        """
        self.rectangles = []

    def add_rectangle(self, rectangle: "Rectangle") -> None:
        """
        >>> rc = RectangleCollection()
        >>> r1 = Rectangle(1,2)
        >>> rc.add_rectangle(r1)
        >>> rc.rectangles
        [r1]
        """

        # your code goes here

    def get_same_area_rects(self, area: int) -> List["Rectangle"]:
        """
        >>> rc = RectangleCollection()
        >>> r1 = Rectangle(1,2)
        >>> r2 = Rectangle(2,2)
        >>> r3 = Rectangle(4,1)
        >>> rc.add_rectangle(r1)
        >>> rc.add_rectangle(r2)
        >>> rc.add_rectangle(r3)
        >>> rc.get_same_area_rects(4)
        [r2,r3]
        """

        results = []

        # your code goes here.

        return results
