#!/bin/bash

echo "Monitoring memory for 5 minutes..."
echo "Warning will be shown if free memory < 500MB."
echo

count=0

while [ $count -lt 30 ]  # 30 checks × 10 seconds = 5 minutes
do
    free_mem=$(free -m | awk ' {print $4}' | head -2 | tail -1 )
    echo "Free memory: ${free_mem}MB"

    if [ "$free_mem" -lt 500 ]; then
        echo " WARNING: Free memory is below 500MB!"
    fi

    sleep 1
    count=$((count + 1))
done

echo "Done monitoring."

