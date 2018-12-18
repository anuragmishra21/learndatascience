from sklearn import tree
#[height,weight,shoe size]
X=[[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,63,41],[171,75,42],[181,85,43]]
Y=['male','female','female','female','male','male','female','male','female','male','male']

A=[[10,12],[13,14],[15,14]]
B=['duffer','idiot','duffer']
clf=tree.DecisionTreeClassifier()
clf=clf.fit(A,B)

prediction=clf.predict([[19,44]])
print(prediction)