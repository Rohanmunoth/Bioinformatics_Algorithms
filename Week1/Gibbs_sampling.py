import sys 
import random

# Please do not remove package declarations because these are used by the autograder.

# Insert your gibbs_sampler function here, along with any subroutines you need
def gibbs_sampler(dna: list[str], k: int, t: int, n: int) -> list[str]:
    best_score = float('inf')
    best_motifs = []
    for _ in range(20):
        motifs = random_motifs(dna, k, t)
        for j in range(n):
            i = random.randint(0, t-1)
            motifs.pop(i)
            profile = profile_generation(motifs, k)
            motifs.insert(i, profile_most_probable_kmer(dna[i], k, profile))
            current_score = score(motifs)
            if current_score < best_score:
                best_score = current_score
                best_motifs = motifs[:]
    return best_motifs

def random_motifs(dna, k, t):
    return [random_kmer(seq, k) for seq in dna]

def random_kmer(seq, k):
    start = random.randint(0, len(seq) - k)
    return seq[start:start+k]

def profile_generation(motifs, k):
    profile = [[1 for _ in range(k)] for _ in range(4)]
    for string in motifs:
        for index in range(len(string)):
            nucleotide = string[index]
            profile["ACGT".index(nucleotide)][index] += 1
    for i in range(len(profile)):
        for j in range(len(profile[i])):
            profile[i][j] = profile[i][j] / len(motifs)
    return profile

def profile_most_probable_kmer(text, k, profile):
    max_prob = -1
    kmer = text[0:k]
    for i in range(len(text) - k + 1):
        prob = 1
        pattern = text[i:i+k]
        for j in range(k):
            nucleotide = pattern[j]
            prob *= profile["ACGT".index(nucleotide)][j]
        if prob > max_prob:
            max_prob = prob
            kmer = pattern
    return kmer

def score(motifs):
    score = 0
    k = len(motifs[0])
    for i in range(k):
        frequency_map = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for motif in motifs:
            frequency_map[motif[i]] += 1
        score += sum(frequency_map.values()) - max(frequency_map.values())
    return score

