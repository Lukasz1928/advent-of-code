
function readInput()
    lines = {}
    for line in io.lines('input') do
        lines[#lines + 1] = line
    end
    return lines
end

function unique(s)
    u = {}
    for k, v in pairs(s) do
        u[#u + 1] = k
    end
    return u
end

function parseRight(right)
    elems = {}
    while right ~= nil do
        right, s = string.match(right, "(.*)(%u%l?)")
        if s == nil then
            break
        end
        elems[#elems + 1] = s
    end
    revElems = {}
    for i=1,#elems do
        revElems[i] = elems[#elems + 1 - i]
    end
    return revElems
end

rhsPrefix = 1000
startId = 10000
terminalPrefix = 100
startSymbol = "e"
function transformGrammar(symbol2id, id2symbol, grammar) 
    newGrammar = {}
    
    -- add new start symbol
    grammar[#grammar + 1] = {startId, {symbol2id[startSymbol]}}
    id2symbol[#id2symbol + 1] = {startId, startSymbol}
    symbol2id[#symbol2id + 1] = {startSymbol, startId}
    
    -- add terminal symbol for each nonterminal symbol(except for startSymbol)
    for i, s in pairs(id2symbol) do
        if s ~= startSymbol and s[1] ~= startId then
            newGrammar[#newGrammar + 1] = {i, {terminalPrefix + i}}
        end
    end
    
    -- eliminate right handsides with more than two symbols
    rhsIndex = 1
    for i, p in pairs(grammar) do
        l = p[1]
        r = p[2]
        if #r <= 2 then
            newGrammar[#newGrammar + 1] = {l, r}
        else
            newSymbolId = rhsPrefix + rhsIndex
            newGrammar[#newGrammar + 1] = {l, {r[1], newSymbolId}}
            newSymbolId = newSymbolId + 1
            rhsIndex = rhsIndex + 1
            for j, s in pairs(r) do
                if j > 1 and j < #r - 1 then
                    newGrammar[#newGrammar + 1] = {newSymbolId - 1, {s, newSymbolId}}
                    newSymbolId = newSymbolId + 1
                    rhsIndex = rhsIndex + 1
                end
            end
            newGrammar[#newGrammar + 1] = {newSymbolId - 1, {r[#r - 1], r[#r]}}
            rhsIndex = rhsIndex + 1
        end
    end
    
    -- eliminate productions with single nonterminal rhs
    finalGrammar = newGrammar
    tmp = {}
    changed = true
    while changed do
        tmp = finalGrammar
        finalGrammar = {}
        changed = false
        for k, p in pairs(tmp) do
            l = p[1]
            r = p[2]
            if #r == 1 then
                if r[1] >= terminalPrefix and r[1] < rhsPrefix then
                    finalGrammar[#finalGrammar + 1] = {l, r}
                else
                    for k1, p1 in pairs(tmp) do
                        if p1[1] == r[1] and (r[1] < terminalPrefix or r[1] > rhsPrefix) then
                            finalGrammar[#finalGrammar + 1] = {l, p1[2]}
                            changed = true
                        end
                    end
                end
            else
                finalGrammar[#finalGrammar + 1] = {l, r}
            end
        end
        rhsSymbols = {}
        rhsSymbols[startId] = true
        for k, p in pairs(finalGrammar) do
            for i, s in pairs(p[2]) do
                rhsSymbols[s] = true
            end
        end
        rhsSymbols = unique(rhsSymbols)
        tmp = finalGrammar
        finalGrammar = {}
        for k, p in pairs(tmp) do
            l = p[1]
            used = false
            for i, r in pairs(rhsSymbols) do
                if l == r then
                    used = true
                    break
                end
            end
            if used then
                finalGrammar[#finalGrammar + 1] = {l, p[2]}
            end
        end
    end
    print("final grammar")
    for i, s in pairs(finalGrammar) do
        l = s[1]
        r = ""
        for j, k in pairs(s[2]) do
            r = r .. " " .. k
        end
        print(l .. " -> " .. r)
    end
    return finalGrammar
end

function inTable(elem, t)
    
end

function toCNF(tranformations)
    symbols = {}
    for k, t in pairs(tranformations) do
        symbols[t[1]] = true
        rs = parseRight(t[2])
        for k, s in pairs(rs) do
            symbols[s] = true
        end
    end
    intTransformations = {}
    id2symbol = unique(symbols)
    symbol2id = {}
    for k, s in pairs(id2symbol) do
        symbol2id[s] = k
    end
    for k, t in pairs(tranformations) do
        left = symbol2id[t[1]]
        r = parseRight(t[2])
        right = {}
        for i, s in pairs(r) do
            right[#right + 1] = symbol2id[s]
        end
        intTransformations[#intTransformations + 1] = {left, right}
    end
    g = transformGrammar(symbol2id, id2symbol, intTransformations)
    return g, symbol2id
end

function transformWord(symbol2id, word)
    transformed = {}
    w = word
    while w ~= nil do
        w, s = string.match(w, "(.*)(%u%l?)")
        if s == nil then
            break
        end
        transformed[#transformed + 1] = symbol2id[s]
    end
    rev = {}
    for i=1,#transformed do
        rev[i] = transformed[#transformed + 1 - i]
    end
    return rev
end

function calculateSubstitutionNumber(grammar, target)
    t = {}
    for i = 1,(#target) do
        a = {}
        for j = 1,(#target + 1 - i) do
            a[#a + 1] = {}
        end
        t[#t + 1] = a
    end
    return 0
end

rawData = readInput()
transformations = {}
for i = 1,(#rawData-2) do
    l, r = string.match(rawData[i], "(.+) => (.+)")
    transformations[#transformations + 1] = {l, r}
end
source = rawData[#rawData]
print("\n\n")

CNFGrammar, s2id = toCNF(transformations)
s2id[startSymbol] = startId
target = transformWord(s2id, source)

result = calculateSubstitutionNumber(CNFGrammar, target)
print(result)
