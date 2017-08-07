package main

import (
	"fmt"
	"math"
	"math/cmplx"
)

func ditfft2(x []float64, y []complex128, n, s int) {
	if n == 1 {
		y[0] = complex(x[0], 0)
		return
	}
	ditfft2(x, y, n/2, 2*s)
	ditfft2(x[s:], y[n/2:], n/2, 2*s)
	for k := 0; k < n/2; k++ {
		tf := cmplx.Rect(1, -2*math.Pi*float64(k)/float64(n)) * y[k+n/2]
		y[k], y[k+n/2] = y[k]+tf, y[k]-tf
	}
}

func main() {
	//x := []float64{1, 1, 1, 1, 0, 0, 0, 0}
	const N = 10000000
	x := make([]float64, N)
	for i := 0; i < N; i++ {
		x[i] = math.Sin(float64(i))
	}
	y := make([]complex128, len(x))
	fmt.Printf("Starting FFT")
	ditfft2(x, y, len(x), 1)
	fmt.Printf("Done with FFT")

	fmt.Printf("%8.4f\n", y[123456])
	//for _, c := range y {
	//    fmt.Printf("%8.4f\n", c)
	//}
}
