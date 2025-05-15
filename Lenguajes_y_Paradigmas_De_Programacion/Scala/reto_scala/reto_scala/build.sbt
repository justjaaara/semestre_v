ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "3.3.5"

lazy val root = (project in file("."))
  .settings(
    name := "reto_scala",
    libraryDependencies += "com.typesafe.play" %% "play-json" % "2.10.0"
  )
