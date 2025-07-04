print("Enter Marks obtained in four subjects:  ")
math=int(input("math:        "))
english=int(input("english:  "))
science=int(input("science:  "))
hindi=int(input("hindi:      "))
sum=math+english+science+hindi
print("Sum of math,english,science,hindi is: ",sum)
perc=(sum/400)*100
print(end="The percentage marks is:             ")
print(perc)
