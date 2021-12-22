# Algorithm:
# 1. If the length of the array is lesser than or equal to 2 then return True (Base case)
# 2. Initialize a variable called direction and assign the difference between the second element and the first element of the input array
# 3. Pick the next element (2nd Index or 3rd Element) in the input array
# 4. Check if the direction = 0, if that is the case then for each element that we pick, try to define the direction as the difference between the current element and the previous element and move on to the next element
# 5. Check if the current element and the previous element are breaking direction, if they are then return False, otherwise move on to the next element
# 6. Repeat steps: 3 - 5 until we reach the end of the list
# 7. return True as we have not encuontered any pair that breaks direction

def isMonotonic(array):
    if len(array) <= 2:
        return True
    
    direction = array[1] - array[0]
    for i in range(2, len(array)):
        if direction == 0:
            direction = array[i] - array[i - 1]
            continue

        if breaksDirection(direction, array[i - 1], array[i]):
            return False
    
    return True

def breaksDirection(direction, previousEl, currentEl):
    current_direction = currentEl - previousEl
    if direction > 0 and current_direction < 0:
        return True
    if direction < 0 and current_direction > 0:
        return True
    return False


if __name__ == "__main__":
    testcases = [
        [1, 5, 10, 10, 1100, 1101, 1102, 9001],
        [9001, 1102, 1101, 1100, 10, 10, 5, 1],
        [9001, 1102, 1101, 1100, 10, 15, 5, 1]
    ]

    for testcase in testcases:
        result = isMonotonic(testcase)
        print(f"is monotonic: {result}")
    