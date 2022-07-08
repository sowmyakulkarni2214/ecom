e=42
h="i am sowmya my age is {1}{2}{0}"
print(h)
print(h.format(e,'nandana',10))

class Image:
    url='sdsibdsibisg'
    def imageurl(self):
        try:
            url=self.url
            print(url)
        except:
            url='not given'
            print(url)
    @classmethod
    def changeurlnow(cls,changeurl):
        print(Image.url)
        Image.url=changeurl

I = Image()
I.imageurl()
change=Image.changeurlnow('sowmya')
print(change)

a=Image()
a.imageurl()

try:
    obj=Person.objects.get(name='sowmay', age='42')
except:Person.DoesNotExist
    obj=Person.objects(name='sowmya',age='42')
    Person.save()

order,created = Person.objects.get_or_create(name='sowmya', age='42')

