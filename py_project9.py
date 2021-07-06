#To  find out output total marks  and average marks of any 5 subjects by using input method.

sub_marks = input("enter marks of all subjects (please include space between numbers e.g. 1 2 3): ").split()
sub_marks = [int(i) for i in sub_marks]
total_marks = sum(sub_marks)
print("Total marks are: ", total_marks)
Avg_marks = total_marks / len(sub_marks)
print("Average marks are: ", Avg_marks)
