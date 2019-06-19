Local execution using Unix pipes and gives us the count of each vowel in the haiku.txt:

$ cat haiku.txt | ./count_vowels_mapper.py | sort | ./sum_reducer.py
'a' 6
'e' 5
'i' 2
'o' 5
'u' 1