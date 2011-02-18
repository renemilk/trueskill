set xlabel "iteration"
set term wxt 0
set ylabel "mu"

plot 'skills.csv' using 1:2 with lines title 'mu alice',\
'skills.csv' using 1:4 with lines title 'mu bob',\
'skills.csv' using 1:6 with lines title 'mu chris',\
'skills.csv' using 1:8 with lines title 'mu darren'

set term wxt 1
set ylabel "sigma"

plot 'skills.csv' using 1:3 with lines title 'sigma alice',\
'skills.csv' using 1:5 with lines title 'sigma bob',\
'skills.csv' using 1:7 with lines title 'sigma chris',\
'skills.csv' using 1:9 with lines title 'sigma darren'