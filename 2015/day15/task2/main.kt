import java.io.File
import java.io.InputStream

class Ingridient(val name: String, val params: List<Int>)

fun readInput(): List<Ingridient> {
    val r = Regex("(\\w+): (.*)")
    val propr = Regex("capacity (-?\\d+), durability (-?\\d+), flavor (-?\\d+), texture (-?\\d+), calories (-?\\d+)")
    val inputStream: InputStream = File("input").inputStream()
    val lines = mutableListOf<Ingridient>()
    inputStream.bufferedReader().forEachLine {
        val rmatch = r.find(it)
        val name = rmatch!!.groupValues[1]
        val proprmatch = propr.find(rmatch.groupValues[2])
        lines.add(Ingridient(name, listOf(proprmatch!!.groupValues[1].toInt(), proprmatch.groupValues[2].toInt(),
                                          proprmatch.groupValues[3].toInt(), proprmatch.groupValues[4].toInt(),
                                          proprmatch.groupValues[5].toInt())))
    }
    return lines
}

fun generateTuplesWithConstantSum(elems: Int, sum: Int): List<List<Int>> {
    if(elems == 1) {
        return listOf(listOf(sum))
    }
    val tuples = mutableListOf<List<Int>>()
    for(i in 0..sum) {
        val subtuples = generateTuplesWithConstantSum(elems - 1, sum - i)
        for(st in subtuples) {
            tuples.add(listOf(i) + st)
        }
    }
    return tuples
}

fun calculateValue(ingridients: List<Ingridient>, amounts: List<Int>): Int {
    val vals = ingridients[0].params.map {0}.toMutableList()
    for(i in 0 until ingridients.size) {
        for(j in 0 until (ingridients[0].params.size)) {
            vals[j] += ingridients[i].params[j] * amounts[i]
        }
    }
    if(vals[vals.size - 1] != 500) {
        return -1
    }
    return vals.subList(0, vals.size - 1).map { if(it > 0) it else 0 }.reduce {acc, i -> acc * i}
}

fun findBestTotalScore(data: List<Ingridient>): Int {
    val cnt = data.size
    val tuples = generateTuplesWithConstantSum(cnt, 100)
    var bestValue = -1
    for(t in tuples) {
        val value = calculateValue(data, t)
        if(value > bestValue) {
            bestValue = value
        }
    }
    return bestValue
}

fun main() {
    val data = readInput()
    val result = findBestTotalScore(data)
    print(result)
}