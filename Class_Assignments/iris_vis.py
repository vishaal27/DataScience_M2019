from sklearn import datasets
import matplotlib.pyplot as plt

iris=datasets.load_iris()

# print(iris.data[:,3])
target_1_index=list(iris.target).index(1)
target_2_index=list(iris.target).index(2)

plt.figure()
plt.plot(iris.data[:target_1_index,0], label='Setosa')
plt.plot(iris.data[target_1_index:target_2_index,0], label='Versicolour')
plt.plot(iris.data[target_2_index:,0], label='Virginica')
plt.xlabel('Data Samples')
plt.ylabel('Sepal length')
plt.legend(loc='best')
plt.show()

plt.figure()
plt.plot(iris.data[:target_1_index,1], label='Setosa')
plt.plot(iris.data[target_1_index:target_2_index,1], label='Versicolour')
plt.plot(iris.data[target_2_index:,1], label='Virginica')
plt.xlabel('Data Samples')
plt.ylabel('Sepal width')
plt.legend(loc='best')
plt.show()

plt.figure()
plt.plot(iris.data[:target_1_index,2], label='Setosa')
plt.plot(iris.data[target_1_index:target_2_index,2], label='Versicolour')
plt.plot(iris.data[target_2_index:,2], label='Virginica')
plt.xlabel('Data Samples')
plt.ylabel('Petal length')
plt.legend(loc='best')
plt.show()

plt.figure()
plt.plot(iris.data[:target_1_index,3], label='Setosa')
plt.plot(iris.data[target_1_index:target_2_index,3], label='Versicolour')
plt.plot(iris.data[target_2_index:,3], label='Virginica')
plt.xlabel('Data Samples')
plt.ylabel('Petal width')
plt.legend(loc='best')
plt.show()