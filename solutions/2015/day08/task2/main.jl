
function readInput()
    return readlines("input")
end

function calculateCodeLength(strs)
    tl = 0
    for s in strs
        tl += length(s)
    end
    return tl
end

function isEncodable(c)
    return c == '"' || c == '\\'
end

function calculateEncodedStringSize(str)
    s = 0
    i = 1
    while i <= length(str)
        if isEncodable(str[i])
            s += 2
        else
            s += 1
        end
        i += 1
    end
    s += 2
    return s
end

function calculateEncodedStringsSize(strs)
    size = 0
    for s in strs
        size += calculateEncodedStringSize(s)
    end
    return size
end

strs = readInput()
cl = calculateCodeLength(strs)
es = calculateEncodedStringsSize(strs)
result = es - cl
print(result)
