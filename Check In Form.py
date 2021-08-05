import csv
from datetime import datetime

def badgePrompt(destination):
    if destination.lower() == 'volunteer':
      badgeAssignment = input('Input Badge #:')
      badgeAssignment = int(badgeAssignment)
      return badgeAssignment
    else:
      return

def appendGuestList(outFile, newRow):
  with open(outFile,'a+',newline='') as outputFile:
    csv_writer = csv.writer(outputFile)
    csv_writer.writerow(newRow)

def main():
  name = input('Name:')
  destination = input('Destination:')
  destination = destination.lower()
  badgeID = badgePrompt(destination)
  
  if len(name) > 1:
    inTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

  newRow =[name,inTime,destination,badgeID]

  appendGuestList('Guest_Check_In.csv', newRow)
  
  #outputWriter = csv.writer(outputFile)
  #outputWriter.writerow([name, inTime, destination, badgeID])
  
  


if __name__ == "__main__":
    main()

