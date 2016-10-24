operations = ['add', 'list', 'mark', 'archive', 'exit']

todolist = []
donelist = []

while True:
    task_sel = input('Please specify a command [list, add, mark, archive, exit]: ')
    if task_sel == 'exit':
        break
    else:
        if task_sel in operations:
            if task_sel == 'add':
                new_task = input('Add an item: ')
                todolist.append(new_task)
                print('Task added.')
            elif task_sel == 'list':
                if not todolist and not donelist:
                    print('You have no tasks yet.')
                else:
                    task_number = 1
                    print('You saved the following to do items:')
                    for e in todolist:
                        print(task_number, end='. ')
                        print('[ ]', end=' ')
                        print(e)
                        task_number += 1
                    for e in donelist:
                        print(task_number, end='. ')
                        print('[X]', end=' ')
                        print(e)
                        task_number += 1

            elif task_sel == 'archive':
                donelist = []
                print('All completed tasks got deleted.')
            elif task_sel == 'mark':
                if not todolist and not donelist:
                    print('You have no tasks yet.')
                else:
                    task_number = 1
                    print('You saved the following to do items.')
                    for e in todolist:
                        print(task_number, end='. ')
                        print('[ ]', end=' ')
                        print(e)
                        task_number += 1
                    while True:
                        try:
                            mark_item = int(input('Please select item to be marked as completed: '))
                            if mark_item in range (1, task_number+1):
                                donelist.append((todolist.pop(mark_item-1)))
                                break
                        except IndexError or ValueError:
                            print('Incorrect task number. Please try again.')
