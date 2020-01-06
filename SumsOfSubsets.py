def SumsOfSubsets(arr):
  #This is our array to keep track of all Sums 
  Allsums = []

  #We loop over all numbers that we need to consider for the final list of Sums
  for number in arr:
    #Make a duplicate of the list so we dont get stuck in an endless loop
    Placeholder = Allsums[:]
    #Adding each new number to the final list
    Allsums.append(number) 
    #Looping over all our existing sums to add all new sums that include the new number
    for sum in Placeholder:
      Allsums.append(sum + number)
  #Adding the final case of not selecting any numbers (Can be removed if needed) 
  Allsums.append(0)
  #Sorting the list for neatness (Can be removed/edited as needed)
  Allsums.sort(reverse = True)
  #Returning the final list
  return(Allsums)

#Code written by Karan Shishoo
