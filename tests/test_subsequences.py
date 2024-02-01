from subsequences import calc_single_score, calc_score_matrix

def test_calc_single_delta():
    assert calc_single_score('A', 'A') == 1
    assert calc_single_score('A', 'G') == 0
    assert calc_single_score('A', 'T') == -1

def test_calc_score_matrix():
    assert calc_score_matrix('AAA', 'AAA') == [[0,  0,  0,  0],
                                               [0, -3, -2, -2],
                                               [0, -2, -3, -2],
                                               [0, -2, -2, -3]]
