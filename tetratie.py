def tetratie(getal,tet):
    getetreerd = getal
    for amai in range(0,tet,1):
        getetreerd = getetreerd**getal
    return getetreerd
print(tetratie(5,5))