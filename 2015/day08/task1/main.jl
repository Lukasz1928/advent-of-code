
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

function calculateStringMemorySize(str)
    size = 0
    bare_str = join(collect(str)[2:length(str)-1])
    i = 1
    while i <= length(bare_str)
        if bare_str[i] == '\\'
            if bare_str[i + 1] == '"' || bare_str[i + 1] == '\\'
                i += 2
            else
                i += 4
            end
        else
            i += 1
        end
        size += 1
    end
    return size
end

function calculateTotalMemorySize(strs)
    memSize = 0
    for s in strs
        memSize += calculateStringMemorySize(s)
    end
    return memSize
end

strs = readInput()
cl = calculateCodeLength(strs)
ms = calculateTotalMemorySize(strs)
result = cl - ms
print(result)
