my_dict = {}
with open('6.txt') as f:
    for subject in f:
        subject_name = subject.split()[0]
        hours = subject.split()[1:]
        my_dict[subject_name] = 0
        for i in hours:
            try:
                my_dict[subject_name] += int(i[:i.find("(")])
            except ValueError:
                pass
print(my_dict)
