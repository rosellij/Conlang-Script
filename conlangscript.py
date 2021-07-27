import random

def makeWords(wordcount):

    consonantlistvoiceless = ['m', 'n', 'p', 'f', 't', 'ts', 's', 'sh', 'tch', 'r', 'l', 'k', 'x', 'w', 'λ', 'h', '?']
    consonantlistvoiced = ['m', 'n', 'b', 'v', 'd', 'dz', 'z', 'zh', 'dzh', 'r', 'l', 'g', 'γ', 'w', 'λ', 'h','?']
    vowellist = ['a', 'e', 'i', 'o', 'u', 'y']
    macrondict = {'a': 'ā', 'e': 'ē', 'i': 'ī', 'o': 'ō', 'u': 'ū', 'y': 'ȳ'}
    wordlist = []

    mlist = ['mn', 'mp', 'mf', 'mt', 'mts', 'ms', 'msh', 'mtch', 'mr', 'ml', 'mw', 'mλ', 'mk', 'mx', 'm?']
    nlist = ['np', 'nf', 'nt', 'nts', 'ns', 'nsh', 'ntch', 'nr', 'nl', 'nw', 'nλ', 'nk', 'nx', 'n?']
    plist = ['ps', 'psh', 'pr', 'pl', 'pw', 'pλ', 'px', 'p?']
    flist = ['ft', 'fts', 'fs', 'fsh', 'ftch', 'fr', 'fl', 'fw', 'fλ', 'fk', 'fx', 'f?']
    tlist = ['tr', 'tl', 'tw', 'tλ', 'tk', 'tx', 't?']
    tslist = ['tsm', 'tsn', 'tsp', 'tsf', 'tst', 'tsr', 'tsl', 'tsw', 'tsλ', 'tsk', 'tsx', 'ts?']
    slist = ['sm', 'sn', 'sp', 'sf', 'st', 'sts', 'stch', 'sr', 'sl', 'sw', 'sλ', 'sk', 'sx', 's?']
    shlist = ['shm', 'shn', 'shp', 'shf', 'sht', 'shts', 'shs', 'shtch', 'shr', 'shl', 'shw', 'shλ', 'shk', 'shx', 'sh?']
    tchlist = ['tchm', 'tchn', 'tchp', 'tchf', 'tcht', 'tchts', 'tchs', 'tchr', 'tchl', 'tchw', 'tchλ', 'tchk', 'tchx', 'tch?']

    listlist = [mlist, nlist, plist, flist, tlist, tslist, slist, shlist, tchlist]

    def innerFunction(subwordcount):

        wordlist = []
    
        for anynum in range(subwordcount):

            newword = ''
            if random.random() >= (2/3):
                newword += random.choice(consonantlistvoiceless)
            tempchar = random.choice(consonantlistvoiceless)
            if len(newword) > 0 and random.random() >= 0.5 and tempchar != newword[-1] and newword[-1] not in ['h', '?'] and consonantlistvoiceless.index(newword[0]) <= 8:
                newword = newword.replace(newword[:len(newword)], random.choice(listlist[consonantlistvoiceless.index(newword[:len(newword)])]))
            elif len(newword) > 0 and random.random() >= 0.5 and tempchar != newword[-1] and newword[-1] not in ['h', '?'] and consonantlistvoiceless.index(newword[0]) >= 9:
                newword = newword.replace(newword[:len(newword)], random.choice(random.choice(listlist)))
            newword += random.choice(vowellist)
            tempchar = random.choice(vowellist[:-1])
            if random.random() >= (1/3) and newword[-1] != 'y' and tempchar != newword[-1]:
                newword += tempchar
            tempchar = random.choice(consonantlistvoiceless[:-3])
            if random.random() >= (1/3):
                newword += tempchar
            if newword[0] in vowellist:
                newword = '?' + newword
            if random.random() <= (1/4):
                for anychar in newword:
                    if anychar in vowellist and anychar != 'u':
                        newword = newword.replace(anychar, macrondict[anychar])
                        break
                    elif anychar in vowellist:
                        if anychar == 'u':
                            if anychar != newword[-1]:
                                if newword[newword.index(anychar) + 1] in vowellist:
                                    newword = newword.replace(newword[newword.index(anychar) + 1], macrondict[newword[newword.index(anychar) + 1]])
            if newword not in wordlist:
                wordlist += [newword]
            elif newword in wordlist:
                continue

        return wordlist

    returnlist = innerFunction(wordcount)

    while len(returnlist) < wordcount:

        returnlist += innerFunction(len(returnlist) - wordcount)

    return returnlist

print(makeWords(10))