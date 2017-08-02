name := "gui"

version := "0.1.0"

scalaVersion := "2.11.8"

libraryDependencies ++= Seq(
  // javax (read media)
  "javax" % "javaee-api" % "7.0" % "provided",
  // Breeze (Numeric Lib)
  "org.scalanlp" %% "breeze" % "0.13.2",
  "org.scalanlp" %% "breeze-natives" % "0.13.2",
  // ScalaFX (GUI)
  //"org.scalafx" %% "scalafx" % "2.2.76-R11", // for java(7)
  "org.scalafx" %% "scalafx" % "8.0.92-R10", // for java(8)
  // ScalaTest (testing this package)
  "org.scalatest" %% "scalatest" % "3.0.0" % "test"
)

resolvers += Opts.resolver.sonatypeSnapshots

// Allows multiple runs within an sbt session
fork in run := true
