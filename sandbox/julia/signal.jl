#= Install Packages
Pkg.init() # only needed if this is the first time you are dealing with packages
Pkg.update()
Pkg.add("DSP")
Pkg.add("WAV")
Pkg.add("PyCall")
Pkg.build("PyCall")
Pkg.add("PyPlot")
=#

using WAV

# Loading and plotting an audio signal
@time s, fs = wavread("/Users/lui9/wav/embraceableYou.wav");

size(s)

# Plot
#plot(0:1/fs:(length(s)-1)/fs, s)
#xlabel("Time [s]")


### BLINK GUI in browser
using Blink
w = Window() # Open a new window
body!(w, "Hello World") # Set the body content
loadurl(w, "http://julialang.org"); # Load a web page
loadurl(w, "http://luiarthur.github.io"); # Load a web page
@js w Math.log(10)
@js w console.log("hello, web-scale world")
@js w console.log("hello, BLA world")
bla = "KAJSHDKSAD"
@js w console.log($(s[1,1]))
@js w console.log($bla)

