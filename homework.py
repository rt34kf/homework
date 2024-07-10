gradess = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
gradess1 = (sum(gradess[0]) / len(gradess[0]), sum(gradess[1]) / len(gradess[1]),
            sum(gradess[2]) / len(gradess[2]), sum(gradess[3]) / len(gradess[3]),
            sum(gradess[4]) / len(gradess[4]))
students1 = sorted(students)
gradess_students = zip(students1, gradess1)
print(dict(gradess_students))




