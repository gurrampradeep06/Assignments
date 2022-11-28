class DataTypes:
    def Method(self):
        i = 1
        j = 1.1
        k = 923456789023456789092345678902345678909234567890234567890
        l = 'c'
        m = "pradeep"
        n = complex(1,2)
        o = True
        p = None
        print(type(i),type(j),type(k),type(l),type(m),type(o),type(p),n)

        q = 10/9
        r = 9*923456789023456789092345678902345678909234567890234567890
        print(type(r))
        s = 1.1*30
        print(s,type(s))


        print(q)

        #----------------------Set-------------------

        s = set()
        for i in range(10):
            print("enter element")
            s.add(bool(input()))

        print(s)
        s1 = set()
        s1.add(True)
        s1.add(False)
        print(s1)

        if(True):
            pass







if __name__ == "__main__":
    obj1 = DataTypes()
    obj1.Method()
