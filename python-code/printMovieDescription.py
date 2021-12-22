class Movie:
    def __init__(self,language,character,duration):
        self.language=language
        self.character=character
        self.duration=duration
    def play(self):
        x=("This is a "+self.language+" movie with "+self.character+" characters and is "+self.duration+" minutes long.")
        print(x)
l=input()
ch=input()
du=input()
obj1=Movie(l,ch,du)
obj1.play()