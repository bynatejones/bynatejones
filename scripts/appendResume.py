import sys
import json
import time

def write_json(data, filename="C:/Nate/Work Projects/Film TV Commercial/Website/bynatejones.com/Development/bynatejones/src/data/resume.json"):
    with open (filename, "w") as f:
        json.dump(data, f, indent=4)

while True:
    print("================\n")
    date = input("Date (YYMM): ")
    title = input("Production: ")
    type = input("Category: ")
    role = input("Role: ")
    camera = input("Camera(s): ")

    with open ("C:/Nate/Work Projects/Film TV Commercial/Website/bynatejones.com/Development/bynatejones/src/data/resume.json") as json_file:
        data = json.load(json_file)
        y = {"date": date, "title": title, "type": type, "role": role, "camera": camera}
        data.append(y)

    write_json(data)
    print("==== Success! ====")

    while True:
        time.sleep(0.5)
        restart = input("Add another? (y/n): ").lower()

        if restart in ("y", "n"):
            break
    if restart == 'y':
        print("\n================\nRunning again...")
        continue
    else:
        print("==== Goodbye! ====")
        time.sleep(1.5)
        break
