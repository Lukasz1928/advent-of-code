import java.io.File
import java.io.InputStream
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter

fun readInput(): List<Record> {
    val inputStream: InputStream = File("input").inputStream()
    val lines = mutableListOf<String>()
    inputStream.bufferedReader().forEachLine { lines.add(it) }
    return lines.toList().map { parseLine(it) }
}

fun parseLine(line: String): Record {
    val idx = line.lastIndexOf(']')
    return Record(line.subSequence(1, idx).toString(), line.substring(idx + 2))

}

fun parseDate(date: String) : LocalDateTime {
    val formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm")
    return LocalDateTime.parse(date, formatter)
}

enum class Event {
    BEGIN_SHIFT, FALL_ASLEEP, WAKE_UP;

    companion object {
        fun fromString(str: String): Event {
            if(str == "falls asleep") {
                return FALL_ASLEEP
            }
            else if(str == "wakes up") {
                return WAKE_UP
            }
            return BEGIN_SHIFT
        }
    }
}

fun getGuardId(str: String): Int {
    val r = Regex("Guard #(\\d+) begins shift")
    val match = r.find(str)
    return match!!.groupValues[1].toInt()
}

class Record(val date: LocalDateTime, val event: Event, var guardId: Int = -1) {
    constructor(eventDate: String, eventDescription: String) : this(parseDate(eventDate), Event.fromString(eventDescription)) {
        if(event == Event.BEGIN_SHIFT) {
            guardId = getGuardId(eventDescription)
        }
    }
}

fun sortRecords(records: List<Record>): List<Record> {
    return records.sortedWith(compareBy {it.date})
}

fun findGuardsSleepTime(records: List<Record>): Map<Int, List<Int>> {
    val guardIds = records.map { it.guardId }.filter { it > 0 }.toSet()
    val times = guardIds.map { it to listOf<Int>().toMutableList() }.toMap().toMutableMap()
    for(id in guardIds) {
        for(i in 0..59) {
            times[id]!!.add(0)
        }
    }
    var currentGuard = -1
    var fallAsleepTime: LocalDateTime = LocalDateTime.now()
    for(rec in records) {
        if(rec.event == Event.BEGIN_SHIFT) {
            currentGuard = rec.guardId
        }
        if(rec.event == Event.FALL_ASLEEP) {
            fallAsleepTime = rec.date
        }
        if(rec.event == Event.WAKE_UP) {
            val startMin = fallAsleepTime.minute
            val endMin = rec.date.minute - 1
            for(m in startMin..endMin) {
                times[currentGuard]!![m] = times[currentGuard]!![m] + 1
            }
        }
    }
    return times
}

fun calculateResult(sleepTimes: Map<Int, List<Int>>): Int {
    var maxGuard: Int = -1
    var maxMinute: Int = -1
    var maxValue: Int = -1
    for(g in sleepTimes.keys) {
        for(t in 0..59) {
            val sleepTime = sleepTimes[g]!![t]
            if(sleepTime > maxValue) {
                maxValue = sleepTime
                maxGuard = g
                maxMinute = t
            }
        }
    }
    return maxGuard * maxMinute
}


fun main() {
    val records = sortRecords(readInput())
    val sleepTimes = findGuardsSleepTime(records)
    val result = calculateResult(sleepTimes)
    print(result)
}