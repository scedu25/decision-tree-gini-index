import sys

def train(input):
    training_classes = {}
    for line in input[1:n+1]:
        line = line.strip().split()
        label = line[0]
        if (label not in training_classes):
            training_classes[label] = {'size': 1}
        else:
            training_classes[label]['size'] += 1
        for pair in line[1:]:
            index, value = pair.split(':')
            if index not in training_classes[label]:
                training_classes[label][index] = {value: 1}
            elif value not in training_classes[label][index]:
                training_classes[label][index][value] = 1
            else:
                training_classes[label][index][value] += 1
    # print(training_classes)
    num_classes = len(training_classes)
    gini_d = 1 - sum([(len(training_classes[x]) / n)**2 for x in training_classes])
    # for 

def test(input):
    for line in input[n+2:]:
        line = line.strip().split()
        for pair in line:
            index, value = pair.split(':')


if __name__ == "__main__":
    input = sys.stdin.readlines()
    # input = open("input.txt", "r").readlines()
    n = int(input[0])
    t = int(input[n+1])
    predictions = []
    train(input)
    test(input)