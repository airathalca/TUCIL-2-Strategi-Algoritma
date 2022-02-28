from math import atan2
from matplotlib import pyplot as plt

def quickhull(List):
    answer = []
    List.sort(key = lambda arr: [arr[0], arr[1]])
    answer.append(List[0])
    answer.append(List[-1])

    Arrpos = checkPoint (List,"POS",List[0],List[-1])
    Arrneg = checkPoint (List,"NEG",List[0],List[-1])
    answer += (Hull(Arrpos,List[0],List[-1]))
    answer += (Hull(Arrneg,List[0],List[-1]))
    center = searchCenter(answer)
    answer.sort(key = lambda point: (atan2(point[1]-center[1],point[0]-center[0])))
    return answer

def checkPoint(List, side, pointLeft, pointRight):
    newList = []
    for i in range(len(List)):
        check = pointLine(pointLeft, pointRight, List[i])
        if (side == "POS" and check > 0):
            newList.append(List[i])
        elif (side == "NEG" and check < 0):
            newList.append(List[i])
    return newList

def Hull(List,pointL,pointR): #divide and conquer
    ans = []
    if (len(List) == 0):
        return ans
    List.sort(key = lambda point:abs(pointLine(pointL,pointR,point)), reverse=True)
    ans.append(List[0])
    arrpos = []
    arrneg = []
    for point in List:
        if pointLine(pointL,List[0],point) * pointLine(pointL,List[0],pointR) < 0:
            arrpos.append(point)
        if pointLine(pointR,List[0],point) * pointLine(pointR,List[0],pointL) < 0:
            arrneg.append(point)
    ans += Hull(arrpos,pointL,List[0])
    ans += Hull(arrneg,List[0],pointR)
    return ans
        
def pointLine(p1,p2,p):
    return (p2[0]-p1[0])*(p[1]-p1[1]) - (p2[1]-p1[1])*(p[0]-p1[0])

def searchCenter(List):
	x = y = 0
	for point in List:
		x += point[0]
		y += point[1]
	center = [x/len(List), y/len(List)]
	return center

def plotting(data, type_name, x_point, y_point, target):
    data_plot = data.copy()
    plt.figure(figsize = (10, 6))
    colors = ["blue","orange","green","red","purple","brown","pink","gray","olive","cyan"]
    plt.title(f"{x_point} vs {y_point}")
    plt.xlabel(x_point)
    plt.ylabel(y_point)
    if (target != "NONE"):
        i = 0
        for v in data_plot[target].unique():
            bucket = data_plot[data_plot[target] == v]
            datasets = bucket[[x_point,y_point]].values.tolist()
            hull = quickhull(datasets)
            ansX, ansY = [x for x in zip(*hull)]
            ansX = list(ansX)
            ansY = list(ansY)
            ansX.append(hull[0][0])
            ansY.append(hull[0][1])
            plt.scatter(bucket[x_point].values, bucket[y_point].values, label=type_name[i])
            plt.plot(list(ansX), list(ansY), colors[i%len(colors)])
            i += 1
        plt.legend()
    else:
        bucket = data_plot
        datasets = bucket[[x_point,y_point]].values.tolist()
        hull = quickhull(datasets)
        ansX, ansY = [x for x in zip(*hull)]
        ansX = list(ansX)
        ansY = list(ansY)
        ansX.append(hull[0][0])
        ansY.append(hull[0][1])
        plt.scatter(bucket[x_point].values, bucket[y_point].values)
        plt.plot(list(ansX), list(ansY), colors[2])
    plt.show()