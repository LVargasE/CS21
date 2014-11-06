def infileRead():
    # open the original Golfers.txt file
    infile = open("Golfers.txt", "r")

    # read the first record's 'name' field
    name = infile.readline()

    # read rest of file
    while name != '':
        # read the score field
        score = infile.readline()

        # strip the '\n' from 'name' and 'score'
        name = name.rstrip('\n')
        score = score.rstrip('\n')

        # read next name
        name = infile.readline()

    # Close Golfers.txt file
    infile.close()

def outfileWrite():
    # open the temp file
    outfile = open("Temp.txt", "w")

    # read rest of file
    while name != '':
        # read the score field
        score = infile.readline()

        # strip the '\n' from 'name'
        name = name.rstrip('\n')

        # search determins if user input is written to Golfer's file, or temp
        if name == search:
            outfile.write(name + '\n')
            outfile.write(str(newScore) + '\n')

            # set found flag to true
            found = True
        else:
            # write original score to temp file
            outfile.write(name + '\n')
            outfile.write(str(score) + '\n')

        # read next name
        name = infile.readline()

    # Close Golfers.txt file + Temp.txt file
    infile.close()
    outfile.close()
