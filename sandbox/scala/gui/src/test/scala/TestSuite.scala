import org.scalatest.FunSuite

class TestSuite extends FunSuite {
  // TODO: Try scalaFX + ScalaCollider?
  import breeze.linalg._
  import breeze.signal._
  import gui.util.timer

  test("dummy") { 
    val N = 2E3
    val x = DenseVector.tabulate(N.toInt)(i => scala.util.Random.nextGaussian)
    val f = fourierTr(x)
    timer { println(f(0)) }
  }
  
  test("Read embraceableYou.wav") { 
    // See: https://stackoverflow.com/questions/9438718/playing-wav-files-in-scala
    import java.nio.file.{Files, Paths}
    import breeze.linalg._
    import breeze.signal._

    timer {
      val path = getClass.getResource("/embraceableYou.wav").getPath
      println("Reading: " + path)
      lazy val x = Files.readAllBytes(Paths.get(path)).map(_.toDouble)
      lazy val y = new DenseMatrix(x.size/2,2,x)
      val z = y(::,0).toDenseVector
      println(z.length)
      //val f = fourierTr(z)
    }

    //def takeEvery(x:Array[Byte], n: Int) = x.grouped(n).flatMap(_.take(n-1)).toList
    //val y = takeEvery(x, 2)
    //val y = x.zipWithIndex.filter(_._2 % 2 == 1).map(_._1)

    //import javax.sound.sampled._
    //val stream = getClass.getResourceAsStream("/embraceableYou.wav") // works in console mode when the wav is in main/resources
    //val audioIn = AudioSystem.getAudioInputStream(stream)
    //val clip = AudioSystem.getClip
    //clip.open(audioIn)
    //clip.start
    //clip.close
  }

 
}
