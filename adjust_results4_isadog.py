#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Tripti Bhardwaj
# DATE CREATED: 05/11/2023                              
# REVISED DATE: 08/11/2023
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 

def adjust_results4_isadog(results_dict, dog_file_path):
    """
    Checks and adjusts the results dictionary to identify correct classifications
    of images as dogs or not dogs. Demonstrates the model's ability to classify
    dog images correctly even if the breed is wrong.
    
    Parameters:
      results_dict - Dictionary with 'key' as image filename and 'value' as a 
                     List with the following items: 
                     index 0 = pet image label (string)
                     index 1 = classifier label (string)
                     index 2 = 1/0 (int)  where 1 = match between pet image
                               and classifier labels and 0 = no match between labels
                 ------ where index 3 & index 4 are added by this function -----
                      NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                                  0 = pet Image 'is-NOT-a' dog. 
                      NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                                  'as-a' dog and 0 = Classifier classifies image  
                                  'as-NOT-a' dog.
     dog_file_path - A text file that contains names of all dogs from the classifier
                     function and dog names from the pet image files. This file has 
                     one dog name per line; dog names are all in lowercase with 
                     spaces separating the distinct words of the dog name. Dog names
                     from the classifier function can be a string of dog names separated
                     by commas when a particular breed of dog has multiple dog names 
                     associated with that breed (e.g., maltese dog, maltese terrier, 
                     maltese) (string - indicates text file's filename)
    Returns:
           None - results_dict is mutable data type, so no return needed.
    """           
    with open(dog_file_path, 'r') as file:
        dog_names = file.readlines()
    
    # Convert dog names to lowercase and remove leading/trailing whitespaces
    dog_names = [name.strip().lower() for name in dog_names]

    # Iterate through the results_dict and update index 3 and index 4
    for key in results_dict:
        # Check if pet image label is a dog
        results_dict[key].append(1 if results_dict[key][0] in dog_names else 0)

        # Check if classifier label is a dog
        results_dict[key].append(1 if results_dict[key][1] in dog_names else 0)