def findWordCount(smyInput, swhichWord):
  res = 0
  a =  smyInput.split(" ")
  print(a)
  b =  swhichWord.lower()
  for i in a:
    if i == b:
      res +=1
  print(res)
  return res


myString = 'It can hardly be a coincidence that no language on Earth has ever produced the expression as pretty as an airport. Airports are ugly. Some are very ugly. Some attain a degree of ugliness that can only be the result of a special effort. This ugliness arises because airports are full of people who are tired, cross, and have just discovered that their luggage has landed in Murmansk (Murmansk airport is the only known exception to this otherwise infallible rule), and architects have on the whole tried to reflect this in their designs. They have sought to highlight the tiredness and crossness motif with brutal shapes and nerve jangling colours, to make effortless the business of separating the traveller for ever from his or her luggage or loved ones, to confuse the traveller with arrows that appear to point at the windows, distant tie racks, or the current position of Ursa Minor in the night sky, and wherever possible to expose the plumbing on the grounds that it is functional, and conceal the location of the departure gates, presumably on the grounds that they are not.'

findWordCount(myString, 'ugly')