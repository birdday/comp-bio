# TODO: Create Sequence Matrix Class. Use these functions as methods. Avoids continuously passing around same args. 

import numpy as np
import matplotlib.pyplot as plt

def calc_single_score(nuc1, nuc2):
    """Function which calculates the score term for two nucleotides.

    Args:
        nuc1 (str): First nucleotide.
        nuc2 (str): Second nucleotide.

    Returns:
        int: integer value to be added to the i,j term.
    """

    # AGCT x AGCT
    scoring_values = [[ 1,  0, -1, -1],
                      [ 0,  1, -1, -1],
                      [-1, -1,  1,  0],
                      [-1, -1,  0,  1]]
    
    # Convert nucleotides characters to indicies.
    nucleotide_index = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
    ind1 = nucleotide_index[nuc1]
    ind2 = nucleotide_index[nuc2]

    return scoring_values[ind1][ind2]


def calc_score_matrix(seq1, seq2):
    """Generate matrix of scores comparing nucleotides.

    Args:
        seq1 (str): DNA Sequence 1.
        seq2 (str): DNA Sequence 2.

    Returns:
        list[list[ints]]: A 2D matrix of len(seq1) x len(seq2).
    """

    return [[calc_single_score(seq1[i], seq2[j]) for j in range(len(seq2))] for i in range(len(seq1))]

    
def calc_value_matrix(seq1, seq2):
    gap_score = -1
    score_matrix = calc_score_matrix(seq1, seq2)
    value_matrix = [[0 for _ in range(len(seq2))] for _ in range(len(seq1))]

    # This feels sloppy...?
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            # Literal edge cases
            if i == 0 and j == 0:
                value_matrix[i][j] = max(0, score_matrix[i][j])
                continue
            if i == 0:
                value_matrix[i][j] = value_matrix[i][j-1] + gap_score
                continue
            if j == 0:
                value_matrix[i][j] = value_matrix[i-1][j] + gap_score 
                continue

            # Everything else
            value_matrix[i][j] = max(value_matrix[i-1][j] + gap_score,
                                     value_matrix[i-1][j-1] + score_matrix[i][j],
                                     value_matrix[i][j-1] + gap_score
                                     )

    return value_matrix


def print_matrix(seq1, seq2, matrix):
    matT = np.transpose(matrix)
    
    fig, ax = plt.subplots()
    ax.matshow(np.array(matT))
    for (i, j), z in np.ndenumerate(matT):
        ax.text(j, i, '{:0.0f}'.format(z), ha='center', va='center')
    ax.set_xticks([i for i in range(len(seq1))])
    ax.set_xticklabels([char for char in seq1])
    ax.set_yticks([i for i in range(len(seq1))])
    ax.set_yticklabels([char for char in seq1])
    plt.show()

# def longest_subsequence_gaps(seq1, seq2):
#     """

#     Args:
#         seq1 (str): The first DNA sequence.
#         seq2 (str): The second DNA sequence.

#     Returns:
#         str: The longest shared subsequence, with gaps allowed, represented by '-'.
#     """

    
#     populate_seq_matrix(seq1, seq2, seq_matrix)


# def longest_subsequence_no_gaps(seq1, seq2):

#     """
#     Args:
#         seq1 (str): The first DNA sequence.
#         seq2 (str): The second DNA sequence.

#     Returns:
#         str: The longest shared subsequence, with no gaps allowed.
#     """

