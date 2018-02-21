# TITLE : Lists

if __name__ == '__main__':
    N = int(raw_input())
    l = []
    i = 0
    for i in xrange(N):
        masuk = raw_input().split()
        perintah = masuk[0]
        
        if perintah == 'insert':
            x = int(masuk[1])
            y = int(masuk[2])
            l.insert(x,y)
        elif perintah == 'print':
            print l
        elif perintah == 'remove':
            x = int(masuk[1])
            l.remove(x)
        elif perintah == 'append':
            x = int(masuk[1])
            l.append(x)
        elif perintah == 'sort':
            l.sort()
        elif perintah == 'pop':
            l.pop()
        elif perintah == 'reverse':
            l.reverse() 
        