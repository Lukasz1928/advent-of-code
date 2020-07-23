import scala.collection.mutable.ListBuffer
import scala.io.Source
import scala.util.matching.Regex

object Main {
    def main(args: Array[String]): Unit = {
        val rectangles = parseInput()
        val result = calculateOverlap(rectangles)
        println(result)
    }

    def calculateOverlap(rectangles: List[Rectangle]): Int = {
        var distinctSquares = Set[(Int, Int)]()
        var overlapping = Set[(Int, Int)]()
        rectangles.foreach(rect => {
            val squares = rect.getAllSquares
            squares.foreach(sq => {
                if(distinctSquares.contains(sq)) {
                    overlapping = overlapping + sq
                }
            })
            distinctSquares = distinctSquares ++ rect.getAllSquares
        })
        overlapping.size
    }

    case class Rectangle(id: Int,
                         x: Int, y: Int,
                         width: Int, height: Int) {
        override def toString: String = {
            s"$id: ($x, $y), [$width, $height]"
        }

        def getAllSquares: List[(Int, Int)] = {
            val squares = new ListBuffer[(Int, Int)]
            for(i <- x.until(x + width)) {
                for(j <- y.until(y + height)) {
                    squares.addOne((i, j))
                }
            }
            squares.toList
        }
    }

    def parseLine(line: String): Rectangle = {
        val pattern = new Regex("#(\\d+) @ (\\d+),(\\d+): (\\d+)x(\\d+)", "id", "x", "y", "width", "height")
        val m = pattern.findAllIn(line)
        Rectangle(m.group("id").toInt,
            m.group("x").toInt,
            m.group("y").toInt,
            m.group("width").toInt,
            m.group("height").toInt)
    }

    def parseInput(): List[Rectangle] = {
        val inputFile = "input"
        val source = Source.fromFile(inputFile)
        var rectangles = new ListBuffer[Rectangle]
        for(line <- source.getLines()) {
            rectangles += parseLine(line)
        }
        source.close()
        rectangles.toList
    }
}
