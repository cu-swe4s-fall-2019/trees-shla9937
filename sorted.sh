for i in $(seq 10000 $END); do echo $((1 + RANDOM % 1000)) $((1 + RANDOM % 1000)) ; done | sort -n > sorted.txt