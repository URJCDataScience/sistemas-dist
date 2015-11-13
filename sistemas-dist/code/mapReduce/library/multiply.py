import MapReduce
import sys

"""
Matrix Multiply Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    matrix = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if (matrix == "a"):
    	for k in range (0,5):
      		mr.emit_intermediate((i,k), (matrix,j,value))
    elif (matrix == "b"):
    	for k in range (0,5):
      		mr.emit_intermediate((k,j), (matrix,i,value))


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    a = [0,0,0,0,0]
    b = [0,0,0,0,0]

    for data in list_of_values:
    	if (data[0] == "a"):
    		a[data[1]] = data[2]
    	elif (data[0] == "b"):
    		b[data[1]] = data[2]
    
    for j in range(0,5):
    	total += a[j]*b[j]
    
    if total <> 0:
   		mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
