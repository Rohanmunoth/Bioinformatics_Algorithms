import sys
import random 

# Please do not remove package declarations because these are used by the autograder.

# Insert your randomized_motif_search function here, along with any subroutines you need
def randomized_motif_search(dna: list[str], k: int, t: int) -> list[str]:
    bestMotif = None
    output = None
    for i in range(1000):
        k_mers = [random.randint(0, len(dna[j]) - k) for j in range(t)]
        motif = [dna[j][k_mers[j]:k_mers[j] + k] for j in range(t)]
        bestMotif = motif
        while True:
            profile = profile_generation(motif)
            motif = [profile_most_probable_kmer(dna[i], k, profile) for i in range(t)]
            if score(motif) < score(bestMotif):
                bestMotif = motif
            else:
                break
        if output is None or score(bestMotif) < score(output):
            output = bestMotif
    return output

def profile_generation(motif):
    nucleotides = ['A', 'C', 'G', 'T']
    length = len(motif)
    profile = []
    for i in range(len(motif[0])):
        for base in motif:
            if i >= len(base):
                raise Exception(f'The value of i is {i}\n{motif}')
        nucleotides_column = [base[i] for base in motif]
        count = []
        for c in nucleotides:
            nucleotide_count = float((nucleotides_column.count(c) + 1) / (length + 4))
            count.append(nucleotide_count)
        profile.append(count)
    transposed_profile = []
    for i in range(len(profile[0])):
        transposed_count = [profile[j][i] for j in range(len(profile))]
        transposed_profile.append(transposed_count)
    return transposed_profile


def profile_most_probable_kmer(text, k, profile):
    bestKmer = []
    for i in range(len(text) - k + 1):
        k_mer = text[i:i + k]
        score = 1
        for j in range(len(k_mer)):
            checking_dict = {'A': profile[0][j], 'C': profile[1][j], 'G': profile[2][j], 'T': profile[3][j]}
            value = checking_dict[k_mer[j]]
            score *= value
        bestKmer.append(score)
    maximum = max(bestKmer)
    index = bestKmer.index(maximum)
    motif_kmer = text[index:index + k]
    return motif_kmer


def score(motifs):
    score = 0
    for i in range(len(motifs[0])):
        nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            nucleotide_counts[motif[i]] += 1
        score += sum(nucleotide_counts.values()) - max(nucleotide_counts.values())
    return score


def count(sequence1, sequence2):
    if isinstance(sequence1, str) and isinstance(sequence2, str):
        if len(sequence1) == len(sequence2):
            distance = 0
            for i in range(len(sequence1)):
                if sequence1[i] != sequence2[i]:
                    distance += 1
            return distance
    return 0