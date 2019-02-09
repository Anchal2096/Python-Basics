class HakerRank():
    def MaxPrizeSplit(self):
        self.NoOfLotteryTickets = int(input("ENTER THE NUMBER OF LOTTERY TICKETS"))
        print(self.NoOfLotteryTickets)
        self.listOfSumOfDigits = []
        self.listOfFrequency = []
        for i in range(self.NoOfLotteryTickets):
            #print(i)
            self.Number = i+1
            self.SumOfDigits()
        # print(self.listOfSumOfDigits)
        self.maxInTheList = max(self.listOfSumOfDigits)
        self.CountTheFrequencyOfS()
        print("THE PRIZE WILL SPLIT AMONG", self.maxFrequency, " PEOPLE")


    def SumOfDigits(self):
        sum=0
        while(self.Number>0):
            dig=self.Number%10
            sum=sum+dig
            self.Number=self.Number//10
            # print("The total sum of digits is:",sum)
        self.listOfSumOfDigits.append(sum)

    def CountTheFrequencyOfS(self):
         for j in range(self.maxInTheList):
             s = j+1
             count = 0
             for i in self.listOfSumOfDigits:
                if i == s:
                    count+= 1
             #print("s = " , s ,"count = " ,count)
             self.listOfFrequency.append(count)
         # print(self.listOfFrequency)
         self.maxFrequency = max(self.listOfFrequency)


def main():
    HakerRankObj = HakerRank()
    HakerRankObj.MaxPrizeSplit()
    #HakerRankObj.SumOfDigits(10)


if __name__ == '__main__':
    main()
