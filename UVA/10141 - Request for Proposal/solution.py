from sys import stdin
for t in stdin:
    n, p = map(int, t.split())
    if n == p and n==0:
        break
    requirements = []
    proposals = {}
    for _ in range(n):
        requirements.insert(0, stdin.readline())
    for __ in range(p):
        proposal = stdin.readline()
        proposals[proposal] = {}
        price_req = stdin.readline()
        proposals[proposal]['price'] = float(price_req.split()[0])
        req_met = int(price_req.split()[1])
        proposals[proposal]['req_met'] = req_met
        for ___ in range(req_met):
            s = stdin.readline()
        proposals[proposal]['compliance'] = req_met/n

    
    
        
print(proposals)