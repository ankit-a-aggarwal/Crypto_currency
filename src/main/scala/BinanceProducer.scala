import akka.Done
import akka.actor._
import akka.http.scaladsl._
import akka.http.scaladsl.model.StatusCodes._
import akka.http.scaladsl.model.headers.Accept
import akka.http.scaladsl.model.{HttpRequest, HttpResponse, MediaRanges}
import akka.stream._
import akka.stream.scaladsl.{Sink, Source}
import akka.util.ByteString

import scala.concurrent.Future
import scala.concurrent.Await
import scala.concurrent.duration.Duration
import java.util.concurrent.TimeUnit
import akka.http.scaladsl.model.ws.Message
import akka.http.scaladsl.model.ws.TextMessage
import akka.NotUsed
import akka.http.scaladsl.model.ws.WebSocketRequest
import akka.stream.scaladsl.Flow
import akka.stream.scaladsl.Keep
import akka.http.scaladsl.model.StatusCodes
import scala.concurrent.Promise

object BinanceWebSocket {

  def main(args: Array[String]): Unit = {
    implicit val actorSystem = ActorSystem("binance-websocket")
    implicit val materializer = ActorMaterializer()
    import actorSystem.dispatcher

    val flow: Flow[Message, Message, Promise[Option[Message]]] =
      Flow.fromSinkAndSourceMat(
        Sink.foreach[Message](
          record => {
            println(record.asInstanceOf[TextMessage].getStrictText)
          }
        ), Source.maybe[Message]) (Keep.right)

    val (upgradeResponse, closed) =
      Http().singleWebSocketRequest(
        WebSocketRequest("wss://stream.binance.com:9443/ws/xvgbtc@trade"),
        flow
      )

    val connected = upgradeResponse.map {
      upgrade => 
      if(upgrade.response.status == StatusCodes.SwitchingProtocols){
        Done
      } else{
        throw new RuntimeException(s"Connection failed : ${upgrade.response.status}")
      }
    }

    connected.onComplete(println)
  }

}
