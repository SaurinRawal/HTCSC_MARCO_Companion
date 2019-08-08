# MARCO Companion, GUI Version

This branch contains the same functionality as the master but is a GUI implementation using [Gooey](https://github.com/chriskiehl/Gooey)

DISCLAIMER
Gooey itself is working reliably but still in beta. Therefore if something breaks open an issue and checkout the regular command line version. 

# Setup

First you will need to get the trained model which is available from Vincent Vanhoucke and [downloadable from here](https://storage.googleapis.com/marco-168219-model/savedmodel.zip). You may also be interested in reviewing the publication on the MARCO model, 
[Classification of crystallization outcomes using deep convolutional neural networks](https://arxiv.org/abs/1803.10342).

After you unzip the model add it to a directory of your choice, althouh it is easiest to place it in your cloned repository.

Next you need some images to classify. Download from the HTCSC's FTP server using FileZilla and place in a convenient directory.

Finally, you will need the csv version of the HTCSC latest cocktail recipes. A copy of the latest version is included in this repo at the time of writing but no guarantees it will be down the road. You can find the [downloadable cocktails here](https://hwi.buffalo.edu/crystallization-cocktails/)

# Usage

To launch the GUI naviagate to the directory containing the Run_Marco.py file and execute the command
```
python Run_Marco.py
```
You of course could do this from another directory as well. Either way you should be greeted by something like this

![Screenshot from 2019-08-08 15-07-15](https://user-images.githubusercontent.com/45807040/62734298-473c4d00-b9ee-11e9-84b7-1d9574dc0c38.png)

From here you can type in or use the ```Browse``` buttons to specify all of the files in question. The GUI is currently designed to handle one job at a time. So if you want to batch process many screening runs I would suggest using the command line version. 

