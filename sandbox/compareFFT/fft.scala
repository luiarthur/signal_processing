import scala.math.{ Pi, cos, sin, cosh, sinh, abs, pow}

/** times the execution of a block and returns 
 *  the result of the block 
 */
def timer[R](block: => R): R = {  
  val t0 = System.nanoTime()
  val result = block
  val t1 = System.nanoTime()
  println("Elapsed time: " + (t1 - t0) / 1E9 + "s")
  result
}

 
case class Complex(re: Double, im: Double=0) {
    def +(x: Complex): Complex = Complex(re + x.re, im + x.im)
    def -(x: Complex): Complex = Complex(re - x.re, im - x.im)
    def *(x: Double):  Complex = Complex(re * x, im * x)
    def *(x: Complex): Complex = Complex(re * x.re - im * x.im, re * x.im + im * x.re)
    def /(x: Double):  Complex = Complex(re / x, im / x)
 
    override def toString(): String = {
        val a = "%1.3f" format re
        val b = "%1.3f" format abs(im)
        (a,b) match {
            case (_, "0.000") => a
            case ("0.000", _) => b + "i"
            case (_, _) if im > 0 => a + " + " + b + "i"
            case (_, _) => a + " - " + b + "i"
        }
    }
}
 
def exp(c: Complex) : Complex = {
    val r = (cosh(c.re) + sinh(c.re))
    Complex(cos(c.im), sin(c.im)) * r
}

def _fft(cSeq: Seq[Complex], direction: Complex, scalar: Int): Seq[Complex] = {
    if (cSeq.length == 1) {
        return cSeq
    }
    val n = cSeq.length
    assume(n % 2 == 0, "The Cooley-Tukey FFT algorithm only works when the length of the input is even.")
 
    lazy val evenOddPairs = cSeq.grouped(2).toSeq
    lazy val evens = _fft(evenOddPairs map (_(0)), direction, scalar)
    lazy val odds  = _fft(evenOddPairs map (_(1)), direction, scalar)
 
    def leftRightPair(k: Int): (Complex, Complex) = {
        lazy val base = evens(k) / scalar
        lazy val offset = exp(direction * (Pi * k / n)) * odds(k) / scalar
        (base + offset, base - offset)
    }
 
    lazy val pairs = (0 until n/2) map leftRightPair
    lazy val left  = pairs map (_._1)
    lazy val right = pairs map (_._2)
    left ++ right
}
 
def  fft(cSeq: Seq[Complex]): Seq[Complex] = _fft(cSeq, Complex(0,  2), 1)
def rfft(cSeq: Seq[Complex]): Seq[Complex] = _fft(cSeq, Complex(0, -2), 2)

//val data = Seq.tabulate(1E7.toInt)(i => Complex(math.sin(i)))
//val data = Seq.tabulate(pow(2,24).toInt)(i => Complex(math.sin(i)))

val smallDat =  Seq.tabulate(pow(2,12).toInt)(i => Complex(math.sin(i)))
val data = Seq.tabulate(pow(2,19).toInt)(i => Complex(math.sin(i)))

val z = {
  val warmup = { 
    val x = fft(smallDat) 
    val y = rfft(fft(smallDat))
  }

  timer { val x = fft(smallDat) }
  timer { val y = rfft(fft(smallDat)) }
}

println("N: " + data.size)

timer { 
  val x = fft(data)
}

timer { 
  val y = rfft(fft(data))
}


