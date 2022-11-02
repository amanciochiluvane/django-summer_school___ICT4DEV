scores=list([float(x) for x in input("Enter the 3 scores:").split(',')])
weight=list(float(x) for x in input("Enter their weights:").split(','))
if len(scores)!=len(weight):
    print("The amount of scores and weights are different!")
else:
    prod=[x*y for x,y in zip(scores,weight)]
    sum_of_prods = sum(prod)
    weight_sum=sum(weight)


    m = sum_of_prods / weight_sum
    print("Your final score is:",m)






