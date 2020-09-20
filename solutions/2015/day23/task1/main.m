
rawFile = fileread("input");
lines = strsplit(rawFile, "\n");
a = 0;
b = 0;
i = 1;
while i > 0 && i <= length(lines)
    line = lines{1, i};
    while substr(line, -1, 1) == "\n" || substr(line, -1, 1) == " " || substr(line, -1, 1) == "\r"
        line = substr(line, 1, length(line) - 1);
    endwhile
    llen = length(line);
    splitLine = strsplit(line, " ");
    instr = splitLine{1, 1};
    if instr == "hlf"
        reg = splitLine{1, 2};
        if reg == "a"
            a = a / 2;
        endif
        if reg == "b"
            b = b / 2;
        endif
        i = i + 1;
    endif
    if instr == "tpl"
        reg = splitLine{1, 2};
        if reg == "a"
            a = 3 * a;
        endif
        if reg == "b"
            b = 3 * b;
        endif
        i = i + 1;
    endif
    if instr == "inc"
        reg = splitLine{1, 2};
        if reg == "a"
            a = a + 1;
        endif
        if reg == "b"
            b = b + 1;
        endif
        i = i + 1;
    endif
    if instr == "jmp"
        ofs = splitLine{1, 2};
        sign = substr(ofs, 1, 1);
        num = erase(substr(ofs, 2), " ");
        numlen = length(num);
        offset = base2dec(num, 10);
        if sign == "-"
            offset = -1 * offset;
        endif
        i = i + offset;
    endif
    if instr == "jie"
        reg = substr(splitLine{1, 2}, 1, 1);
        ofs = splitLine{1, 3};
        sign = substr(ofs, 1, 1);
        num = erase(substr(ofs, 2), " ");
        offset = base2dec(num, 10);
        if sign == "-"
            offset = -1 * offset;
        endif
        rv = a;
        if reg == "b"
            rv = b;
        endif
        if mod(rv, 2) == 0
            i = i + offset;
        else
            i = i + 1;
        endif
    endif
    if instr == "jio"
        reg = substr(splitLine{1, 2}, 1, 1);
        ofs = splitLine{1, 3};
        sign = substr(ofs, 1, 1);
        num = erase(substr(ofs, 2), " ");
        offset = base2dec(num, 10);
        if sign == "-"
            offset = -1 * offset;
        endif
        rv = a;
        if reg == "b"
            rv = b;
        endif
        if rv == 1
            i = i + offset;
        else
            i = i + 1;
        endif
    endif
endwhile

printf("%d", b)
 