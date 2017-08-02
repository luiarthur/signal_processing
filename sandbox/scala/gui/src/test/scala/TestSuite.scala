import org.scalatest.FunSuite

class TestSuite extends FunSuite {
  import breeze.linalg._
  import breeze.signal._
  import gui.util.timer

  test("dummy") { 
    val N = 2E3
    val x = DenseVector.tabulate(N.toInt)(i => scala.util.Random.nextGaussian)
    val f = fourierTr(x)
    timer { println(f(0)) }
    assert(true) 
  }
  

}
