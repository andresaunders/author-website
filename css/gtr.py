
gtr = [3,1, 15, 6, 2]
gtr_org = [3,1, 15, 6, 2]

def change_gtr(factors, gtr):
    for i in range(len(gtr)):
        gtr[i] *= factors[i]
    print_list()
    gtr = gtr_org

'''def change_gtr(index, new):
    global gtr
    current = gtr[index]
    factor = new/current
    for i in range(len(gtr)):
        gtr[i] *= factor'''

def print_list():
    global gtr
    gtr_css = ""
    for i in range(len(gtr)):
        if i != len(gtr) - 1:
            gtr_css += str(gtr[i]) + "fr "
        else:
            gtr_css += str(gtr[i]) + "fr;"
    print(gtr_css)

while True:
    change = input("change gtr?");
    if change == "y":
        factors = input("factors:\n")
        factors = [float(s) for s in factors.split(',')]
        change_gtr(factors, gtr)
        



