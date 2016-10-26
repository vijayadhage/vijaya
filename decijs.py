import json

def main():
    jString = '{"matrix":[["1","2"],["3","4"]]}'
    jMatrix = json.loads(jString)
    print jMatrix
    Matrix = jMatrix["matrix"]
    print Matrix
    i = [[int(v) for v in row] for row in Matrix]
    j=[map(int, y) for y in Matrix]
    print j
#    new=map(int, Matrix[0])
#    term1 = new[0]       # yields: '1'   expected: 1
#    term2 = new[1]       # yields: '2'   expected: 2
    term1=i[0][0]
    term2=i[0][1]

    result = term1 + term2     # yields: '12'   expected: 3
    print result
    return

if __name__ == "__main__":
    main()
