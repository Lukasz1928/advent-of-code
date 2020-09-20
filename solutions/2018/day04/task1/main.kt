import java.io.File
import java.io.InputStream
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.time.temporal.ChronoUnit

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

fun findGuardsSleepTime(records: List<Record>): Map<Int, Int> {
    val guardIds = records.map { it.guardId }.filter { it > 0 }.toSet()
    val times = guardIds.map { it to 0 }.toMap().toMutableMap()
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
            val sleepTime = fallAsleepTime.until(rec.date, ChronoUnit.MINUTES).toInt()
            times[currentGuard] = times[currentGuard]!! + sleepTime
        }
    }
    return times
}

fun findGuardWithMostMinutesSlept(times: Map<Int, Int>): Int {
    return times.toList().maxBy { it.second }!!.first
}

fun findGuardsMostSleepyMinute(records: List<Record>, guardId: Int): Int {
    var minutes = listOf<Int>().toMutableList()
    for(i in 0..59) {
        minutes.add(0)
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
            if(currentGuard == guardId) {
                val startMin = fallAsleepTime.minute
                val endMin = rec.date.minute
                for(m in startMin until endMin) {
                    minutes[m] = minutes[m] + 1
                }
            }
        }
    }
    return minutes.indexOf(minutes.max())
}

fun main() {
    val records = sortRecords(readInput())
    val sleepTimes = findGuardsSleepTime(records)
    val guardWithMostTimeSlept = findGuardWithMostMinutesSlept(sleepTimes)
    val mostSleepyMinute = findGuardsMostSleepyMinute(records, guardWithMostTimeSlept)
    val result = mostSleepyMinute * guardWithMostTimeSlept
    println(result)
}