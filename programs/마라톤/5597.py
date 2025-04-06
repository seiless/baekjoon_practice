import sys

all_students = [i for i in range(1,31)]
submited_students = [int(line.strip()) for line in sys.stdin]
not_submitted = list(set(all_students)-set(submited_students))
not_submitted.sort()
for student in not_submitted:
    print(student)