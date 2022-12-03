package main

import (
    "bufio"
    "fmt"
    "log"
    "os"
    "strconv"
    "sort"
)

var input_path = "input.txt"

type Elf struct {
    snacks []int
}

func (elf *Elf) AddSnack(snack int) {
    elf.snacks = append(elf.snacks, snack)
}

func (elf Elf) SnackValue() int {
    return sum(elf.snacks)
}



func main() {
    elves := ReadInput()

    sort.Slice(elves, func(i, j int) bool { return elves[i].SnackValue() > elves[j].SnackValue() })

    fmt.Printf("Most stacked elf: %s\n", strconv.Itoa(elves[0].SnackValue()))
    fmt.Printf("Second most stacked elf: %s\n", strconv.Itoa(elves[1].SnackValue()))
    fmt.Printf("Third most stacked elf: %s\n", strconv.Itoa(elves[2].SnackValue()))

    fmt.Printf("Sum of top 3: %s\n", strconv.Itoa(elves[0].SnackValue() + elves[1].SnackValue() + elves[2].SnackValue()))

}

func ReadInput() []Elf {
    file, error := os.Open(input_path)

    if error != nil {
        log.Fatal(error)
    }

    // Close the file
    defer file.Close()

    scanner := bufio.NewScanner(file)

    elves := []Elf{}
    elf := Elf{}
    for scanner.Scan() {
        snack_text := scanner.Text()

        snack_value, error := strconv.Atoi(snack_text)

        if error != nil {
            elves = append(elves, elf)
            elf = Elf{}
            continue
        }

        elf.AddSnack(snack_value)
    }

    elves = append(elves, elf)

    return elves
}

func sum(array []int) int {
    result := 0
    for _, value := range array {
        result += value
    }

    return result
}