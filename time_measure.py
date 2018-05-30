import datetime import datetime
import pandas as pd
import time
from time import sleep

class Time_Measure:
    def __init__(self, save_path="/Users/yoneda/github/time_measure/"):
        self.save_path = save_path
        now = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        self.save_file_name = "time_measure_result_{}.csv".format(now)

        self.point_dict = {}
        self.resutlt_df = pd.DataFrame({"point_name": [], "start": [], "elapsed": [], "explanation": []})

    def start(self, point_name, explanation=""):
        number = len(self.point_dict)
        self.point_dict[point_name] = number

        add_df = pd.DataFrame({"point_name": [point_name], "start": [time.time()], "elapsed": [-1], "explanation": [explanation]})
        self.resutlt_df = self.resutlt_df.append(add_df, ignore_index=True)

    def end(self, point_name):
        try:
            number = self.point_dict[point_name]
        except:
            print("fail to record elapsed.")

        start = self.resutlt_df.at[number, "start"]
        self.resutlt_df.at[number, "elapsed"] = time.time() - start

    def save(self):
        self.resutlt_df = self.resutlt_df[["point_name", "elapsed", "explanation"]]
        self.resutlt_df.to_csv(self.save_path + self.save_file_name)

def test_function():
    sleep(3)

class Test_Class(Time_Measure):
    def __init__(self):
        Time_Measure.__init__(self)
        sleep(1)

    def test1(self):
        sleep(2)

    def main(self):
        self.start(point_name="test1", explanation="test1_explanation")
        self.test1()
        self.end(point_name="test1")

        self.start(point_name="test2", explanation="test1_explanation")
        self.test1()
        self.end(point_name="test2")

        self.save()

def main1():
    tm = Time_Measure()

    tm.start(point_name="test1", explanation="test1_explanation")
    test_function()
    tm.end(point_name="test1")

    tm.save()

def main2():
    tc = Test_Class()
    tc.main()

if __name__ == "__main__":
    # main1()
    main2()
