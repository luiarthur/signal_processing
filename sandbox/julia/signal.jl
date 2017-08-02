#= Install Packages
Pkg.init() # only needed if this is the first time you are dealing with packages
Pkg.update()
Pkg.add("DSP")
Pkg.add("WAV")
Pkg.add("PyCall")
Pkg.build("PyCall")
Pkg.add("PyPlot")
=#

using DSP, WAV, PyPlot

# Loading and plotting an audio signal
s, fs = wavread("/Users/lui9/wav/embraceableYou.wav")

plot(0:1/fs:(length(s)-1)/fs, s)
xlabel("Time [s]")
