#first pass
Syta= dict()
Syta={'R0':0,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,'R8':8, 'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15,'SCREEN':16384,'KBD':24576,'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4}
Jbit = dict()
Jbit ={'null':'000','JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}
Dbit = dict()
Dbit ={'null':'000','M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':'111'}
Cbit = dict()
Cbit ={'0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100', 'A':'0110000', '!D':'0001101','!A':'0110001', '-D':'0001111' ,'-A':'0110011', 'D+1':'0011111', 'A+1':'0110111', 'D-1':'0001110', 'A-1':'0110010','D+A':'0000010' ,'D-A':'0010011', 'A-D':'0000111', 'D&A':'0000000', 'D|A':'0010101', 'M':'1110000' , '!M':'1110001' , '-M':'1110011' , 'M+1':'1110111', 'M-1':'1110010', 'D+M':'1000010','D-M':'1010011', 'M-D':'1000111' ,'D&M':'1000000' ,'D|M':'1010101' }

count= 0

asm=list()
inp =input('Enter the file name:')
fh = open(inp)
for line in fh:    
    line=line.rstrip()
    if line is '' or line.startswith('//'):
        continue    
    if line.startswith('('):
        label=line[1:len(line)-1]
        Syta[label]=Syta.get(label,count)
        continue
    count = count +1
    n=line.find('//')
    if n > -1 :
        line1=line[:n].rstrip()
        asm.append(line1)
    else :
        asm.append(line)
#print(asm)
#output file
out= inp[:inp.find('.')]
outf =out +'.hack'
ofh = open(outf,'w')


#second pass
n=16
for line in asm:
    ACstr =str()
    ACint =list()
    line=line.strip()
    if line.startswith('@'):
        try : 
            loc=int(line[1:]) 
        except :
            if line[1:] not in Syta :
                Syta[line[1:]]=n
                n=n+1
            loc=Syta[line[1:]]       
        while loc > 0:
            r=str(loc%2)
            ACint.append(r)
            loc=int(loc/2)
        while len(ACint) < 16:
            ACint.append('0')      
        ACint.reverse()
    else:
        first=line.find('=')     
        second=line.find(';')
        if first >-1 :
            dest=line[:first]
        else :
            dest='null'
        if second >-1 :
            jump=line[second+1:]
        else :
            jump='null'
            second=len(line)
        comp=line[first+1:second]
        ACint.append('111')
        ACint.append(Cbit[comp])
        ACint.append(Dbit[dest])
        ACint.append(Jbit[jump])
    for i in ACint :
        ACstr=ACstr+i
    ofh.write(ACstr)
    ofh.write('\n')  

