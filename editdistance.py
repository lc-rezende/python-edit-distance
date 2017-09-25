import editdistance
import numpy as np
import csv

np_email_arr = []
np_distance_arr = []
np_filter = []
np_distance_result = []

def parseFileIntoNPArray(filePath):
    np_email_arr = []
    f = open(filePath, 'r').read()
    f = f.split()
    np_email_arr = np.array(f)
    return np_email_arr

def generateArrayWithDistances(email_arr):
    np_distance_arr = []
    for email in email_arr:
        for line in email_arr:
            result = []
            result.append(email)
            result.append(line)
            result.append(editdistance.eval(email, line))
            np_distance_arr.append(result)
    np_distance_arr = np.array(np_distance_arr)
    return np_distance_arr

def getArrayByDistanceFilter(distance_arr, distance_value = 3):
    np_filter = []
    np_filter = distance_arr[:,2].astype(int) <= distance_value
    np_distance_result = distance_arr[np_filter]
    np_distance_result = np.array(np_distance_result)
    return np_distance_result

def export(np_array):
    # destinationFile = destination + '/EditDistanceResult.csv'
    #np.savetxt('resultado.csv', np_array, delimiter=',')
    print np_array
