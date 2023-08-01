import argparse


def extract_scores(translations_path, score_path):
    """ Extracts translation scores from fairseq-generate output """

    # Read file and store scores
    scores = list()
    with open(translations_path, 'r', encoding='utf8') as tr_f:
        for line in tr_f:
            if line.startswith('H-'):
                score = line.split('     ')[0].split('  ')[1]
                scores.append(score)

    # Write scores to file
    with open(score_path, 'w', encoding='utf8') as sc_f:
        for s_id, s in enumerate(scores):
            if s_id >= 1:
                sc_f.write('\n')
            sc_f.write(s)

    print('-' * 20)
    print('Wrote perplexity scores to {:s}'.format(score_path))


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--translation_path', type=str, default=None,
                        help='path to the text file containing fairseq translation output')
    parser.add_argument('--score_path', type=str, default=None,
                        help='path to the text file to which translation scores are to be written')
    args = parser.parse_args()


