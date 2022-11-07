import csv
from statsmodels.stats.contingency_tables import mcnemar

combinations = []

for a1a in [True,False]:
    for b2b in [True,False]:
        for c3c in [True,False]:
            if(not a1a and not b2b and not c3c):
                continue
            combinations.append([a1a,b2b,c3c])

csv_data = []

with open("mcnemars.csv",newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for iterations in range(7):
        for row in reader:
            csv_data.append(row)

def evaluate(data,start,end,print_data=True,write_data=True,configuration=None):
    YESNO = 0
    NOYES = 0
    YESYES = 0
    NONO = 0

    try:
        data[start]
        data[end-1]
    except Exception as e:
        print("Invalid start or end index.")
        return

    for i in range(start,end):
        if data[i]["SVM Correct"] == str(False) and data[i]["Guess Correct"] == str(True):
            NOYES+=1
        if data[i]["SVM Correct"] == str(True) and data[i]["Guess Correct"] == str(False):
            YESNO+=1
        if data[i]["SVM Correct"] == str(False) and data[i]["Guess Correct"] == str(False):
            NONO+=1
        if data[i]["SVM Correct"] == str(True) and data[i]["Guess Correct"] == str(True):
            YESYES+=1

    contingency_table = [
        [YESYES,YESNO],
        [NOYES,NONO]
    ]

    #print(contingency_table)

    result = mcnemar(contingency_table, exact=False,correction=True)
    alpha = 0.05
    message = ""
    if result.pvalue > alpha:
        message = 'Same proportions of errors (fail to reject H0)'
    else:
        message = 'Different proportions of errors (reject H0)'
    if print_data:
        print('statistic=%.3f, p-value=%.3f' % (result.statistic, result.pvalue))
        print(message)
    if write_data:
        with open("mcnemarsresults.txt", "a") as file:
            if not configuration == None:
                file.writelines(["\n" + str(configuration),'\nstatistic=%.3f, p-value=%.3f' % (result.statistic, result.pvalue),"\n" + message])
            else:
                file.writelines(['\nstatistic=%.3f, p-value=%.3f' % (result.statistic, result.pvalue),"\n" + message])
for index in range(7):
    start_index = (index*255)
    stop_index = ((index+1)*255)
    evaluate(csv_data,start_index,stop_index,configuration=combinations[index])