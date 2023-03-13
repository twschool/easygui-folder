import easygui as eg
nz_word = eg.enterbox("Word")
ok = nz_word.replace("our", "or")
ok = ok.replace("ise", "ize")
if ok == nz_word:
    eg.msgbox("Same")
else:
    eg.msgbox(f"Different: Old word ({nz_word}) New word ({ok})")
# Change