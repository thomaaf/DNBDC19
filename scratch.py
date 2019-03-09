import pandas as pd
import datetime
import matplotlib.pyplot as plt
import random
import matplotlib.dates as mdates

key_date = "quote_date"


def main():
    data = pd.read_csv("data.csv")
    data = data.drop(labels=["paper", "exch", "value", "volume"], axis=1)
    #print(data.head())
    savings = pd.read_csv("savings.csv")

    savings_day=[]
    savings_input=[]
    for i in range (len( savings["Dato"])):
        savings_day.append(savings["Dato"][i])
        savings_input.append(savings["Innskudd"][i])
    print(savings_input)
    print(savings_day)
    date_dt = data[key_date].apply(lambda x: datetime.datetime.strptime(str(x), "%Y%m%d"))
    first_date = date_dt.min()
    #print("First date is: {}".format(first_date))

    date_days = date_dt.apply(lambda x: (x - first_date).days)
    #print(date_days)

    stock_value =  []
    stock_percentage = [0]
    init_invest = [10000]
    init_invest2 = [10000]
    init_invest3 = [10000]

    for i in range(0,len(data["high"])):
        stock_value.append(data["high"][i])
    stock_value.reverse()

    for i in range(0,len(stock_value)-1):
        stock_percentage.append((stock_value[i+1] - stock_value[i])/stock_value[i])
    stock_startday = 3000;
    counter = 0
    dates2 = []
    for i in range(1, len(stock_value) - 1 - stock_startday):
        if i in savings_day:
            init_invest[i-1] = init_invest[i-1] + savings_input[counter]
            init_invest3[i - 1] = init_invest3[i - 1] + savings_input[counter]
            init_invest2[i - 1] = init_invest2[i - 1] + savings_input[counter]
            counter += 1
        init_invest.append(init_invest[i-1] + init_invest[i-1]*stock_percentage[stock_startday +  i]*0.3)
        init_invest3.append(init_invest3[i - 1] + init_invest3[i - 1] * (random.randint(-100, 100)/100 +0.05)/100)
        init_invest2.append(init_invest2[i-1] + init_invest2[i-1]*3/100/365)
        dates2.append(stock_percentage[stock_startday +  i])
        print(i)

    #plt.gca().xaxis.set_major_locator(mdates.DayLocator())
    plt.plot(init_invest, label="DNB Teknologi",linewidth=2)
    plt.plot(init_invest3,label="High risk Stock",linewidth=2)
    plt.plot(init_invest2, label="BSU account",linewidth=2)


    plt.grid()
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()