# def tabuada():
#     tab = 1
#     while tab <= 10:
#         print("Tabuada do", tab, ":", end="\t")
#         i = 1
#         while i <= 10:
#             print(tab*1, end="\t")
#             i = i + 1
#         print()
#         tab = tab + 1
# tabuada()

# def tabuada():
#     tab = 1
#     while tab <= 10:
#         i = 1
#         while i <= 10:
#             print(tab, "x", i, "=", tab*i)
#             i = i + 1
#         print()
#         tab = tab + 1
# tabuada()

def tabuada():
    tab = 0
    while tab < 10:
        tab = tab + 1
        i = 0
        while i < 10:
            i = i + 1
            print(tab,"x",i,"=",tab*i)
        print()
tabuada()