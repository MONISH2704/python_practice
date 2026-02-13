score=[52,47,87,92,99]
def marks(score):
    if score >=90:
        return "excellent"
    elif score >=75:
        return "average"
    elif score>=60:
        return "good"
    else:
        return "fail"

result=(map(marks,score))
print("marks: ",score)
print("comment: ",list(result))