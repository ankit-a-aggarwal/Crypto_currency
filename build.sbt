name := "Crypto Kafka Publisher"
version := "1.0"
resolvers += "jgit-repository" at "http://download.eclipse.org/jgit/maven"
//resolvers += "apache" at "https://mvnrepository.com/artifact/org.apache.kafka"
// https://mvnrepository.com/artifact/org.apache.kafka/kafka-streams-scala
libraryDependencies += "org.apache.kafka" %% "kafka-streams-scala" % "2.5.0"
