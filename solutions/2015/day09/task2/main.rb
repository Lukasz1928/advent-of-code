
def readInput()
    return File.readlines("input", chomp: true)
end

def getDistanceArray(rawInput)
    distances = {}
    for l in rawInput
        m = /(\w+) to (\w+) = (\d+)/.match(l)
        loc1 = m[1]
        loc2 = m[2]
        dist = m[3].to_i
        if distances.has_key?(loc1) then
            distances[loc1][loc2] = dist
        else
            distances[loc1] = {loc2 => dist}
        end
        if distances.has_key?(loc2) then
            distances[loc2][loc1] = dist
        else
            distances[loc2] = {loc1 => dist}
        end
    end
    return distances
end

def pathLength(path, distances)
    l = 0
    cl = path[0]
    nl = path[0]
    for i in 1..path.length() - 1
        cl = nl
        nl = path[i]
        l += distances[cl][nl]
    end
    return l
end

def findLongestRouteLength(distances)
    paths = distances.keys.permutation().to_a
    longest = pathLength(paths[0], distances)
    for p in paths
        l = pathLength(p, distances)
        if l > longest then
            longest = l
        end
    end
    return longest
end

rawInput = readInput()
distances = getDistanceArray(rawInput)
longest = findLongestRouteLength(distances)
print(longest)
