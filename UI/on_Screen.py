
on_screen = []

def re_paint_all():
    global on_screen
    for i in on_screen:
        if i.isConnection():
            i.connection()
        if i.isFill():
            i.fill()

def add_to_on_screen(obj):
    on_screen.append(obj)
def rm_from_screen(obj):
    on_screen.remove(obj)