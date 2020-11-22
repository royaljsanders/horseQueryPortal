# takes a table generated by the sql query of ours and combines the measurement types
"""
Created on Wed Sep 16 13:40:03 2020

@author: royal
"""

import pandas as pd
import argparse

    
    
def nonCLI(inputfile, outputfile):
    print(inputfile, outputfile)
    inputDf = pd.read_csv(inputfile)
    #print(inputDf)
    outputDf = pd.DataFrame()
    print("Will attempt to use function parameters as filenames, working...")
    outputDf = goQuery(inputDf, outputDf)
    #print(outputDf)
    outputDf.to_csv(outputfile)
    print("Exported to", outputfile)

def goQuery(inputDf, outputDf):
    for i in range(len(inputDf) - 1):
        #print(inputData.iloc[i].analysisDataId)
        """
        if (inputDf.iloc[i].measurementType == 1 ):
            type1 = inputDf.iloc[i]
            type2 = inputDf.iloc[i+1]
        if (inputDf.iloc[i].measurementType == 2):
            type2 = inputDf.iloc[i]
            type1 = inputDf.iloc[i+1]
        
        type1 = inputDf.iloc[i]
        type2 = inputDf.iloc[i+1]
        """
        #checks to see if there is a pair of values
        #print(inputDf.iloc[i].diffMinMean, inputDf.iloc[i+1].diffMinMean)
        if inputDf.iloc[i].analysisDataId == inputDf.iloc[i+1].analysisDataId:
            # print(inputDf.iloc[i].diffMinMean, inputDf.iloc[i+1].diffMinMean)
            
            if (inputDf.iloc[i].measurementType == 1 ):
                type1 = inputDf.iloc[i]
                type2 = inputDf.iloc[i+1]
                #print("_")
            elif (inputDf.iloc[i].measurementType == 2):
                type2 = inputDf.iloc[i]
                type1 = inputDf.iloc[i+1]
                #print("2")
            # print("Type1, Type1", type1.diffMinMean, type2.diffMinMean)
            if type1.diffMinMean*type2.diffMinMean > 0:
                #print(type1.analysisDataId)
                #print(type1.measurementType) #should only print 1
                #vectorSum = type1.vectorSum
                #print(vectorSum)
                #print("good")
                new_row = {
                    'vectorSum' : type1.vectorSum,
                    'diffMinHead' : type1.diffMinMean,
                    'diffMinPelvis' : type2.diffMinMean,
                    'diffMaxMean' : type2.diffMaxMean,
                    'diffMinStdDev' : type2.diffMinStdDev,
                    'horseId' : type1.horseId,
                    'trialIdGuid' : type1.trialidGuid,
                    'trialPattern' : type1.trialPattern,
                    'trialId' : type1.trialId,
                    'horseIdGuid' : type1.horseIdGuid,
                    'ownerId' : type1.ownerId,
                    'ownerFname' : type1.firstName,
                    'ownerLname' : type1.lastName,
                    'owneridGuid' : type1.owneridGuid,
                    'attendingId' : type1.personId,
                    'attendingFname' : type1.attendingFname,
                    'attendingLname' : type1.attendingLname,
                    'personidGuid' : type1.personidGuid     
                }
                
                #print(new_row)
                
                outputDf = outputDf.append(new_row, ignore_index=True)
    return outputDf
                
def main():
    print("printed from main")
    #create parser
    parser = argparse.ArgumentParser()
    
    #add arguments to the parser
    parser.add_argument("inputfile")
    parser.add_argument("outputfile")
    
    args = parser.parse_args()
    
    inputDf = pd.read_csv(args.inputfile)
    #print(inputDf)
    outputDf = pd.DataFrame()
    
    #ANALYSIS MEASUREMENT: vectorSum (type1), diffMinHead (diffMinMean type1), diffMinPelvis (diffMinMean type2), diffMaxMean (type2), diffMinStdDev (type2),
    #TRIALhorseID, idGuid, trialPattern, id, 
    #HORSE id (horse), name (name), idGuid, 
    #OWNER id, firstName, lastName, idGuid, 
    #PERSON id, lastName, idGuid
    
    print("Will attempt to use arguments as filenames, working...")
    outputDf = goQuery(inputDf, outputDf)
 
    outputDf.to_csv(args.outputfile)
    print("Exported to", args.outputfile)
 
if __name__ == "__main__":
    main()