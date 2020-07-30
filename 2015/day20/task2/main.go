package main

import (
    "fmt"
    "io/ioutil"
    "strconv"
)

func readInput() int {
    data, _ := ioutil.ReadFile("input")
    num, _ := strconv.Atoi(string(data))
    return num
}

func divisors(n int) ([]int) {
    divs := []int{}
	for i := 1; i * i <= n; i++ {
        if n % i == 0 {
            if n == i * i {
                divs = append(divs, i)
            } else {
                divs = append(divs, i)
                divs = append(divs, n / i)
            }
        }
    }
	return divs
}

func countHousePresents(house int) int {
    presents := 0
    divs := divisors(house)
    for _, d := range divs {
        if house / d - 1 <= 50 {
            presents += 11 * d
        }
    }
    return presents
}

func getHouseWithPresents(count int) int {
    h := 1
    for true {
        p := countHousePresents(h)
        if p >= count {
            break
        }
        h += 1
    }
    return h
}

func main() {
    target := readInput()
    houseId := getHouseWithPresents(target)
    fmt.Println(houseId)
}