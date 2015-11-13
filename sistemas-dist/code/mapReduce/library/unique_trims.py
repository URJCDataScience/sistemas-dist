import MapReduce
import sys

"""
Unique Trims Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence identifier
    id = record[0]
    sequence = record[1]
    # Quita ls 10 ultimos caracteres del string
    sequence = sequence [:-10]
    mr.emit_intermediate(sequence, 1)

def reducer(key, list_of_values):
    # key: sequencia menos los 10 ultimas letras
    mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
