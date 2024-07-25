import copy
def leaderBoardCycloPeptideSequencing(spectrum, N):
    leaderBoard=[] #LFAE 
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


m='0 71 97 97 97 101 103 103 113 113 114 115 115 115 128 129 131 137 156 163 186 186 186 194 194 206 210 212 216 230 234 243 244 251 257 259 264 268 285 287 291 299 300 301 301 307 309 319 335 340 341 349 362 372 381 382 388 400 402 404 406 413 415 416 437 437 438 450 450 464 469 475 478 487 491 495 503 505 516 519 521 528 530 534 535 552 563 565 566 568 575 592 601 604 606 619 625 631 634 636 647 650 650 661 663 666 667 672 681 683 689 722 728 732 734 737 738 749 751 751 762 764 769 776 778 778 786 787 790 796 798 819 825 831 840 847 852 864 865 869 875 891 893 901 901 907 911 915 918 922 925 928 932 937 944 955 967 972 982 990 996 1002 1008 1019 1025 1029 1032 1033 1035 1041 1044 1050 1051 1054 1063 1070 1079 1087 1087 1105 1111 1125 1130 1133 1134 1138 1138 1145 1153 1158 1164 1166 1176 1182 1188 1200 1202 1202 1215 1226 1227 1231 1240 1242 1246 1251 1253 1256 1267 1269 1273 1297 1301 1303 1314 1317 1319 1324 1328 1330 1339 1343 1344 1355 1368 1368 1370 1382 1388 1394 1404 1406 1412 1417 1425 1432 1432 1436 1437 1440 1445 1459 1465 1483 1483 1491 1500 1507 1516 1519 1520 1526 1529 1535 1537 1538 1541 1545 1551 1562 1568 1574 1580 1588 1598 1603 1615 1626 1633 1638 1642 1645 1648 1652 1655 1659 1663 1669 1669 1677 1679 1695 1701 1705 1706 1718 1723 1730 1739 1745 1751 1772 1774 1780 1783 1784 1792 1792 1794 1801 1806 1808 1819 1819 1821 1832 1833 1836 1838 1842 1848 1881 1887 1889 1898 1903 1904 1907 1909 1920 1920 1923 1934 1936 1939 1945 1951 1964 1966 1969 1978 1995 2002 2004 2005 2007 2035 2036 2040 2042 2049 2051 2054 2065 2067 2075 2079 2083 2092 2095 2101 2106 2120 2120 2132 2133 2133 2154 2155 2157 2164 2166 2168 2170 2182 2188 2189 2198 2208 2221 2229 2230 2235 2251 2261 2263 2269 2269 2270 2271 2279 2283 2285 2302 2306 2311 2313 2319 2326 2327 2336 2340 2354 2358 2360 2364 2376 2376 2384 2384 2384 2407 2414 2433 2439 2441 2442 2455 2455 2455 2456 2457 2457 2467 2467 2469 2473 2473 2473 2499 2570'
print(leaderBoardCycloPeptideSequencing(m,169))