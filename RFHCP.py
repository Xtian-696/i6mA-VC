gene_type='DNA'
fill_NA='0'


if gene_type=="RNA":
    gene_value="U"
elif gene_type=="DNA":
    gene_value="T"


def convert_with(dataPath,outputPath):
    lines=open(dataPath).readlines()
    finally_text = open(outputPath, 'w')
    finnaly_lines=""
    for line in lines:
        if line.strip()=="":continue
        if line.strip()[0] in ['A','G','C',gene_value,'N']:
            position_mark=0
            count_AGCT=[0,0,0,0,0]
            temp = ""
            for x in list(line.strip()):
                position_mark+=1
                if x=="A" or x=="G":temp+="1,"
                else:temp+="0,"
                if x=="A" or x==gene_value:temp+="1,"
                else:temp+="0,"
                if x == "A" or x == "C":temp+="1,"
                else:temp+="0,"
                if x == "A":
                    count_AGCT[0] += 1
                    temp +=str(round(count_AGCT[0] / position_mark*1.0,2))
                    temp+=','
                elif x == "G":
                    count_AGCT[1] += 1
                    temp +=str(round(count_AGCT[1] / position_mark*1.0,2))
                    temp += ','
                elif x == "C":
                    count_AGCT[2] += 1
                    temp +=str(round(count_AGCT[2] / position_mark*1.0,2))
                    temp += ','
                elif x == gene_value:
                    count_AGCT[3] += 1
                    temp +=str(round(count_AGCT[3] / position_mark*1.0,2))
                    temp += ','
                elif x == "N":
                    count_AGCT[4] += 1
                    temp +=str(round(count_AGCT[4] / position_mark*1.0,2))
                    temp += ','

            finnaly_lines+=((temp[:len(temp)-1])+'\n')
    finally_text.writelines(finnaly_lines)
    finally_text.close()

def convert_without(dataPath,outputPath):
    lines=open('dataset.txt').readlines()
    finally_text = open('RFHCP2.txt', 'w')
    finnaly_lines=""
    for line in lines:
        if line.strip()=="":continue
        if line.strip()[0] in ['A','G','C',gene_value]:
            position_mark=0
            count_AGCT=[0,0,0,0]
            temp = ""
            for x in list(line.strip()):
                position_mark+=1
                if x=="A" or x=="G":temp+="1,"
                else:temp+="0,"
                if x=="A" or x==gene_value:temp+="1,"
                else:temp+="0,"
                if x == "A" or x == "C":temp+="1,"
                else:temp+="0,"
                if x == "A":
                    count_AGCT[0] += 1
                    temp +=str(round(count_AGCT[0] / position_mark*1.0,2))
                    temp+=','
                elif x == "G":
                    count_AGCT[1] += 1
                    temp +=str(round(count_AGCT[1] / position_mark*1.0,2))
                    temp += ','
                elif x == "C":
                    count_AGCT[2] += 1
                    temp +=str(round(count_AGCT[2] / position_mark*1.0,2))
                    temp += ','
                elif x == gene_value:
                    count_AGCT[3] += 1
                    temp +=str(round(count_AGCT[3] / position_mark*1.0,2))
                    temp += ','

            finnaly_lines+=((temp[:len(temp)-1])+'\n')
    finally_text.writelines(finnaly_lines)
    finally_text.close()


if fill_NA=="1":
    convert_with('dataset.txt','RFHCP1.txt')
elif fill_NA=="0":
    convert_without('dataset.txt','RFHCP2.txt')