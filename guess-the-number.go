package main

import (
	"bufio"
	"fmt"
	"log"
	"math/rand"
	"os"
	"strconv"
	"strings"
)

func main() {
	log.Println("guess the number stared.")

	var (
		guess int
		err   error
		num   = 0
		moves = 10
	)
	reader := bufio.NewReader(os.Stdin)

	num = rand.Intn(700-300) + 300

	for {

		log.Println("Make a guess (only numbers)[" + strconv.Itoa(num) + "]: ")
		input, _ := reader.ReadString('\n')
		input = strings.Replace(input, "\n", "", 1)

		guess, err = strconv.Atoi(input)

		if err != nil {
			log.Println("not a number.. retry..")
			continue
		}

		switch true {
		case guess == num:
			log.Println("correct!!!")
			return
		case guess-num >= 0 && guess-num <= 50:
			log.Println("Little smaller than the original answer")
		case num-guess >= 0 && num-guess <= 50:
			log.Println("Little greater than the original answer")
		case guess-num >= 0 && guess-num <= 200:
			log.Println("smaller than the original answer")
		case num-guess >= 0 && num-guess <= 200:
			log.Println("greater than the original answer")
		}

		moves = moves - 1

		if moves == 0 {
			return
		}

		log.Println(fmt.Sprintf("You have %d moves left.\n\n", moves))
	}
}

