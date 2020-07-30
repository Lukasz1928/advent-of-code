
function readInput()
    lines = {}
    for line in io.lines('input') do
        lines[#lines + 1] = line
    end
    return lines
end

rawData = readInput()
transformations = {}
for i = 1,(#rawData-2) do
    l, r = string.match(rawData[i], "(.+) => (.+)")
    transformations[#transformations + 1] = {l, r}
end
source = rawData[#rawData]


minLength = math.huge
function calculateMinLength(trans, word, steps)
    print(#word .. " " .. steps)
    if steps >= minLength then
        return
    end
    if word == "e" then
        if steps < minLength then
            minLength = steps
            print("new min length: " .. minLength)
        end
        return
    end
    for k, t in pairs(trans) do
        l = word
        while l ~= nil do
            l, m, r = string.match(l, "(.*)(" .. t[2] .. ")(.*)")
            if m == nil then
                break
            end
            --print(l .. " " .. m .. " " .. r)
            calculateMinLength(trans, l .. t[1] .. r, steps + 1)
        end
    end
end

calculateMinLength(transformations, source, 0)
print(minLength)