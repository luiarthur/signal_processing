n <- 1E7
x <- sin(1:n)
print( system.time(fft(x)) )
