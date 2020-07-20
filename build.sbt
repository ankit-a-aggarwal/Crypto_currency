name := "Crypto Kafka Publisher"
version := "1.0"
val AkkaVersion = "2.6.8"

libraryDependencies += "org.apache.kafka" %% "kafka-streams-scala" % "2.5.0"
libraryDependencies += "com.typesafe.akka" %% "akka-stream" % AkkaVersion