#withouth index
explain analyse select * from  persons_languages where languages_id=36
"  Rows Removed by Filter: 661"
"Execution time: 0.191 ms"
"Execution time: 0.171 ms"
"Execution time: 0.159 ms"


explain analyse select * from  persons_languages where persons_id=3
"Execution time: 0.075 ms"
"Execution time: 0.078 ms"
"Execution time: 0.064 ms"


#with indexom at language_id
create index moj on persons_languages(languages_id)
explain analyse select * from  persons_languages where persons_id=33
"Execution time: 0.055 ms"
"Execution time: 0.060 ms"
"Execution time: 0.066 ms"
explain analyse select * from  persons_languages where languages_id=12
"Execution time: 0.118 ms"
"Execution time: 0.066 ms"
"Execution time: 0.034 ms"
"Execution time: 0.076 ms"

it hepled almost 5 times better results.
Even its small amont of data it grows exponentialnaly.
approximetly 600 rows

