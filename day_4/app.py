from day_4.classes import Guards, Guard, Dates, Date
from day_4.inputs import test_data, read_data
from datetime import datetime

def format_data(data):
    guard = {
        "id": 12,
        "dates": [
            {
                "mins": [12, 13, 14],
                "min_asleep": 1
            }
        ]
    }
    guards = Guards()
    dates = Dates()
    last = 0
    for entry in data:
        dt = entry[1:17]
        formatted_time = datetime.strptime(dt, '%Y-%m-%d %H:%M')
        if dates.find(formatted_time):
            print(formatted_time)
        else:
            d = Date(date=formatted_time)
            print(formatted_time)


        print([x.date for x in dates.list])

        if entry.find("Guard ") > -1:
            spl = entry.split(' ')
            id = int(spl[3][1:])
            last = id

            if guards.find(id):
                print("FOUND")
            else:
                g = Guard(id=id)
                guards.add(g)
        else:
            print(last)
    print([x.id for x in guards.list])



def main():
    data = test_data()
    format_data(data)

if __name__ == '__main__':
    main()
