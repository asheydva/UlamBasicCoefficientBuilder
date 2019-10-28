def linear_model():
    """Calculate Ulam coefficients based on U(1,4) and U(1,5)."""

    n = 4

    seq1 = []
    f = open("ulam_sequence-04-04000000.log","r")
    for line in f:
        seq1.append(eval(line))

    f.close()

    seq2 = []
    f = open("ulam_sequence-05-05000000.log","r")
    for line in f:
        seq2.append(eval(line))

    f.close()

    coeff_list = []
    len1 = len(seq1)
    len2 = len(seq2)

    while (len1 > 1) and (len2 > 1):
        start1 = seq1[0]
        start2 = seq2[0]

        m = (start2 - start1)
        p = start1 - m * n

        try:
            while (len1 > 1) and (seq1[1] == seq1[0] + 1):
                seq1.pop(0)
                len1 = len(seq1)

        except IndexError:
            len1 = len(seq1)

        try:
            while (len2 > 1) and (seq2[1] == seq2[0] + 1):
                seq2.pop(0)
                len12 = len(seq2)

        except IndexError:
            len2 = len(seq2)

        if (len1 > 1) and (len2 > 1):
            end1 = seq1.pop(0)
            end2 = seq2.pop(0)

            k = end2 - end1
            r = end1 - k * n

            coeff_list.append(((m,p),(k,r)))

    f = open("Conjectured_Ulam_Coeff.txt","w")

    for item in coeff_list:
        f.write(str(item) + "\n")

    f.close()

    return "Completed!"

linear_model()
