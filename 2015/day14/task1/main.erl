-module(aoc)

main([]) ->
    RawInput = readInput(),
    Reindeers = parseInput(RawInput),
    Time = 2503,
    Distances = lists:map(fun(X) -> distance(X, Time) end, Reindeers),
    Result = lists:max(Distances),
    io:format("~p\n", [Result]).
    
readInput() ->
    {ok, File} = file:open("input", [read]),
    read(File).
    
read(File) ->
    case file:read_line(File) of
        {ok, Data} -> [Data | read(File)];
        eof        -> []
    end.
    
parseLine(Line) ->
    case re:run(Line, "(\\w+) can fly (?<speed>\\d+) km/s for (?<ftime>\\d+) (\\w+), but then must rest for (?<rtime>\\d+) \\w+\.", [{capture, [speed, ftime, rtime], list}]) of
        {match, Captured} -> lists:map(fun(X) -> list_to_integer(X) end, Captured)
    end.
    
parseInput(Raw) ->
    lists:map(fun(X) -> parseLine(X) end, Raw).
    
distance(Reindeer, Time) ->
    Speed = lists:nth(1, Reindeer),
    Ftime = lists:nth(2, Reindeer),
    Rtime = lists:nth(3, Reindeer),
    FullCycles = Time div (Ftime + Rtime),
    FullCyclesTime = FullCycles * (Ftime + Rtime), 
    TimeLeft = Time - FullCyclesTime,
    Dist = FullCycles * Ftime * Speed,
    Dist + min(TimeLeft, Ftime) * Speed.
