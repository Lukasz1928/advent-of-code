
open System
open System.Text.RegularExpressions

let readInput() : List<string> = Seq.toList(System.IO.File.ReadLines("D:/Desktop/advent-of-code/2015/day16/task1/input"))

let rec parseParams(params: string) : Map<string, int> =
    let pattern = Regex("(\w+): (\d+)(.*)")
    let matches = pattern.Match params
    let name = matches.Groups.[1].Value
    let value = matches.Groups.[2].Value |> int
    let remainder = matches.Groups.[3].Value
    if remainder.Equals "" then Map.empty.Add(name, value)
    else Map.add name value (parseParams remainder)

let parseAunt(aunt : string) : Map<string, int> = 
    let patternId = Regex("Sue (\d+): (.*)")
    let idMatch = patternId.Match aunt
    let id = idMatch.Groups.[1].Value |> int
    let params = idMatch.Groups.[2].Value

    let p = parseParams params
    Map.add "id" id p

let parseAunts(rawData : List<string>) : List<Map<string, int>> = List.map parseAunt rawData

let auntsEqual(searched : Map<string, int>, potential: Map<string, int>) : Boolean = 
    let potentialWithoutId = Map.remove "id" potential
    (Map.filter (fun k v -> searched.Item k <> v) potentialWithoutId).Count = 0

[<EntryPoint>]
let main argv =
    let rawData = readInput()
    let aunts = parseAunts rawData
    let searchedAunt = Map.empty
                        .Add("children", 3)
                        .Add("cats", 7)
                        .Add("samoyeds", 2)
                        .Add("pomeranians", 3)
                        .Add("akitas", 0)
                        .Add("vizslas", 0)
                        .Add("goldfish", 5)
                        .Add("trees", 3)
                        .Add("cars", 2)
                        .Add("perfumes", 1);
    let result = (List.filter (fun a -> (auntsEqual(searchedAunt, a))) aunts).Head.Item "id"
    printfn "%A" result
    0
