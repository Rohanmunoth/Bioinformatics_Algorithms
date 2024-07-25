import copy

def ConvolutionCyclopeptideSequencing(M,N,spectrum):
    compareSpectrum=copy.deepcopy(convertConvolution(spectrum))
    spectrum=spectralConvolution(spectrum)
    mass_values=dict()
    finalCount=dict()
    finalPeptides=[]
    count=[]
    m=65
    occurrance=dict()
    for i in range (57,201):
        mass_values[chr(m)]=i
        m+=1
    for i in spectrum:
        if (i>=57 and i<=200):
            if i not in occurrance:
                occurrance[i]= spectrum.count(i)
                count.append(spectrum.count(i))
    count.sort()
    count=count[::-1]
    #print(count)
    for j in range (M,len(count)-1):
        if count[j]<count[M-1]:
            count=count[:j]
            break
    for i in occurrance:
        if occurrance[i] not in finalCount:
            finalCount[occurrance[i]]=[i]
        else:
            finalCount[occurrance[i]].append(i)
    for i in set(count):
        for j in finalCount[i]:
            #print(j)
            finalPeptides.append(j)
    return leaderBoardCycloPeptideSequencing(finalPeptides,N,compareSpectrum)

def spectralConvolution(spectrum):
    spectrum = convertConvolution(spectrum)
    copySpectrum=copy.deepcopy(spectrum)
    resultingList=[]
    for i in spectrum:
        for j in copySpectrum:
            values=i-j
            if (values>0):
                resultingList.append(values)
    #resultingList=covertList(resultingList)
    return resultingList

def covertList(spectrum):
    result=''
    for i in spectrum:
        result+=str(i)+' '
    return result


def convertConvolution(spectrum):
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

def leaderBoardCycloPeptideSequencing(aminoAcids, N,spectrum):
    leaderBoard=[] #LFAE 
    leaderPeptideString=''
    #spectrum=convertSpectrum(spectrum)
    m=65
    mass_values=dict()
    for i in range (57,201):
        mass_values[chr(m)]=i
        m+=1
    for i in aminoAcids:
        for j in mass_values:
            if (i==mass_values[j]):
                leaderBoard.append(j)
    singlePeptides=copy.deepcopy(leaderBoard)
    while leaderBoard!=[]:
        leaderBoard=expand(leaderBoard,singlePeptides)
        m=copy.deepcopy(leaderBoard)
        for peptide in m:
            if score(peptide)<=spectrum[-1]:
                if linearMassScore(peptide,spectrum)>linearMassScore(leaderPeptideString,spectrum):
                    leaderPeptideString=peptide
            elif score(peptide)>spectrum[-1]:
                leaderBoard.remove(peptide)
        leaderBoard=trim(leaderBoard,spectrum,N)
    #print(linearMassScore(leaderPeptideString,spectrum),linearMassScore('LFAE',spectrum))
    leaderPeptideString=convert(leaderPeptideString,mass_values)
    m=''
    for i in leaderPeptideString:
        m+=i+'-'
    leaderPeptideString=m    
    return leaderPeptideString[:-1]

def trim(leaderBoard, spectrum, N):
    finalList=[]
    linearScoresList=[]
    linearScores=dict()
    newDict=dict()
    for j in range (len(leaderBoard)):
        peptide= leaderBoard[j]
        linearScores[peptide]=linearMassScore(peptide,spectrum)
        linearScoresList.append(linearScores[peptide])
    linearScoresList=sorted(linearScoresList)
    linearScoresList=linearScoresList[::-1]
    for i in linearScores:
        if (linearScores[i] not in newDict):
            newDict[linearScores[i]]=[]
            newDict[linearScores[i]].append(i)
        else:
            newDict[linearScores[i]].append(i)
    for j in range (N,len(linearScoresList)-1):
        if linearScoresList[j]<linearScoresList[N-1]:
            linearScoresList=linearScoresList[:j]
            break
    for i in linearScoresList:
        finalList.append(newDict[i])
    leaderBoard=[]
    for i in finalList:
        while i!=[]:
            leaderBoard.append(i.pop())
    return leaderBoard
       
def convert(finalPeptide,massValues):
    finalSet=[]
    m=''
    for i in finalPeptide:
        for j in i:
            m+=str(massValues[j])+'-'
        m=m[:-1]
        finalSet.append(m)
        m=''
    return (finalSet)

def linearMassScore(g,m):
    spectrum=copy.deepcopy(m)
    theoreticalSpectrum= linearSpectrum(g)
    experimentalSpectrum = spectrum
    count=0
    for i in theoreticalSpectrum:
        spectrum=experimentalSpectrum
        for j in spectrum:
            if (i==j):
                count+=1
                experimentalSpectrum.remove(j)
                break
    return count


def linearSpectrum(g):
    final=[]
    c=1
    scores=[]
    for i in range (len(g)):
        for j in range (len(g)):
            if (j+c<len(g)+1):
                m=g[j:j+c]
                if (len(m)!=len(g)):
                    final.append(m)
        c+=1
    (final.append(g))
    for i in final:
        scores.append(score(i))
    scores=[0]+scores
    scores=sorted(scores)
    return scores

def Cyclospectrum(g):
    final=[]
    c=1
    scores=[]
    for i in range (len(g)):
        for j in range (len(g)):
            if ((j+c)<len(g)):
                m=g[j:j+c]
            else:
                m=g[j:]+g[:(j+c-len(g))]
            if (len(m)!=len(g)):
                final.append(m)
        c+=1
    (final.append(g))
    for i in final:
        scores.append(score(i))
    scores=[0]+scores
    scores=sorted(scores)
    return scores

def score(string):
    scores=0
    mass_values=dict()
    m=65
    for i in range (57,201):
        mass_values[chr(m)]=i
        m+=1
    for i in string:
        scores+=mass_values[i]
    return scores

def expand(candidatePeptides,peptides):
    newCandidates=[]
    m=''
    for i in candidatePeptides:
        for j in peptides:
            m=i+j
            newCandidates.append(m)
            m=''
    return newCandidates

def convertSpectrum(spectrum):
    spectrumList=[]
    s=''
    for i in spectrum:
        if (i==' '):
            spectrumList.append(int(s))
            s=''
        else:
            s+=i
    spectrumList.append(int(s))
    return spectrumList


m="0 87 87 97 101 103 103 113 128 128 129 131 186 190 200 214 215 216 216 226 232 234 256 273 303 313 314 317 329 331 335 343 344 345 376 401 404 416 432 441 442 448 448 460 472 489 504 529 529 535 544 545 547 551 561 569 590 616 617 632 638 648 648 658 672 674 675 718 719 721 735 745 745 755 761 776 777 803 824 832 842 846 848 849 858 864 864 889 904 921 933 945 945 951 952 961 977 989 992 1017 1048 1049 1050 1058 1062 1064 1076 1079 1080 1090 1120 1137 1159 1161 1167 1177 1177 1178 1179 1193 1203 1207 1262 1264 1265 1265 1280 1290 1290 1292 1296 1306 1306 1393"
print(ConvolutionCyclopeptideSequencing(20,398,m))