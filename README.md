If you need to filter null values, be sure to use the filterTable function to assign the returned dataframe to itself again. This isn't very intuitive since filterTable works with other kinds of functions without returning the dataframe and assigning it to itself, so I made a nullBlocks function that does the same thing. 

What WILL work to keep null blocks: 
df1 = fdb.filterTable(df1, "Blocks", "==", "Null") 
OR 
df1 = fdb.nullBlocks(df1) 

What WON'T work to keep null blocks: 
fdb.filterTable(df1, "Blocks", "==", "Null") 
fdb.nullBlocks(df1) 

Notice how to filter null blocks out, you should assign the return value of the function back to df1. Not intuitive, sorry.  
