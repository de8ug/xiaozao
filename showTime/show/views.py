from django.shortcuts import render
import json
# Create your views here.
# 

"""
7.1	2	1.6	20
7.2	4	5	22
7.3	7	1	300
7.4	3.2	4	45
7.5	5.6	0.6	63
"""
def get_data(filename):
    date = []
    todo = []
    done = []
    code = []
    with open(filename) as f:
        for line in f:
            d = line.split()
            if d:
                date.append(d[0])
                todo.append(d[1])
                done.append(d[2])
                code.append(d[3])
    return date, todo, done, code


def index(request):
    # date = ['8.11', '7.2', '7.3','7.4','7.5']
    date, todo, done, code = get_data('./data.txt')
    date_j = json.dumps(date, separators=(',', ':'))
    todo_j = json.dumps(todo, separators=(',', ':'))
    done_j = json.dumps(done, separators=(',', ':'))
    code_j = json.dumps(code, separators=(',', ':'))
    return render(request, 'index.html', {'date': date_j, 
                                           'todo': todo_j,
                                           'done': done_j,
                                           'code': code_j })