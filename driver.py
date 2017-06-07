from postman import Solution

s = Solution()

# Case given in the question
matrix = [[0,0,0,'G',0,'X'], [0,1,1,0,'X',0], ['S',0,'X',0,0,0]]
print s.delivery(matrix)

# Case where repeated path has to occur
matrix2 = [['X',1,'G'],[0,1,0],['S',0,'X']]
print s.delivery(matrix2)

# Case that contains unreachable X
matrix3 = [['X',1,'G'],[1,1,0],['S',0,'X']]
print s.delivery(matrix3)

# Case that contains unreachable G
matrix4 = [['X',1,'G'],[0,1,1],['S',0,'X']]
print s.delivery(matrix4)

