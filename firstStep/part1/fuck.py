ist_to_input = ['classA : classB classC classD classG classH', 'classB : classC classE classG classH classK classL', 'classC : classE classD classH classK classL', 'classE : classD classF classK classL', 'classD : classG classH', 'classF : classK', 'classG : classF', 'classH : classL', 'classK : classH classL', 'classL']
list_to_question=['classK classD', 'classD classA', 'classG classD', 'classH classA', 'classE classE', 'classH classG', 'classE classL', 'classB classD', 'classD classL', 'classD classG', 'classD classE', 'classA classF', 'classA classC', 'classK classA', 'classA classH', 'classK classD', 'classH classB', 'classK classB', 'classD classL', 'classG classG', 'classA classH', 'classK classL', 'classG classE', 'classB classA', 'classC classK', 'classK classL', 'classC classL', 'classG classC', 'classD classD', 'classC classG', 'classE classA', 'classF classK', 'classB classG', 'classH classL', 'classL classF', 'classH classG', 'classD classA', 'classH classL']
answers = ['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No']
ma=['Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No']   #мои ответы на список классов list_to_input и список запросов list_to_question
#print(len(list_to_input))   #|            
#for i in list_to_input:     #|
#   print(i)                 #| раскоментить если надо вставить пример в pycharm
#print(len(list_to_question)) #|  
#for i in list_to_question:   #|
#   print(i)                 #|  

#================Получить таблицу сравнения ответов в примере с моим ответами====================
a=[]
cnt=0
for i in range(len(list_to_question)):
    if answers[i]==ma[i]:
        a.append(str(str(i+1)+'\t'+answers[i]+'\t'+ma[i]+'\t'+'1'))
        cnt+=1
    else:
        a.append(str(str(i+1)+'\t'+answers[i]+'\t'+ma[i]+'\t'+'0'))

print('#пп','answers','ma',cnt,sep='\t')
for i in a:
    print(i)