def BEANTWOORD_MIJ():
    '''dees is dus gewoon input, maar dan aandringender'''
    inpuot = ''
    while inpuot == '':
        inpuot = input()
    return inpuot

def BEANTWOORD_MIJ_MET_PROMPT(prompt='>'):
    '''dees is dus gewoon hetzelfde, maar dan met een prompt'''
    inpuot = ''
    while inpuot == '':
        inpuot = input(prompt)
    return inpuot

def BEANTWOORD_MIJ_MET_PROMPT_ZONDER_STRIPWS_EN_ME_TITLECASE(prompt='>', stripws=True, titlecase=False):
    '''dees is dus gewoon hetzelfde, maar dan met een prompt EN ME STRIPWS EN ME TITLECASE'''
    inpuot = ''

    while inpuot == '':
        inpuot = input(prompt)
        if stripws:
            inpuot = inpuot.strip()
        if titlecase:
            inpuot = inpuot.title()

    return inpuot




print("WA IS UW NAAM")
NAAM = BEANTWOORD_MIJ()
TUIN = BEANTWOORD_MIJ_MET_PROMPT(prompt="WA IS UW HUISTUIN: ")
krak = BEANTWOORD_MIJ_MET_PROMPT()
jezus_christus = BEANTWOORD_MIJ_MET_PROMPT_ZONDER_STRIPWS_EN_ME_TITLECASE(prompt="JEZUS: ")
jezus_christus_title = BEANTWOORD_MIJ_MET_PROMPT_ZONDER_STRIPWS_EN_ME_TITLECASE(prompt="JEZUSTITEL: ", titlecase=True)
print(jezus_christus)
print(jezus_christus_title)
print(krak)




print(f"UWE NAAM IS {NAAM} EN GIJ KOMT VAN {TUIN}")