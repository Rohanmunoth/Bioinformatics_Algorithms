import copy
def leaderBoardCycloPeptideSequencing(spectrum, N):
    leaderBoard=[]
    leaderPeptideString=''
    spectrum=convertSpectrum(spectrum)
    mass_values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y': 163,'W': 186}
    for i in spectrum:
        for j in mass_values:
            if (i==mass_values[j]):
                leaderBoard.append(j)
    singlePeptides=copy.deepcopy(leaderBoard)
    while leaderBoard!=[]:
        leaderBoard=expand(leaderBoard,singlePeptides)
        print(leaderBoard)
        for peptide in leaderBoard:
            if linearMassScore(peptide,spectrum):
                if linearMassScore(peptide,spectrum)>linearMassScore(leaderPeptideString,spectrum):
                    leaderPeptideString=peptide
            elif score(peptide)>spectrum[-1]:
                leaderBoard.remove(peptide)
        leaderBoard=trim(leaderBoard,spectrum,N)
    return leaderBoard


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
        if (i not in newDict):
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
    finalSet=set()
    m=''
    for i in finalPeptide:
        for j in i:
            m+=str(massValues[j])+'-'
        m=m[:-1]
        finalSet.add(m)
        m=''
    return list(finalSet)

def linearMassScore(g,m):
    spectrum=copy.deepcopy(m)
    theoreticalSpectrum= linearSpectrum(g)
    experimentalSpectrum = spectrum
    #print(theoreticalSpectrum)
    #print(experimentalSpectrum)
    count=0
    #print(theoreticalSpectrum,experimentalSpectrum)
    for i in theoreticalSpectrum:
        for j in experimentalSpectrum:
            if (i==j):
                count+=1
                experimentalSpectrum.remove(j)
                break
    return (count==len(theoreticalSpectrum))


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
    mass_values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y': 163,'W': 186}
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

print(leaderBoardCycloPeptideSequencing('0 71 113 129 147 200 218 260 313 331 347 389 460',10))