import copy
def spectralConvolution(spectrum):
    spectrum = convert(spectrum)
    copySpectrum=copy.deepcopy(spectrum)
    resultingList=[]
    for i in spectrum:
        for j in copySpectrum:
            values=i-j
            if (values>0):
                resultingList.append(values)
    resultingList=covertList(resultingList)
    return resultingList

def covertList(spectrum):
    result=''
    for i in spectrum:
        result+=str(i)+' '
    return result


def convert (spectrum):
    spectrum= spectrum+' '
    newSpectrum=[]
    m=''
    for i in spectrum:
        if (i==' '):
            newSpectrum.append(int(m))
            m=''
        else:
            m+=i
    return newSpectrum

m='0 137 186 323'

print(spectralConvolution(m))