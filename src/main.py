from myConvexHull import plotting
import pandas as pd
from sklearn import datasets
import os

def chooseCSV():
    print("Current Dataset:")
    dir = os.getcwd()
    dir += f"\\dataset"
    list_dataset = os.listdir(dir)
    for i in range(len(list_dataset)):
        print(f"{i+1}. {list_dataset[i]}")
    a = int(input("Masukkan data csv yang ingin dipilih (dalam angka): "))
    if a <= 0 or a > len(list_dataset):
        print("\ndata yang dipilih tidak ditemukan.\n")
        return chooseCSV()
    return f"dataset\\{list_dataset[a-1]}"

print("CONVEX HULL VISUALIZER")
print("1. iris")
print("2. wine")
print("3. breast-cancer")
print("4. manual csv")
a = int(input("Masukkan dataset yang akan dipilih: "))
while (a < 1 or a > 4):
    print("\nMasukkan salah, silahkan ulangi!\n")
    a = int(input("Masukkan dataset yang akan dipilih: "))
if a == 1:
    data = datasets.load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    target_name = data.target_names
    check = True
elif a == 2:
    data = datasets.load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    target_name = data.target_names
    check = True
elif a == 3:
    data = datasets.load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)
    target_name = data.target_names
    check = True
elif a == 4:
    df = chooseCSV()
    df = pd.read_csv(df)
    choose = input("Apakah dataset memiliki target? (Y/N): ")
    while (str.lower(choose) != 'y' and str.lower(choose) != 'n'):
        choose = input("Apakah dataset memiliki target? (Y/N): ")
    if (str.lower(choose) == 'y'):
        check = True
        target_name = df.target.unique()
    else:
        target_name = []
        check = False
df.head()
print(df)
print("list column: ")
for i in range (len(df.columns)):
    print(f"{i+1}. {df.columns[i]}")

x_point = int(input("attribute as x (dalam angka): "))
y_point = int(input("attribute as y (dalam angka): "))
while (x_point <= 0 or x_point > len(df.columns)):
    x_point = int(input("attribute as x (dalam angka): "))
while (y_point <= 0 or y_point > len(df.columns)):
    y_point = int(input("attribute as y (dalam angka): "))
x_point = df.columns[x_point-1]
y_point = df.columns[y_point-1]

if(check):
    target = int(input("attribute as target (dalam angka):"))
    while (target <= 0 or target > len(df.columns)):
        target = int(input("attribute as target (dalam angka):"))
    target = df.columns[target-1]
else:
    target = "NONE"
try:
    plotting(df,target_name,x_point,y_point,target)
except:
    print("Data tidak bisa diplot.")