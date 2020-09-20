import scala.collection.mutable.ListBuffer
import scala.io.Source
import scala.util.matching.Regex

object Main {
    def main(args: Array[String]): Unit = {
        val preferences = parseInput()
        val extendedPreferences = extendPreferences(preferences)
        val result = calculateMaximalHappinessGain(extendedPreferences)
        print(result)
    }

    case class Preference(from: String, to: String, value: Int) {

    }

    def extendPreferences(preferences: List[Preference]): List[Preference] = {
        val people = getPeopleList(preferences)
        val extension = people.map(p => Preference(p, "me", 0)) ::: people.map(p => Preference("me", p, 0))
        preferences ::: extension
    }

    def findPreferenceValue(preferences: List[Preference], from: String, to: String): Int = {
        preferences.filter(p => p.from == from && p.to == to).head.value
    }

    def calculateConfigurationGain(preferences: List[Preference], config: List[String]): Int = {
        var gain = 0
        val cyclicConfig = List(config.last) ::: config ::: List(config.head)
        for(i <- 1 until (cyclicConfig.length - 1)) {
            val person = cyclicConfig(i)
            val lngh = cyclicConfig(i - 1)
            val rngh = cyclicConfig(i + 1)
            gain += findPreferenceValue(preferences, person, lngh) + findPreferenceValue(preferences, person, rngh)
        }
        gain
    }

    def calculateMaximalHappinessGain(preferences: List[Preference]): Int = {
        val people = getPeopleList(preferences)
        var highestGain = -1
        people.permutations.foreach((lst: List[String]) => {
            val gain = calculateConfigurationGain(preferences, lst)
            if(gain > highestGain) {
                highestGain = gain
            }
        })
        highestGain
    }

    def parseLine(line: String): Preference = {
        val pattern = new Regex("(\\w+) would (gain|lose) (\\d+) happiness units by sitting next to (\\w+).", "from", "changeType", "value", "to")
        val m = pattern.findAllIn(line)
        Preference(m.group("from"), m.group("to"), m.group("value").toInt * (if(m.group("changeType").equals("gain")) 1 else -1))
    }

    def parseInput(): List[Preference] = {
        val inputFile = "input"
        val source = Source.fromFile(inputFile)
        val prefs = new ListBuffer[Preference]
        for(line <- source.getLines()) {
            prefs += parseLine(line)
        }
        source.close()
        prefs.toList
    }

    def getPeopleList(prefs: List[Preference]): List[String] = {
        prefs.map((p: Preference) => p.from).distinct
    }
}
