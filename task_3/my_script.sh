#!/bin/bash

filename=$1
output=$2


word_count=$(sed 's/[^[:alpha:]]/ /g' "$filename" | tr '[:upper:]' '[:lower:]' | awk '{ for (i=1; i<=NF; i++) { print $i } }' | sort | uniq -c)

echo "Word count result:"
echo "$word_count"


top_words=$(echo "$word_count" | sort -nr | head -n 10)

while read -r line; do
    count=$(echo "$line" | awk '{print $1}')
    word=$(echo "$line" | awk '{print $2}')
    touch "$output/${word}_${count}"
done <<< "$top_words"
