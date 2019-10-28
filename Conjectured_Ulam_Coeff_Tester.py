def load_model():
    model = []
    f = open("Conjectured_Ulam_Coeff.txt","r")

    for line in f:
        model.append(eval(line))

    f.close()
    return model

def load_sequence(n):
    base_name = "ulam_sequence-"
    number_name = str(n).zfill(2)

    longer_name = base_name + number_name + "-"
    length_name = str(1000000*n).zfill(8)

    file_name = longer_name + length_name + ".log"

    ulam_list = []
    f = open(file_name,"r")

    for line in f:
        ulam_list.append(eval(line))

    f.close()
    return ulam_list

def ulam_sequence_expected(model, n):
    """Returns the sequence U(1,n) predicted by the model."""

    seq = []

    for term in model:
        (m, p) = term[0]
        (k, r) = term[1]

        start = m * n + p
        end = k * n + r

        for u in range(start, end + 1):
            seq.append(u)

    return seq

def compare_actual_w_predicted(model, n):
    ulam_actual = load_sequence(n)
    ulam_expected = ulam_sequence_expected(model, n)

    ulam_actual = ulam_actual[:len(ulam_expected)]

    for i in range(len(ulam_expected)):
        if ulam_actual[i] != ulam_expected[i]:
            print(ulam_actual[i])
            print(ulam_expected[i])
            return "Difference at " + str(i) + "-th place."

    return "No differences found."

def ulam_comparison():
    model = load_model()

    for n in range(6,15):
        print("Testing U(1," + str(n) + ")")
        print(compare_actual_w_predicted(model,n))

    return "All done!"
