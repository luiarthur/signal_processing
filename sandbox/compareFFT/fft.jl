n = 1E7
x = sin.(1:n)
y = fft(x[1:10])
@time y = fft(x)

print(y[123456 + 1])
