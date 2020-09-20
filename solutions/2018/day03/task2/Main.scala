import scala.collection.mutable.ListBuffer
import scala.io.Source
import scala.util.matching.Regex

object Main {
    def main(args: Array[String]): Unit = {
        val rectangles = parseInput()
        val claims = calculateClaims(rectangles)
        val distinct = findDistinctRectangle(rectangles, claims)
        val result = distinct.id
        print(result)
    }

    def findDistinctRectangle(rectangles: List[Rectangle], claims: Map[(Int, Int), List[Int]]): Rectangle = {
        var result: Rectangle = null
        rectangles.foreach(rect => {
            val sq = rect.getAllSquares
            var distinct = true
            sq.foreach(s => {
                if(claims(s).size != 1) {
                    distinct = false
                }
            })
            if(distinct) {
                result = rect
            }
        })
        result
    }

    def calculateClaims(rectangles: List[Rectangle]): Map[(Int, Int), List[Int]] = {
        var distinctSquares = Set[(Int, Int)]()
        var claimsOfSquare = Map[(Int, Int), List[Int]]()
        rectangles.foreach(rect => {
            val squares = rect.getAllSquares
            squares.foreach(sq => {
                if(claimsOfSquare.contains(sq)) {
                    claimsOfSquare = (claimsOfSquare - sq) + (sq -> (claimsOfSquare(sq) ::: List(rect.id)))
                }
                else {
                    val b = new ListBuffer[Int]()
                    b.addOne(rect.id)
                    claimsOfSquare = claimsOfSquare + (sq -> b.toList)
                }
            })
            distinctSquares = distinctSquares ++ rect.getAllSquares
        })
        claimsOfSquare
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
