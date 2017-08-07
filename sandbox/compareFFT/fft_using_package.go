package main

import (
	"fmt"
	"github.com/mjibson/go-dsp/fft"
	"math"
)

func main() {
	const n = 10000000
	x := make([]float64, n)
	for i := 0; i < n; i++ {
		x[i] = math.Sin(float64(i))
	}

	//fmt.Println(fft.FFTReal([]float64{1, 2, 3}))
	fmt.Println("START")
	y := fft.FFTReal(x)
	//fmt.Println(fft.FFTReal(x))
	fmt.Println(y[0])
	fmt.Println("DONE")
}
