
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

molecules = {}
for k, t in pairs(transformations) do
    l = source
    totalR = ""
    while true do
        l, m, r = string.match(l, "(.*)(" .. t[1] .. ")(.*)")
        if m == nil then
            break
        end
        
        key = l .. t[2] .. r .. totalR
        totalR = m .. r .. totalR
        molecules[key] = true
    end
end

uniqueMolecules = {}
for k, t in pairs(molecules) do
    uniqueMolecules[#uniqueMolecules + 1] = k
end
result = #uniqueMolecules
print(result)
