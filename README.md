# HTCSC_MARCO_Companion

This repository is a collection of companion methods to make processing image data from the High Throughput Crystalization Screening Center at Hauptman-Woodward Medical Research Institute easier and more accesible. 

# Setup

First you will need to get the trained model which is available from Vincent Vanhoucke and [downloadable from here](https://storage.googleapis.com/marco-168219-model/savedmodel.zip). You may also be interested in reviewing the publication on the MARCO model, 
[Classification of crystallization outcomes using deep convolutional neural networks](https://arxiv.org/abs/1803.10342).

After you unzip the model add it to a directory of your choice, althouh it is easiest to place it in your cloned repository.

Next you need some images to classify. Download from the HTCSC's FTP server using FileZilla and place in a convenient directory.

Finally, you will need the csv version of the HTCSC latest cocktail recipes. A copy of the latest version is included in this repo at the time of writing but no guarantees it will be down the road. You can find the [downloadable cocktails here](https://hwi.buffalo.edu/crystallization-cocktails/)

# Usage

If the repository has not been added to your Path variables the commad to run the model will look like this

```
python Run_Marco.py --PATH (path to your images) --CSV_PATH (location where all results will be written) 
-- HITS_PATH (location where crystal hits will be written)
```
If you are not using the included cocktail csv you will also need to specify 
```
--COCKTAIL PATH (location of your cocktail csv file)
```

# What you get

1. Classification of all the images in the location specified by the `--PATH` argument
2. Csv file containing the classification, confidences, well number and cocktail recipe for all images
3. Directory containing only the images classified as crystals 
4. Csv file containing same information as 2. but only for the images classified as crystals 

# GUI Version
This repository also contains a GUI version of the companion which can be found on the Gooey branch. 
[You can also download it as a release from here](https://github.com/EthanHolleman/HTCSC_MARCO_Companion/tree/Gooey)

![Screenshot from 2019-08-08 15-07-15](https://user-images.githubusercontent.com/45807040/62734298-473c4d00-b9ee-11e9-84b7-1d9574dc0c38.png)
