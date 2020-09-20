-module(aoc)

main([]) ->
    RawInput = readInput(),
    Reindeers = parseInput(RawInput),
    ReindeerCount = length(Reindeers),
    Time = 2503,
    Points = calculateResultAfter(Reindeers, Time),
    Result = lists:max(Points),
    io:format("~p", [Result]).
    
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
    
distances(Reindeers, Time) ->
    lists:map(fun(X) -> distance(X, Time) end, Reindeers).
    
distance(Reindeer, Time) ->
    Speed = lists:nth(1, Reindeer),
    Ftime = lists:nth(2, Reindeer),
    Rtime = lists:nth(3, Reindeer),
    FullCycles = Time div (Ftime + Rtime),
    FullCyclesTime = FullCycles * (Ftime + Rtime), 
    TimeLeft = Time - FullCyclesTime,
    Dist = FullCycles * Ftime * Speed,
    Dist + min(TimeLeft, Ftime) * Speed.

calculateResultAfter(Reindeers, 0) -> zeros(length(Reindeers));
calculateResultAfter(Reindeers, Time) ->
    Cnt = length(Reindeers),
    Dist = distances(Reindeers, Time),
    MaxDist = lists:max(Dist),
    Points = lists:map(fun(X) -> bool2int(lists:nth(X, Dist) == MaxDist) end, lists:seq(1, Cnt)),
    list_add(Points, calculateResultAfter(Reindeers, Time - 1)).

bool2int(Bool) ->
    case Bool of
        true -> 1;
        false -> 0
    end.
    
zeros(0) -> [];
zeros(N) when N > 0 -> [0 | zeros(N - 1)]. 

list_add(L1, L2) ->
    lists:zipwith(fun(X, Y) -> X + Y end, L1, L2).
