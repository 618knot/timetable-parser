import pandas as pd
import glob
import pathlib as Path
import tabula

def toDataFrame():

    file = glob.glob("download/*")
    #downloadフォルダの0番目のpdfをparseします
    dfs = tabula.read_pdf(f"{file[0]}", lattice=True, pages='all')[:2] #必要な部分のみ
    
    for i in range(2):
        dfs[i] = dfs[i].dropna(axis = 1)
        dfs[i] = pd.DataFrame(dfs[i])

    return dfs


if __name__ == "__main__":
    print(toDataFrame())