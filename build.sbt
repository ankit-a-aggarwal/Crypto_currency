name := "Crypto Kafka Publisher"
version := "1.0"
val AkkaVersion = "2.6.8"
val AkkaHttpVersion = "10.1.11"
val AlpakkaVersion = "2.0.0"
val AlpakkaKafkaVersion = "2.0.2"

libraryDependencies ++= Seq(
  "org.apache.kafka" %% "kafka-streams-scala" % "2.5.0",
  "com.lightbend.akka" %% "akka-stream-alpakka-csv" % AlpakkaVersion,
  "com.typesafe.akka" %% "akka-stream-kafka" % AlpakkaKafkaVersion,
  "com.typesafe.akka" %% "akka-actor-typed" % AkkaVersion,
  "com.typesafe.akka" %% "akka-stream" % AkkaVersion,
  "com.typesafe.akka" %% "akka-http" % AkkaHttpVersion,
  "com.typesafe.akka" %% "akka-http-spray-json" % AkkaHttpVersion,
  "com.fasterxml.jackson.datatype" % "jackson-datatype-jdk8" % "2.10.3",
  "com.fasterxml.jackson.datatype" % "jackson-datatype-jsr310" % "2.10.3",
  "org.testcontainers" % "kafka" % "1.14.1",
  "com.typesafe.akka" %% "akka-slf4j" % AkkaVersion,
  "ch.qos.logback" % "logback-classic" % "1.2.3"
)