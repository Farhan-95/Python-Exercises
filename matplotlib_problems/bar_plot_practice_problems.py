#  =========================== Matplotlib Problems =========================

import matplotlib.pyplot as plt

# program 1 --------------------

language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(language,popularity,width = 0.8)
plt.xlabel('programming language')
plt.ylabel('popularity')
plt.grid()
plt.show()


# program 2 ------------------------

language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.barh(language,popularity,color = 'g',height = 0.9)
plt.xlabel('programming language')
plt.ylabel('popularity')
plt.grid()
plt.show()

# program 3 ----------------------

language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
color = ['red','black', 'green', 'blue', 'yellow', 'skyblue']

plt.bar(language,popularity,color = color)
plt.xlabel('programming language')
plt.ylabel('popularity')
plt.grid()
plt.show()

# program 4 ---------------------

language = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

plt.bar(language,popularity,)
plt.xlabel('programming language')
plt.ylabel('popularity')
plt.grid()
plt.show()



