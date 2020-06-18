from UI.graphic import root,view_menu,color_background
from Class.Retangle import Retangle
from Class.Circle import Circle
from Pixel.colour import get_inverse_color


def create_ret():
    re = Retangle(10, 10, 30, 30)
    re.scaling(2)
    re.reflection_x()
    global color_background
    re.connection("#00cc00")
    re.fill("#00cc00")
from Class.Circle import Circle
view_menu.add_command(label = "Retangle",command=create_ret)
# ci = Circle(10,10,20)
# ci.connection()
# ci.fill("blue")
# ci.connection()

#root.mainloop()