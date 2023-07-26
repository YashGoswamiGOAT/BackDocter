def concatinateList(lis1,lis2):
    res_ = []
    for obj in lis1:
        res_.append(obj)
    for obj in lis2:
        res_.append(obj)
    return res_

def Filter(data,maindata):
    if type(data)==type("string") and type(maindata)==type("string"):
        return data==maindata
    elif type(data)==type(1) and type(maindata)==type(1):
        return data==maindata
    elif type(data)==type([]) and type(maindata)==type([]):
        return_ = False
        allReturn = []
        for elem in data:
            for mainelem  in maindata:
                return_ = Filter(elem,mainelem)
                if return_:
                    allReturn.append(True)
        return len(allReturn)==len(data)
    elif type(data)==type({}) and type(maindata)==type({}):
        return_ = True
        for elem in data.keys():
            if elem not in maindata.keys():
                return_ = False
            else:
                if return_ == True:
                    return_ = Filter(data[elem],maindata[elem])
        return return_
    elif type(data)==type(lambda x:x):
        if type(maindata) == type("string"):
            return data(maindata)
            return data == maindata
        elif type(maindata) == type(1):
            return data(maindata)
        elif type(maindata) == type([]):
            return_ = True
            for mainelem in maindata:
                if data(mainelem) and Filter(data(),mainelem):
                    if return_!=False:
                        return_ = True
                else:
                    return_ = False
            return return_
        # Testing Purpose
        elif type(maindata) == type({}):
            return_ = True
            for elem0 in maindata.keys():
                if return_:
                    return_ = data([elem0,maindata[elem0]])
            for elem in data().keys():
                if elem not in maindata.keys():
                    return_ = False
                else:
                    if return_ == True and data([elem,maindata[elem]]):
                        return_ = Filter(data()[elem], maindata[elem])
            return return_
    else:
        return False