import json

def main():
    jString = '{"matrix":[["1","2"],["3","4"]]}'
    jMatrix = json.loads(jString)
    Matrix = jMatrix["matrix"]
    term1 = Matrix[0][0]       # yields: '1'   expected: 1
    term2 = Matrix[0][1]       # yields: '2'   expected: 2

    result = term1 + term2     # yields: '12'   expected: 3
    return

if __name__ == "__main__":
    main()
