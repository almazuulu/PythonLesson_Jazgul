import pandas as pd

data_school = {
    "Name": ["Adam", "Peter", "Sam", "Tim"],
    "Age": [14, 12, 15, 20],
    "Avg Marks": [4.5, 4.3, 5, 3]
}

data_school2 = {
    "Name": ["Greg", "David", "Egor", "Andrew"],
    "Age": [10, 22, 18, 15],
    "Avg Marks": [3.5, 3.4, 4, 5]
}

df = pd.DataFrame(data_school)
df2 = pd.DataFrame(data_school2)

with pd.ExcelWriter("LessonFiles/marks3.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Marks 1", index=False)
    df2.to_excel(writer, sheet_name="Marks 2", index=False)

