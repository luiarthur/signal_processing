name := "gui"

version := "0.1.0"

scalaVersion := "2.11.8"

libraryDependencies ++= Seq(
  // Breeze (Numeric Lib)
  "org.scalanlp" %% "breeze" % "0.13.2",
  "org.scalanlp" %% "breeze-natives" % "0.13.2",
  // ScalaFX (GUI)
  "org.scalafx" %% "scalafx" % "8.0.92-R10",
  // ScalaTest (testing this package)
  "org.scalatest" %% "scalatest" % "3.0.0" % "test"
)

