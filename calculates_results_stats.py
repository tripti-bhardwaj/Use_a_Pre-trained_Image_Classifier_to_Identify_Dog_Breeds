#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Tripti Bhardwaj
# DATE CREATED: 08/11/2023                        
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_data):
    """
    Calculates statistics based on the results of a program run using a classifier's
    model architecture to classify pet images. The calculated statistics are stored
    in a dictionary (results_stats_dict) for easy retrieval and printing, aiding the
    user in determining the 'best' model for image classification. Note that the
    statistics can be either percentages or counts.

    Parameters:
      results_data - Dictionary with keys as image filenames and values as lists 
                     with the following items: 
                     index 0 = pet image label (string)
                     index 1 = classifier label (string)
                     index 2 = 1/0 (int) where 1 = match between pet image and 
                               classifier labels and 0 = no match between labels
                     index 3 = 1/0 (int) where 1 = pet image 'is-a' dog and 
                               0 = pet Image 'is-NOT-a' dog. 
                     index 4 = 1/0 (int) where 1 = Classifier classifies image 
                               'as-a' dog and 0 = Classifier classifies image  
                               'as-NOT-a' dog.
    Returns:
      results_stats_dict - Dictionary containing the results statistics (either
                           a percentage or a count), where the key is the statistic's 
                           name (starting with 'pct' for percentage or 'n' for count)
                           and the value is the statistic's value. Refer to comments
                           above and the previous topic on Calculating Results for details
                           on how to calculate the counts and statistics.
    """        
    results_stats_dict = {
        'num_dogs_images': 0,
        'num_matching_labels': 0,
        'num_correct_dogs': 0,
        'num_correct_not_dogs': 0,
        'num_correct_breed': 0,
        'num_images': len(results_data),
        'num_not_dogs_images': 0,
        'pct_matching_labels': 0.0,
        'pct_correct_dogs': 0.0,
        'pct_correct_breed': 0.0,
        'pct_correct_not_dogs': 0.0
    }
    
    for key in results_data:
        pet_image_label = results_data[key][0]
        classifier_label = results_data[key][1]
        labels_match = results_data[key][2]
        pet_image_is_dog = results_data[key][3]
        classifier_classifies_as_dog = results_data[key][4]
        
        if labels_match == 1:
            results_stats_dict['num_matching_labels'] += 1
            
        if pet_image_is_dog == 1 and labels_match == 1:
            results_stats_dict['num_correct_breed'] += 1
        
        if pet_image_is_dog == 1:
            results_stats_dict['num_dogs_images'] += 1
            if classifier_classifies_as_dog == 1:
                results_stats_dict['num_correct_dogs'] += 1
        
        if pet_image_is_dog == 0 and classifier_classifies_as_dog == 0:
            results_stats_dict['num_correct_not_dogs'] += 1
        
    results_stats_dict['num_not_dogs_images'] = results_stats_dict['num_images'] - results_stats_dict['num_dogs_images']
    
    if results_stats_dict['num_images'] > 0:
        results_stats_dict['pct_matching_labels'] = (results_stats_dict['num_matching_labels'] / results_stats_dict['num_images']) * 100
        
    if results_stats_dict['num_dogs_images'] > 0:
        results_stats_dict['pct_correct_dogs'] = (results_stats_dict['num_correct_dogs'] / results_stats_dict['num_dogs_images']) * 100
        results_stats_dict['pct_correct_breed'] = (results_stats_dict['num_correct_breed'] / results_stats_dict['num_dogs_images']) * 100
        
    if results_stats_dict['num_not_dogs_images'] > 0:
        results_stats_dict['pct_correct_not_dogs'] = (results_stats_dict['num_correct_not_dogs'] / results_stats_dict['num_not_dogs_images']) * 100.0

    return results_stats_dict