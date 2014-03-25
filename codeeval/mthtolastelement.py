
if __name__ == "__main__":
        
        fileName = raw_input()
        
        dataFile = open(fileName, "r")
        #lines = dataFile.readlines()
        
        for line in dataFile:
                dataLine = line.split()
                m = int(dataLine[-1])
                if len(dataLine) - 1 - m >= 0:
                        print dataLine[len(dataLine) - 1 - m]
        dataFile.close()
                              

