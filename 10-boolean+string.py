
while True:
    print("WILdE GIJ GELIJKHEID OF ONGELIJKHEID?")
    HetDing = str(input())
    if HetDing == "gelijkheid":
        print("geeft is uw  linkergetal")
        linkse = int(input())
        print("geeft is uw rechtergetal")
        rechtse = int(input())
        print(linkse, "=", rechtse, "iiiiiis", linkse==rechtse)
    elif HetDing == "ongelijkheid":
        print("Wilde < of >?")
        Welke = str(input())
        if Welke == "<":
            print("geeft is uw  linkergetal")
            linkse = int(input())
            print("geeft is uw rechtergetal")
            rechtse = int(input())
            print(linkse, "<", rechtse, "iiiiiiis", linkse<rechtse)
        else:
            print("Ja dan maar > eh")
            print("geeft is uw  linkergetal")
            linkse = int(input())
            print("geeft is uw rechtergetal")
            rechtse = int(input())
            print(linkse, ">", rechtse, "iiiiiiis", linkse>rechtse)
    else:
        print("Gast gij zijt ook altijd saai, eh")