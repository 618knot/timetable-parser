from app.toDataFrame import toDataFrame
import datetime

def newJSON():
    dicts = []
    for df in toDataFrame():
        key_list = ["bus stations"]
        contents_list = [list(df.columns)]

        for i in range(len(df)):
            key_list.append(f"bus{i}")
            contents_list.append(df.iloc[i].tolist())

        dicts.append(dict(zip(key_list, contents_list)))
    
    json_dict = {"to cist": dicts[0], "to chitose station": dicts[1], "created at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}
    return json_dict

if __name__ == "__main__":
    print(newJSON())