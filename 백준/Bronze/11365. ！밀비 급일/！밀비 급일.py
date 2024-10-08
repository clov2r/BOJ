while(True):
    sentence=input()
    if sentence=='END':
        break;
    else:
        sentence=list(sentence)
        print(*sentence[::-1], sep="")
