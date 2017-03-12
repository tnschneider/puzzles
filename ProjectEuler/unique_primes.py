def uprimes(n, nprimes):
    p_list = []
    for i in range(2, n + 1):
        inlist = False
        while n % i == 0:
            if inlist == False:
                p_list.append(i)
            inlist = True
            if len(p_list) > nprimes:
                break
            n = n / i
    return len(p_list)
    
def main(num_uprimes):
    x = 0
    for i in range(2, 2*(10**num_uprimes)):
        iprimes = uprimes(i, num_uprimes)
        if iprimes == num_uprimes:
            x += 1
        else:
            x = 0
        if x == num_uprimes:
            print i
            break
        
def main2(n_p):
    i = 5
    while i < 100000:
        iprimes = uprimes(i, n_p)
        if iprimes == n_p:
            if uprimes(i - 1, n_p) == n_p or uprimes(i + 1, n_p) == n_p:
                print i
                i += 4
                #break
            else:
                i += 4
        else:
            i += 4