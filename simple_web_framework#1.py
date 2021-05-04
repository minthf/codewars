class Router(object):
    dict = {}
    
    def bind(self,a,b,f):
        self.dict[a+b] = f
    
    def runRequest(self, a,b):
        try:
            return self.dict[a+b]()
        except KeyError:
            return 'Error 404: Not Found'
            