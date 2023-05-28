r"""
==================================================
Little script for "translating" stuff to Tex

Implemented by intentodemusico and nico
OP: https://stackoverflow.com/users/16504277/nico

==================================================
TODO documentation

"""
__author__ = 'intentodemusico'


from tensorflow.keras import Model


def m2tex(model: Model, modelName: str, line_length: int):
    stringlist = []
    model.summary(line_length=line_length, print_fn=lambda x: stringlist.append(x))
    del stringlist[1:-4:2]
    del stringlist[-1]
    first_vertical_border = int(31 / 70 * line_length)
    second_vertical_border = int(59 / 70 * line_length)
    for ix in range(1, len(stringlist) - 3):
        tmp = stringlist[ix]
        stringlist[ix] = tmp[0:first_vertical_border]+"& "+tmp[first_vertical_border:second_vertical_border]+"& "+tmp[second_vertical_border:]+"\\\\ \hline"
    stringlist[0] = "Model: {} \\\\ \hline".format(modelName)
    stringlist[1] += " \hline"
    stringlist[-4] += " \hline"
    stringlist[-3] += " \\\\"
    stringlist[-2] += " \\\\"
    stringlist[-1] += " \\\\ \hline"
    prefix = ["\\begin{table}[]", "\\begin{tabular}{lll}"]
    suffix = ["\end{tabular}", "\caption{{Model summary for {}.}}".format(modelName), "\label{tab:model-summary}" , "\end{table}"]
    stringlist = prefix + stringlist + suffix
    out_str = " \n".join(stringlist)
    out_str = out_str.replace("_", "\_")
    out_str = out_str.replace("#", "\#")
    print(out_str)
