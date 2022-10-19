# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the cha 
def jlist(thing):
  return ''.join(thing)

counter={}

def player(prev_play,opponent_history=[]):
  if prev_play != '':
    opponent_history.append(prev_play)
  guess='P'
  #we need to set a specific depth to make a guess
  depth = 6

  if(len(opponent_history)) > depth:
    finds = jlist(opponent_history[-depth:])

    #we start to track patterns of length "depth" and note how many times we encounter them each time we play
    if jlist(opponent_history[-(depth+1):]) in counter.keys():
      counter[jlist(opponent_history[-(depth+1):])] +=1
    else:
      counter[jlist(opponent_history[-(depth+1):])] = 1

    #then we have to compute all the possible outcomes
    out = [finds+'R',finds+'P',finds+'S']
    #add non-existent paths in counter so that we will be able to get the max
    for i in out:
      if not i in counter.keys():
        counter[i]=0

    #finally we predict what is the next move to counter according
    #to the most played pattern of the opponent 
    predict = max(out, key=lambda key: counter[key])

    if predict[-1] == "P":
          guess = "S"
    if predict[-1] == "R":
          guess = "P"
    if predict[-1] == "S":
          guess = "R"

  return guess

