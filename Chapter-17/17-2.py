class Kangaroo():
    def __init__(self,pouch_contents=None):
        if pouch_contents is None:
            self.pouch_contents=[]
        else:
            self.pouch_contents=[pouch_contents]
    def put_in_pouch(self,other): # we are just modifying, don't need return value
        if isinstance(other,Kangaroo):
            self.pouch_contents.extend(other.pouch_contents)
        else:
            self.pouch_contents.extend(other)


    def __str__(self):
        return f"{self.pouch_contents}"
kanga=Kangaroo(6)
roo=Kangaroo(["n",7])
kanga.put_in_pouch(roo)

print(kanga)
print(roo)
