import argparse


def extract_scores(translation_path, ref_path, hyp_path):
    """ Extracts translation scores from fairseq-generate output """

    # Read file and store scores
    ref_list, hyp_list = list(), list()
    with open(translation_path, 'r', encoding='utf8') as tr_f:
        for line in tr_f:
            if line.startswith('T-'):
                ref = line.split('\t')[-1].strip()
                ref_list.append(ref)
            if line.startswith('H-'):
                hyp = line.split('\t')[-1].strip()
                hyp_list.append(hyp)

    # Write clean information to file
    with open(ref_path, 'w', encoding='utf8') as r_f:
        for r_id, r in enumerate(ref_list):
            if r_id >= 1:
                r_f.write('\n')
            r_f.write(r)

    with open(hyp_path, 'w', encoding='utf8') as h_f:
        for h_id, h in enumerate(hyp_list):
            if h_id >= 1:
                h_f.write('\n')
            h_f.write(h)

    print('-' * 20)
    print('Done!')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--translation_path', type=str, default=None,
                        help='path to the text file containing fairseq translation output')
    parser.add_argument('--ref_path', type=str, default=None,
                        help='path to the text file to which sample references should be written')
    parser.add_argument('--hyp_path', type=str, default=None,
                        help='path to the text file to which cleaned-up model translations should be written')
    args = parser.parse_args()

    extract_scores(args.translation_path, args.ref_path, args.hyp_path)
