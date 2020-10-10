# First task (Gate detection using image processing):
1-first convert images to HSV.\
2-apply color detection mask (Two filter masks for near and far gates).\
3-apply noise removal filter(opening transformation).\
4-then apply find contour function which appropriate to our problem to find gate contours.\
\
\
![detection process](https://github.com/fatma-mohamed-98/AUV_gate_detection/blob/main/applying_filters.JPG)

4.1. near gate detection:\
\
![near gate detection](https://github.com/fatma-mohamed-98/AUV_gate_detection/blob/main/image_processing_detection2.JPG)\
4.2. far gate detection:\
\
![far gate detection](https://github.com/fatma-mohamed-98/AUV_gate_detection/blob/main/image_processing_detection.JPG)


# First task (Gate detection using CNN):
1- writting the script to retrieve images from the videos as a first step.\
2-splitting the images to (train-validation-test) files.\
3-applying data augmentation to get better result.\
4-building a CNN model, making a hyper parameter tuning, choosing appropriate loss function and optimizer for our problem.\
5-the model tested by using the testing data which never seen before (test accuracy is 92%).\
**finally look at the model confusion matrix**

![confusion_matrix](https://github.com/fatma-mohamed-98/AUV_gate_detection/blob/main/confusion_matrix.JPG)
