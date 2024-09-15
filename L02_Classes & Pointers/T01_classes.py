# A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
# Every data structure that we are going to create, is going to be created using classes


class Cookie:

    def __init__(self, color) -> None:
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print(f"Cookie one is '{cookie_one.get_color()}'")
print(f"Cookie two is '{cookie_two.get_color()}'")

cookie_one.set_color('yellow')

print(f"\nCookie one is now '{cookie_one.get_color()}'")
print(f"Cookie two is still '{cookie_two.get_color()}'")
