def print_rangoli(size):
    
    # Top Part
    if size != 1:
        s = {0, }
        ls = []
        lst = []
        for i in range(size):
            ls.append(i)

        w = 2 * (len(ls) + (len(ls) - 2)) + 1
        
        lst.append(chr(ls[size - 1] + 97))
        print(("".join(lst)).center(w, "-"))
        
        for i in range(size - 1, 1, -1):
            if len(lst) % 2 == 0:
                lst.insert(len(lst) // 2, chr(97 + (i-1)) + "-" + chr(97 + i))
                print("-".join(lst).center(w, "-"))
            else:
                lst.insert((len(lst) - 1) // 2, chr(97 + i) + "-" + chr(97 + (i-1)))
                print("-".join(lst).center(w, "-"))
        
        # Bottom Part
        s = {0, }
        ls = []
        for i in range(size):
            s.add(i)
        s = list(s)
        lst = s[::-1]
        lst.remove(0)
        lst.extend(s)
        
        for i in lst:
            ls.append(chr(97 + i))
        w = len(ls) + (len(ls) - 1)
        
        for i in range((len(ls) // 2) + 1):
            if i == 0:
                print("-".join(ls).center(w, "-"))
                ls.remove(min(ls))
            else:
                ls.remove(min(ls))
                print("-".join(ls).center(w, "-"))
                ls.remove(min(ls))
    
    else:
        print("a")
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
