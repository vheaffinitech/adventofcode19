data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]
dataTwo = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,2,23,6,27,2,6,27,31,2,13,31,35,1,10,35,39,2,39,13,43,1,43,13,47,1,6,47,51,1,10,51,55,2,55,6,59,1,5,59,63,2,9,63,67,1,6,67,71,2,9,71,75,1,6,75,79,2,79,13,83,1,83,10,87,1,13,87,91,1,91,10,95,2,9,95,99,1,5,99,103,2,10,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]

def compute(data_list, iteration):
    output = data_list
    minThreshold = iteration*4
    if len(data_list) - minThreshold < 4:
        maxThreshold = len(data_list)
    else:
        maxThreshold = (iteration+1)*4
    input = data_list[minThreshold:maxThreshold]
    if input[0] == 1:
        inputOneIndex = input[1]
        inputTwoIndex = input[2]
        outputPosition = input[3]

        inputOne = output[inputOneIndex]
        inputTwo = output[inputTwoIndex]
        inputSum = inputOne + inputTwo
        
        output[outputPosition] = inputSum
    elif input[0] == 2:
        inputOneIndex = input[1]
        inputTwoIndex = input[2]
        outputPosition = input[3]
        
        inputOne = output[inputOneIndex]
        inputTwo = output[inputTwoIndex]
        inputMulti = inputOne * inputTwo
        
        output[outputPosition] = inputMulti
    elif input[0] == 99:
        return (output, -1)
    return (output, iteration)

def data_compute(x):
    iteration = 0
    max_iteration = len(x) // 4
    while iteration <= max_iteration:
        (x, y) = compute(x, iteration)
        if y == -1:
            break
        else:
            iteration = iteration+1
    return x


def test_a():
  assert compute([1,0,0,0,99],0) == ([2,0,0,0,99], 0)
  assert compute([2,3,0,3,99],0) == ([2,3,0,6,99],0)
test_a()

def test_b():
  assert data_compute([1,0,0,0,99]) == [2,0,0,0,99]
  assert data_compute([2,3,0,3,99]) == [2,3,0,6,99]
  assert data_compute([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
  assert data_compute([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]
  assert data_compute([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50]
test_b()


def main():
    outputOne = data_compute(dataTwo)
    print("First answer: %d" %outputOne[0])

    dataThree = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]
    for i in range(0,100):
        for j in range(0,100):
            dataThree[1] = i
            dataThree[2] = j
            
            try:
                o = data_compute(dataThree)

                if o[0] == 19690720:
                    print("noun: %s - verb: %s" %(i, j))
                    answer=100*i+j
                    print("Second anwser : %d" % answer)
                    break
                else:
                    dataThree = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,6,19,23,2,6,23,27,1,5,27,31,2,31,9,35,1,35,5,39,1,39,5,43,1,43,10,47,2,6,47,51,1,51,5,55,2,55,6,59,1,5,59,63,2,63,6,67,1,5,67,71,1,71,6,75,2,75,10,79,1,79,5,83,2,83,6,87,1,87,5,91,2,9,91,95,1,95,6,99,2,9,99,103,2,9,103,107,1,5,107,111,1,111,5,115,1,115,13,119,1,13,119,123,2,6,123,127,1,5,127,131,1,9,131,135,1,135,9,139,2,139,6,143,1,143,5,147,2,147,6,151,1,5,151,155,2,6,155,159,1,159,2,163,1,9,163,0,99,2,0,14,0]
            except IndexError:
                pass

if __name__ == '__main__':
    main()
