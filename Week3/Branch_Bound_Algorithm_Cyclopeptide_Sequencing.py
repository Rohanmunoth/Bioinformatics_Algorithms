import copy
def CyclopeptideSequencing(spectrum):
    finalPeptideString=''
    finalPeptide=[]
    candidatePeptides=[]
    spectrum=convertSpectrum(spectrum)
    peptideLength=numberOfPeptides(spectrum)
    mass_values={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y': 163,'W': 186}
    for i in range (1,peptideLength+1):
        for j in mass_values:
            if (mass_values[j]==spectrum[i]):
                candidatePeptides.append(j)
    singlePeptides=copy.deepcopy(candidatePeptides)
    while candidatePeptides!=[]:
        candidatePeptides=expand(candidatePeptides,singlePeptides)
        checkCandidates=copy.deepcopy(candidatePeptides)
        for peptide in checkCandidates:
            if linearMassScore(peptide,spectrum):
                if (Cyclospectrum(peptide)==spectrum and peptide not in finalPeptide):
                    finalPeptide.append(peptide)
                    candidatePeptides.remove(peptide)
            else:
                candidatePeptides.remove(peptide)
    finalPeptide=convert(finalPeptide,mass_values)
    for i in finalPeptide:
        finalPeptideString+=i+' '
    return finalPeptideString[:-1]

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
    count=0
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

def numberOfPeptides(spectrum):
    peptideLength=None
    spectrumLength=len(spectrum)
    for i in range(spectrumLength):
        if ((i*(i-1))+2==spectrumLength):
            peptideLength=i
            break
    return peptideLength

m='0 87 99 113 113 115 115 128 131 131 156 212 218 227 228 228 241 243 246 262 271 327 340 340 349 356 358 359 374 377 384 453 455 455 464 471 483 487 489 490 505 568 568 570 577 586 602 611 618 620 620 683 698 699 701 705 717 724 733 733 735 804 811 814 829 830 832 839 848 848 861 917 926 942 945 947 960 960 961 970 976 1032 1057 1057 1060 1073 1073 1075 1075 1089 1101 1188'
print(CyclopeptideSequencing(m))
#print(CyclopeptideSequencing('0 87 87 113 113 114 128 131 137 163 163 200 200 201 224 242 244 250 287 291 294 314 326 329 337 337 381 401 405 407 424 442 450 454 457 468 492 529 537 538 544 568 570 581 585 605 631 651 655 666 668 692 698 699 707 744 768 779 782 786 794 812 829 831 835 855 899 899 907 910 922 942 945 949 986 992 994 1012 1035 1036 1036 1073 1073 1099 1105 1108 1122 1123 1123 1149 1149 1236'))