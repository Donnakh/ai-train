#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images_hints.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: This is a *hints* file to help guide students in creating the 
#          function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: EDIT and ADD code BELOW to do the following that's stated in the 
#       comments below that start with "TODO: 3" for the classify_images function 
#       Specifically EDIT and ADD code to define the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    # Process all files in the results_dic - use images_dir to give fullpath
    # that indicates the folder and the filename (key) to be used in the 
    # classifier function
    for key in results_dic:
       
       # TODO: 3a. Set the string variable model_label to be the string that's 
       #           returned from using the classifier function instead of the   
       #           empty string below.
       #
       #  Runs classifier function to classify the images classifier function 
       # inputs: path + filename  and  model, returns model_label 
       # as classifier label
       model_label = ""

       # TODO: 3b. BELOW REPLACE pass with CODE to process the model_label to 
       #           convert all characters within model_label to lowercase 
       #           letters and then remove whitespace characters from the ends
       #           of model_label. Be certain the resulting processed string 
       #           is named model_label.
       #
       # Processes the results so they can be compared with pet image labels
       # set labels to lowercase (lower) and stripping off whitespace(strip)
       pass
              
       # defines truth as pet image label 
       truth = results_dic[key][0]

       # TODO: 3c. REPLACE pass BELOW with CODE that uses the extend list function
       #           to add the classifier label (model_label) and the value of
       #           1 (where the value of 1 indicates a match between pet image 
       #           label and the classifier label) to the results_dic dictionary
       #           for the key indicated by the variable key 
       #
       # If the pet image label is found within the classifier label list of terms 
       # as an exact match to on of the terms in the list - then they are added to 
       # results_dic as an exact match(1) using extend list function
       if truth in model_label:
           pass

       # TODO: 3d. REPLACE pass BELOW with CODE that uses the extend list function
       #           to add the classifier label (model_label) and the value of
       #           0 (where the value of 0 indicates NOT a match between the pet 
       #           image label and the classifier label) to the results_dic 
       #           dictionary for the key indicated by the variable key
       #                   
       # if not found then added to results dictionary as NOT a match(0) using
       # the extend function 
       else:
           ## Defining lists to populate dictionary 
filenames = ["Beagle_01141.jpg", "Beagle_01125.jpg", "skunk_029.jpg" ]
pet_labels = ["beagle", "beagle", "skunk"]
classifier_labels = ["walker hound, walker foxhound", "beagle",
                     "skunk, polecat, wood pussy"]
pet_label_is_dog = [1, 1, 0]
classifier_label_is_dog = [1, 1, 0]

## Defining empty dictionary
results_dic = dict()
    
## Populates empty dictionary with both labels &indicates if they match (idx 2)
for idx in range (0, len(filenames), 1):
    # If first time key is assigned initialize the list with pet & 
    # classifier labels
    if filenames[idx] not in results_dic:
        results_dic[filenames[idx]] = [ pet_labels[idx], classifier_labels[idx] ]
 
    # Determine if pet_labels matches classifier_labels using in operator
    # - so if pet label is 'in' classifier label it's a match
    # ALSO since Key already exists because labels were added, append 
    # value to end of list for idx 2 
    # if pet image label was FOUND then there is a match 
    if pet_labels[idx] in classifier_labels[idx]:
        results_dic[filenames[idx]].append(1)
            
    # if pet image label was NOT found then there is no match
    else:
        results_dic[filenames[idx]].append(0)

## Populates dictionary with whether or not labels indicate a dog image (idx 3&4)
for idx in range (0, len(filenames), 1):
    # Key already exists, extend values to end of list for idx 3 & 4
    results_dic[filenames[idx]].extend([pet_label_is_dog[idx], 
                                       classifier_label_is_dog[idx]])
        
## Iterates through the list to print the results for each filename
for key in results_dic:
    print("\nFilename=", key, "\npet_image Label=", results_dic[key][0],
          "\nClassifier Label=", results_dic[key][1], "\nmatch=",
          results_dic[key][2], "\nImage is dog=", results_dic[key][3],
          "\nClassifier is dog=", results_dic[key][4])                        

    # Provides classifications of the results
    if sum(results_dic[key][2:]) == 3:
        print("*Breed Match*")
    if sum(results_dic[key][3:]) == 2:
        print("*Is-a-Dog Match*")
    if sum(results_dic[key][3:]) == 0 and results_dic[key][2] == 1:
        print("*NOT-a-Dog Match*")
