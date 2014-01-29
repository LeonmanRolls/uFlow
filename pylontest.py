class arguments:
        argone = ''
        argtwo = ''
        argthree = ''

class internalData:
        internalone = 'internalone'
        internaltwo = ''

def argConcat(argone,argtwo):
        print (argone + argtwo)

def internalConcat(internalone):
        print (internalone)
        internaltwo = 'internaltwo'
        return locals()

def allConcat(argone,argtwo,internalone,internaltwo):
        print (argone + argtwo + internalone + internaltwo)
