
# PROGRAMMER: Mukesh Paul
# DATE CREATED: 05-10-2025                                  
# REVISED DATE: 05-10-2025 
# PURPOSE: Create a function that calculates the results statistics from the 
#          results dictionary. This function computes counts and percentages 
#          of correctly classified dog images, correctly classified non-dog 
#          images, and correctly classified dog breeds. The computed statistics 
#          are stored in a results statistics dictionary, where each statistic’s 
#          name is the key and its value is the corresponding numeric result. 
#          The function helps evaluate the overall performance of the image 
#          classification model used in the project.

def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the run and puts statistics in a 
    results statistics dictionary (results_stats_dic).
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a list.
    
    Returns:
      results_stats_dic - Dictionary that contains the results statistics:
                    counts and percentages
    """
    results_stats_dic = dict()
    
    n_images = len(results_dic)         # Total number of images
    n_dogs_img = 0                      # Number of dog images
    n_notdogs_img = 0                   # Number of non-dog images
    n_correct_dogs = 0                  # Number of correctly classified dog images
    n_correct_notdogs = 0               # Number of correctly classified non-dog images
    n_correct_breed = 0                 # Number of correctly classified dog breeds
    n_label_matches = 0                 # Optional: number of label matches
    
    # Iterate through results_dic to compute counts
    for key in results_dic:
        labels_match = results_dic[key][2]
        pet_label_is_dog = results_dic[key][3]
        classifier_is_dog = results_dic[key][4]
        
        # Count
        if pet_label_is_dog == 1:
            n_dogs_img += 1
            # Correctly classified dog images
            if classifier_is_dog == 1:
                n_correct_dogs += 1
            # Correctly classified dog breeds
            if labels_match == 1:
                n_correct_breed += 1
        else:
            # Non-dog images
            n_notdogs_img += 1
            # Correctly classified non-dog images
            if classifier_is_dog == 0:
                n_correct_notdogs += 1
        
        # Optional: Count label matches
        if labels_match == 1:
            n_label_matches += 1
    
    # Compute percentages
    if n_dogs_img > 0:
        pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100
    else:
        pct_correct_dogs = 0

    if n_notdogs_img > 0:
        pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100
    else:
        pct_correct_notdogs = 0

    if n_dogs_img > 0:
        pct_correct_breed = (n_correct_breed / n_dogs_img) * 100
    else:
        pct_correct_breed = 0

    if n_images > 0:
        pct_label_matches = (n_label_matches / n_images) * 100
    else:
        pct_label_matches = 0

    
    # Store counts in dictionary
    results_stats_dic['n_images'] = n_images
    results_stats_dic['n_dogs_img'] = n_dogs_img
    results_stats_dic['n_notdogs_img'] = n_notdogs_img
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs
    results_stats_dic['n_correct_breed'] = n_correct_breed
    results_stats_dic['n_label_matches'] = n_label_matches
    
    # Store percentages in dictionary
    results_stats_dic['pct_correct_dogs'] = pct_correct_dogs
    results_stats_dic['pct_correct_notdogs'] = pct_correct_notdogs
    results_stats_dic['pct_correct_breed'] = pct_correct_breed
    results_stats_dic['pct_label_matches'] = pct_label_matches
    
    return results_stats_dic
