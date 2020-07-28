#!/bin/bash

# slowest possible solution, but at least it works
arraySideSize=100
steps=100
data=()

function readInput {
    rawInput=`cat input`
    SAVEIFS=$IFS
    IFS=$'\n'
    lines=($rawInput)
    IFS=$SAVEIFS
    t=()
    for (( i=0; i<arraySideSize; i++ )); do
        l="${lines[$i]}"
        for ((j=0; j<arraySideSize; j++)); do
            c="${l:$j:1}"
            if [ "$c" = "#" ]; then
                data+=(1)
            else
                data+=(0)
            fi
        done
    done
}

function countOnNeighbours {
    locx="$1"
    locy="$2"
    count=0
    for (( i=locx-1; i<=locx+1; i++)); do
        for (( j=locy-1; j <= locy+1; j++)); do
            if [ "$i" -ge 0 ] && [ "$i" -lt "$arraySideSize" ]; then
                if [ "$j" -ge 0 ] && [ "$j" -lt "$arraySideSize" ]; then
                    idx=$((arraySideSize*i+j))
                    if [ "${data[$idx]}" -eq 1 ]; then
                        ((count++))
                    fi
                fi
            fi
        done
    done
    echo "$count"
}

function step {
    newData=()
    for ((i=0; i<arraySideSize; i++)); do
        for ((j=0; j<arraySideSize; j++)); do
            idx=$((arraySideSize*i+j))
            if [ "${data[$idx]}" -eq 1 ]; then
                cnt=$( countOnNeighbours "$i" "$j" )
                ((cnt--))
                if [ "$cnt" -eq 2 ] || [ "$cnt" -eq 3 ]; then
                    newData+=(1)
                else
                    newData+=(0)
                fi
            else
                cnt=$( countOnNeighbours "$i" "$j" )
                if [ "$cnt" -eq 3 ]; then
                    newData+=(1)
                else
                    newData+=(0)
                fi
            fi
        done
    done
    data=( "${newData[@]}" )
}

function printa {
    for ((i=0; i<arraySideSize; i++)); do
        for ((j=0; j<arraySideSize; j++)); do
            idx=$((arraySideSize*i+j))
            d="${data[$idx]}"
            printf "$d"
        done
        printf "\n"
    done
    printf "\n"
}

function countOn {
    cnt=0
    for ((i=0; i<arraySideSize; i++)); do
        for ((j=0; j<arraySideSize; j++)); do
            idx=$((arraySideSize*i+j))
            if [ "${data[$idx]}" -eq 1 ]; then
                ((cnt++))
            fi
        done
    done
    echo "$cnt"
}

readInput
echo "$steps"
for ((s=0; s<steps; s++)); do
    step
done
result=$( countOn )
echo "$result"
