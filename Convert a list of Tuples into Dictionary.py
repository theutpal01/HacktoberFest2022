# Python code to convert into dictionary
list_1=[("Nakul",93), ("Shivansh",45), ("Samved",65),
           ("Yash",88), ("Vidit",70), ("Pradeep",52)]
dict_1=dict()
  
for student,score in list_1:
    dict_1.setdefault(student, []).append(score)
print(dict_1)
