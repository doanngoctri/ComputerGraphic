from Class.Form import Form

class Retangle(Form):
    def __init__(self,*args):
        first = [args[0],args[1]]
        self.points = []
        self.points.append(first)
        second = [args[0],args[3]]
        self.points.append(second)
        third = [args[2],args[3]]
        self.points.append(third)
        fourth = [args[2],args[1]]
        self.points.append(fourth)
        super().find_mid()