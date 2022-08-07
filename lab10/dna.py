def read_dna(dna_file):
    """
    Read a DNA string from a file.
    the file contains data in the following format:
    A <-> T
    G <-> C
    G <-> C
    C <-> G
    G <-> C
    T <-> A
    Output a list of touples
    [
        ('A', 'T'),
        ('G', 'C'),
        ('G', 'C'),
        ('C', 'G'),
        ('G', 'C'),
        ('T', 'A'),
    ]
    Where either (or both) elements in the string might be missing:
    <-> T
    G <->
    G <-> C
    <->
    <-> C
    T <-> A
    """
    field = ['A', 'T', 'C', 'G', 'U']
    dna = []
    with open(dna_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if len(line) == 8:
                tuple = (line[0], line[-2])
                dna.append(tuple)
            elif len(line) == 3:
                tuple = ('', '')
                dna.append(tuple)
            else:
                if line[0] in field:
                    tuple = (line[0], '')
                    dna.append(tuple)
                elif line[-2] in field:

                    tuple = ('', line[-2])
                    dna.append(tuple)
    return dna


def is_rna(dna):
    """
    Given DNA in the aforementioned format,
    return the string "DNA" if the data is DNA,
    return the string "RNA" if the data is RNA,
    return the string "Invalid" if the data is neither DNA nor RNA.
    DNA consists of the following bases:
    Adenine  ('A'),
    Thymine  ('T'),
    Guanine  ('G'),
    Cytosine ('C'),
    RNA consists of the following bases:
    Adenine  ('A'),
    Uracil   ('U'),
    Guanine  ('G'),
    Cytosine ('C'),
    The data is DNA if at least 90% of the bases are one of the DNA bases.
    The data is RNA if at least 90% of the bases are one of the RNA bases.
    The data is invalid if more than 10% of the bases are not one of the DNA or RNA bases.
    Empty bases should be ignored.
    """
    base = []
    for pair in dna:
        base.append(pair[0])
        base.append(pair[1])
    if 'U' in base:
        return 'RNA'
    else:
        return 'DNA'


def clean_dna(dna):
    """
    Given DNA in the aforementioned format,
    If the pair is incomplete, ('A', '') or ('', 'G'), ect
    Fill in the missing base with the match base.
    In DNA 'A' matches with 'T', 'G' matches with 'C'
    In RNA 'A' matches with 'U', 'G' matches with 'C'
    If a pair contains an invalid base the pair should be removed.
    Pairs of empty bases should be ignored.
    """
    new_dna = []

    field = ['A', 'T', 'C', 'G', 'U']
    pair_ATU = 0
    pair_CG = ord('C') + ord('G')
    if is_rna(dna) == 'DNA':
        pair_ATU = ord('A') + ord('T')
    elif is_rna(dna) == 'RNA':
        pair_ATU = ord('A') + ord('U')

    for pair in dna:
        if pair[0] == '' and pair[1] == '':
            continue

        elif pair[0] in field and pair[1] in field:
            new_dna.append(pair)
            continue

        elif pair[0] == '' and pair[1] in field:
            #print(pair)
            if pair[1] in ['A', 'T', 'U']:
                pair = (chr(pair_ATU - ord(pair[1])), pair[1])
                new_dna.append(pair)
                continue
            elif pair[1] in ['C', 'G']:
                pair = (chr(pair_CG - ord(pair[1])), pair[1])
                new_dna.append(pair)
                continue

        elif pair[0] in field and pair[1] == '':
            if pair[0] in ['A', 'T', 'U']:
                pair = (pair[0], chr(pair_ATU - ord(pair[0])))
                new_dna.append(pair)
                continue
            elif pair[0] in ['C', 'G']:
                pair = (pair[0], chr(pair_CG - ord(pair[0])))
                new_dna.append(pair)
                continue

        else:
            continue

    return new_dna


def mast_common_base(dna):
    """
    Given DNA in the aforementioned format,
    return the most common first base:
    eg. given:
    A <-> T
    G <-> C
    G <-> C
    C <-> G
    G <-> C
    T <-> A
    The most common first base is 'G'.
    Empty bases should be ignored.
    """
    base = []
    for pair in dna:
        base_1 = pair[0]
        base_2 = pair[1]
        base.append(base_1)
        base.append(base_2)

    dict = {}
    for key in base:
        dict[key] = dict.get(key, 0) + 1

    most_num = min(dict.values())
    most_base = ''
    for key, value in dict.items():
        if value == max(dict.values()):
            most_base = key
            break

    #print(dict)
    return most_base


def base_to_name(base):
    """
    Given a base, return the name of the base.
    The base names are:
    Adenine  ('A'),
    Thymine  ('T'),
    Guanine  ('G'),
    Cytosine ('C'),
    Uracil   ('U'),
    return the string "Unknown" if the base isn't one of the above.
    """
    name = ''
    if base == 'A':
        name = 'Adenine'
    elif base == 'T':
        name = 'Thymine'
    elif base == 'G':
        name = 'Guanine'
    elif base == 'C':
        name = 'Cytosine'
    elif base == 'U':
        name = 'Uracil'
    else:
        name = 'Unknown'
    return name
