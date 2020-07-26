.286

data segment
    filename db "input", 0
    handler dw ?
    level dw 0
    buffer db 255 dup('$')
    outputBuffer db 6 dup('$')
    charBuffer db ?
data ends

code segment

main:
    mov ax, seg top
    mov ss, ax
    mov sp, offset top
    
    call calculateLevel
    call printResult
    
close:
    mov ah, 04ch
    int 21h

    
calculateLevel:
    pusha
    mov ax, seg data
    mov es, ax
    
    ;open input file
    mov ax, seg filename
    mov ds, ax
    mov dx, offset filename
    mov ah, 03dh
    int 21h
    mov es:[handler], ax
    ;error checking omitted
    
    read:
        mov ax, seg buffer
        mov ds, ax
        mov dx, offset buffer
        mov bx, word ptr es:[handler]
        mov cx, 254
        mov ah, 03fh
        int 21h
    
        cmp ax, 0
        je closeFile 
        
        mov si, 0
        mov bx, offset level
        
        count:
            ;save read character in cx
            xor cx, cx
            mov cl, byte ptr ds:[buffer + si]
            
            cmp cl, '('
            jne goDown
            
            goUp:
                inc word ptr ds:[bx]
                jmp afterChange
            
            goDown:
                dec word ptr ds:[bx]
            
            afterChange:
            
            inc si
            cmp si, ax
            jb count
            
        cmp ax, 254
        je read
    
    closeFile:
        mov bx, word ptr es:[handler]
        mov ah, 03eh
        int 21h
    
    popa
    ret
    
printResult:
    push ax
    push bx
    push cx
    push dx
    
    mov ax, word ptr ds:[level]
    
    mov si, 0
    mov bl, 10
    
    copyDigits:
        div bl
        add ah, '0'
        mov byte ptr ds:[outputBuffer + si], ah
        inc si
        mov ah, 0
        cmp ax, 0
        jne copyDigits
    dec si
    
    printDigit:
        mov ah, byte ptr ds:[outputBuffer + si]
        mov byte ptr ds:[charBuffer], ah
        call printCharBuffer
        dec si
        cmp si, 0
        ja printDigit
        mov ah, byte ptr ds:[outputBuffer]
        mov byte ptr ds:[charBuffer], ah
        call printCharBuffer
    
    pop dx
    pop cx
    pop bx
    pop ax
    ret
    
printCharBuffer:
    pusha
    
    mov al, 0
    mov ah, 02h
    mov dl, byte ptr ds:[charBuffer]
    int 21h
    
    popa
    ret
    
code ends

stacks segment stack
    top dw ?
    db 200 dup (?)
stacks ends
end main
