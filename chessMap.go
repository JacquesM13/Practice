package main
import "fmt"
import "strings"
import "strconv"


func main() {
	run()
}

func run() string {

	// Test values:

	C := 25
	R := 11
	startPosition := "5a"
	// should end 8b - does
	

	// C := 33
	// R := 7
	// startPosition := "6b"
	// should end 5c - does

	// C := 71
	// R := 4
	// startPosition := "8h"
	// should end 4g - does

	var endPosition string
	var endR int
	var endC int

	abc := make(map[string]int)
	abc["a"] = 1
	abc["b"] = 2
	abc["c"] = 3
	abc["d"] = 4
	abc["e"] = 5
	abc["f"] = 6
	abc["g"] = 7
	abc["h"] = 8

	abc2 := make(map[int]string)
	abc2[1] = "a"
	abc2[2] = "b"
	abc2[3] = "c"
	abc2[4] = "d"
	abc2[5] = "e"
	abc2[6] = "f"
	abc2[7] = "g"
	abc2[8] = "h"


	res := strings.Split(startPosition, "")

	startR, err := strconv.Atoi(res[0])
	if err != nil {
        // ... handle error
    	} 

	startC := abc[res[1]]

	R = R % 8 // remainder will be actual number of squares moved
	C = C % 8

	if R + startR > 8 { // handle moving beyond edge of board
		endR = startR + R - 8
	} else {
		endR = startR + R
	}

	if C + startC > 8 {
		endC = startC + C - 8
	} else {
		endC = startC + C
	}

	endRStr := strconv.Itoa(endR)
	endPosition += endRStr
	endPosition += abc2[endC]


	fmt.Println(endPosition)
	return endPosition
	
}

