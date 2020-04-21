'''for i in range(1, 10):
    print('----------------------')
    for j in range(1, 10):
        print('%2d * %2d = %2d' % (i, j, i * j))'''

student = [("Tien", ["Math", "English", "IT"]),
           ("Hiep", ["Math", "English"]),
           ("IT", ["English", "History", "IT", "xxx"]),
           ("TienHiep", ["xxx"])]

counter = 0
for (name, subjects) in student:
    print(name + " takes ", len(subjects), "courses")
    for sub in subjects:
        if sub == "English":
            counter += 1

print("English: %2d student" % counter)
