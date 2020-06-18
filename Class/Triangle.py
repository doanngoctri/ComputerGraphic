from Class.Form import Form

class Triangle(Form):
    def __init__(self,*args):
        super().__init__(*args)
        super().find_mid()