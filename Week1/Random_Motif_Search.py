# Please do not remove package declarations because these are used by the autograder.

# Insert your profile_most_probable_kmer function here, along with any subroutines you need.

def profile_most_probable_kmer(text: str, k: int,
                               profile: list[dict[str, float]]) -> str:
    bestScore=0
    bestKmer=None
    for i in range(len(text)-k+1):
        k_mer=text[i:i+k]
        score=1
        for j in range (len(k_mer)):
            checking_dict=profile[j]
            value=checking_dict[k_mer[j]]
            score*=value
        if (score>bestScore):
            bestScore=score
            bestKmer=k_mer
          
    return bestKmer
    """Identifies the most probable k-mer according to a given profile matrix.

    The profile matrix is represented as a list of columns, where the i-th element is a map
    whose keys are strings ("A", "C", "G", and "T") and whose values represent the probability
    associated with this symbol in the i-th column of the profile matrix.
    """