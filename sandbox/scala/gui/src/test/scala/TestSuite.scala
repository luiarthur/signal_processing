import org.scalatest.FunSuite

class TestSuite extends FunSuite {
  // TODO: Try scalaFX + ScalaCollider?
  import breeze.linalg._
  import breeze.signal._
  import gui.util.timer

  val runtime = Runtime.getRuntime
  val mb = 1024 * 1024
  println("Total Memory: " + runtime.maxMemory / mb + "MB")
  println("Free Memory:  " + runtime.freeMemory / mb  + "MB")

  test("dummy") { 
    val N = 4096
    val x = DenseVector.tabulate(N.toInt)(i => scala.util.Random.nextGaussian)
    val f = timer{ fourierTr(x) }
    val g = timer{ fourierTr(x) }
    timer { println(f(0)) }
  }
  
  test("Read embraceableYou.wav") { 
    // See: https://stackoverflow.com/questions/9438718/playing-wav-files-in-scala
    import java.nio.file.{Files, Paths}
    import breeze.linalg._
    import breeze.signal._
    import scala.collection.parallel.immutable.ParVector

    println("Total Memory: " + runtime.totalMemory / mb + "MB")

    timer {
      val path = getClass.getResource("/embraceableYou.wav").getPath
      println("Reading: " + path)
      //val x = Files.readAllBytes(Paths.get(path))

      // Only if Large enough heap size
      // https://github.com/sbt/sbt/issues/2945
      // export SBT_OPTS="-Xmx2G -XX:+UseConcMarkSweepGC -XX:+CMSClassUnloadingEnabled -XX:MaxPermSize=2G -Xss2M  -Duser.timezone=GMT"
      lazy val y = {
        val x = timer { Files.readAllBytes(Paths.get(path)).map(_.toDouble) }
        new DenseMatrix(x.size/2, 2, x) 
      }
    
      val N = y.size
      val windowSize = 4096

      val f = timer { 
        ParVector.tabulate(N / windowSize / 2){i =>
        //Vector.tabulate(N / windowSize / 2){i =>
          val lower = i * windowSize
          val upper = (i + 1) * windowSize
          val z = y(lower until upper, 0).toDenseVector
          fourierTr(z)
        }//.flatten
      }

      println(f(0).size)
      println("Free Memory:  " + runtime.freeMemory / mb  + "MB")
    }

    println("Free Memory:  " + runtime.freeMemory / mb  + "MB")

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
