# Content-based recommendation

from matrix import Matrix
import numpy
# numpy.set_printoptions(precision=2)

#-------------------------------------------------------------------

UF = Matrix(
	'UserFeature',
	['Mary', 'Tom', 'Jerry'], 
	['J.Roberts', 'T.Hanks', 'TheRock', 'Thriller', 'Action', 'Romantics']
)

UF.set(0, [5,4,1,0,0,4])
UF.set(1, [3,4,0,0,0,5])
UF.set(2, [1,1,5,4,5,2])
UF.show()

IF = Matrix(
	'ItemFeature',
	['LarryCrowne', 'PrettyWoman', 'Sully', 'Hercules'],
	['J.Roberts', 'T.Hanks', 'TheRock', 'Thriller', 'Action', 'Romantics']
)
IF.set(0, [1, 1, 0, 0, 0, 1])
IF.set(1, [1, 1, 0, 0, 0, 1])
IF.set(2, [0, 1, 0, 1, 1, 0])
IF.set(3, [0, 0, 1, 1, 1, 0])
IF.show()

UI = numpy.matmul(UF.mat, numpy.transpose(UF.mat))
print(UI)

