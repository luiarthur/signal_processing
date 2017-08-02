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
  }
  
  test("Read embraceableYou.wav") { 
    import java.nio.file.{Files, Paths}
    val path = getClass.getResource("/embraceableYou.wav").getPath
    println("Reading: " + path)
    val byteArray = Files.readAllBytes(Paths.get(path))

    //def takeEvery(x:Array[Byte], n: Int) = x.grouped(n).flatMap(_.take(n-1)).toList
    //val x = takeEvery(byteArray, 2)
    //val x = byteArray.zipWithIndex.filter(_._2 % 2 == 1).map(_._1)

    //import javax.sound.sampled._
    //val stream = getClass.getResourceAsStream("/embraceableYou.wav") // works in console mode when the wav is in main/resources
    //val audioIn = AudioSystem.getAudioInputStream(stream)
    //val clip = AudioSystem.getClip
    //clip.open(audioIn)
    //clip.start
    //clip.close
  }
 
}
