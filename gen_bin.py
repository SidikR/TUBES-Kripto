def __biner(bilangan) :
    temp = bin(bilangan)
    temp = temp[2:]

    return temp

def __heksa(bilangan) :
    temp = hex(bilangan)
    temp = temp[2:]

    return temp

def __okta(bilangan) :
    temp = oct(bilangan)
    temp = temp[2:]
    return temp

def bin_conv(bilangan) :
    if type(bilangan) == type(int(1)) :
        return __biner(bilangan)
    elif type(bilangan) == type(str("1")) :
        return int(bilangan, 2)

def hek_conv(bilangan) :
    if type(bilangan) == type(int(1)) :
        return __heksa(bilangan)
    elif type(bilangan) == type(str("1")) :
        return int(bilangan.lower(), 16)

def okt_conv(bilangan) :
    if type(bilangan) == type(int(1)) :
        return __okta(bilangan)
    elif type(bilangan) == type(str("1")) :
        return int(bilangan, 8)