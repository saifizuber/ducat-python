'''
inner class
special class is in the lang class
'''

class lang:
    x='python'
    def show(self):
        print('my lang is ', self.x)
    class special:
        def show2(self):
            print('python is dynamic lang')
            print('python is a mathematic lang')
            print('python is a interpreter')


k=lang()
k.show()
k2=k.special()
k2.show2()


#-------------------------------------------------------------
class lang:
    x='python'
    def show(self):
        if(self.x=='python'):
            print('python is a dynamic language')
    class special:
        def show2(self):
            print('python is high level lang')

            print('python is a interpreter nase language')

        class xyz:
            def show3(self):
                print('hello')


k=lang()
k.show()
k2=k.special()
k2.show2()
k3=k2.xyz()
k3.show3()