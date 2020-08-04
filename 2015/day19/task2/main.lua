
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


function calculateMinLength(word)
    w = word
    count = 0
    while w ~= "e" do
        remLen = 0
        found = False
        while remLen < #w and (not found) do
            sw = string.sub(w, 1, #w - remLen)
            rem = string.sub(w, #w - remLen + 1)
            for i = 1,#transformations do
                l, m = string.match(sw, "(.*)(" .. transformations[i][2] .. ")$")
                if l ~= nil then
                    w = l .. transformations[i][1] .. rem
                    found = true
                    count = count + 1
                    break
                end
            end
            remLen = remLen + 1
        end
    end
    return count
end

result = calculateMinLength(source)
print(result)
