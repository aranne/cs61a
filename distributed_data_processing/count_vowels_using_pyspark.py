"""Using MapReduce flow in pyspark to get all the vowels in shakespeare.txt"""

data = sc.textFile('shakespeare.txt')

""" flatMap(fn) is a method of pyspark.rdd.RDD instance.
Return a new RDD by first applying a function to all elements of this RDD, and then flattening the results."""

def vowels(line):
    for v in 'aeiou':
        if v in line:
            yield (v, line.count(v))    # yield a key-value pair to count how many times a vowel appears in a line.

>>> data.flatMap(vowels).take(10)       # take the first 10 entries.
[('a', 3), ('i', 3), ('o', 4), ('u', 3), ('a', 5), ('e', 1), ('i', 2), ('o', 2), ('u', 1), ('e', 2)]


""" reduceByKey(fn) is a method of pyspark.rdd.RDD instance.
Merge the values for each key using an associative reduce function."""

from operator import add
>>> data.flatMap(vowels).reduceByKey(add).collect()      # collect the results
[('i', 189626), ('a', 233881), ('u', 110820), ('o', 272697), ('e', 387705)]
