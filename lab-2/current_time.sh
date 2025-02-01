
start_time="09:00"
end_time="18:00"

current_time=$(date +%s)
time_to_start=$(( $(date -d $start_time +%s) - $current_time ))
time_to_end=$(( $(date -d $end_time +%s) - $current_time ))

echo -n "it's currently $(date -d \@$current_time +%H:%M)."

if [ $time_to_start -gt 0 ]; then
    echo " your work day hasn't started yet."
elif [ $time_to_end -le 0 ]; then
    echo " your work day is done."
else
    hours_left=$((time_to_end / 3600))
    minutes_left=$(((time_to_end % 3600) / 60))
    echo " you have $hours_left hours and $minutes_left minutes left in your work day."
fi
