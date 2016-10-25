import sys


def doors(arg):
    '''Takes a positive integer as a command line input.
        If no arguments are given, runs for arg = 10.
        Tackles the following programming problem:
        "You have arg number of doors in a hallway that are all initially closed. You make arg passes through the hallway. 
        The first time through, you visit every door and toggle every door.
        If the door is closed, you open it; if it is open, you close it.
        The second time you only visit every 2nd door (door #2, #4, #6, ...). 
        The third time, every 3rd door (door #3, #6, #9, ...), etc."
        Which door are open after the last pass through?"'''
     
    doors = []
    for n in range(0, arg):
        doors.append('X')
    
    print('Initial stage. All the doors are locked: ' +str(doors))

    for passage in range (0, arg):
        for door in range (passage, arg, passage+1):
            if doors[door] == 'X':
                doors[door] = 'O'
            else:
                doors[door] = 'X'

        print('Passage number ' + str(passage+1) + '. Current status: ' + str(doors))

    result = []
    for element in range(0, arg):
        if doors[element] == 'O':
            element += 1
            result.append(element)
    print('Doors number: ' + str(result) + ' are open.')


def main():
    
    error_msg = print('No or incorrect command line argument. Running the program for n = 10.')
    
    try:
        arg = int(sys.argv[1])
    except (IndexError, ValueError):
        error_msg
        arg = 10
    else:
        if arg < 0:
            arg = 10
            error_msg
    doors(arg)
    
if __name__ == '__main__':
    main()