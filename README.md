# Deep Learning to Detect Software Defects

![kmeans](/src/imgs/kmeans.png)

# Abstract
Modern bug detection algorithms rely on hand written rules to ensure source code follows a certain format. As software engineering progresses and source code becomes more complicated the number of different bugs and their complexity increases.  Building algorithms by hand to detect more subtle bugs is almost impossible. To build a more robust bug detector this project takes a natural language processing approach to solving this problem. This project uses information normal bug detectors usually dont consider, like variable names. Even though developers are free to create their own variable names it is good programming practice to use names that are meaningful. The idea is with enough data we can create embeddings for variable names that will do a decent job at describing how those variables are usually used. Using deep learning we create word embeddings on source code and use a recurrent neural network to distinguish between buggy and non-buggy code. To frame bug detection as a machine learning task large amounts of source code, both buggy and non-buggy are required. Our program can download a list of GitHub repositories, extract the source code and we use simple code transformations that take clean code and alter it in some way to make it buggy. This allows us to collect an arbitrarily large amount of labeled buggy and non-buggy code. This program is far from being a commercial product but as a proof of concept we achieved an accuracy of 85% predicting swapped parameters in previously unseen code.

# How to use
NOTE: This project is designed to work best on Linux.

### Step 1
Edit src/download_data.sh and enter a list of GitHub repositories. Then run this script and a json file will be created and stored in the src/jsons/ folder. Note that all repos you enter should be java projects as this program will only extract code from .java files. You can experiment with other languages if you modify the line 98 in src/repo_to_json, but keep in mind the project is optimized to work with java syntax, however it should work with languages with similar syntax such as c#, c++, javascript, etc.

### Step 2
Run src/json_to_vector.py - this script will load the json created in the previous step, tokenize the syntax, and feed the source code to SciKit's Word2Vec. A pickle file will be created and stored in src/py2vec/, this file will contain a dictionary with all the word embeddings I intened to recreate this file using PyTorch to take advantage of a GPU.

### Step 3 (optional)
Run src/vector_explorer.py - this script loads the embeddings and feeds them to a custom kmeans clustering algorithm we wrote and will display the clustered embedding in MatPlotLib. (picture above)

### Step 4
Run src/bug_generator.py - this file will look through the corpus of source code and look for specific logic patterns and alter them in a structured way, to goal is to take clean code and transform it into buggy code. This will give us an arbitrarily large amount of buggy and clean code. This creates 2 pickle files, and stores them in src/py2vec/ - These 2 files will contain arrays containing buggy and non-buggy code examples.

### Step 5
Run src/RNN_model/.ipynb - This notebook loads the embeddings and buggy and non-buggy examples, creates an embedding matrix, builds an LSTM-RNN using Keras with a TensorFlow backend and trains it on the code examples.

# Results and Final Thoughts
I believe this project takes a very interesting approach to bug detection. I was not able to find many research projects taking this kind of approach. I took a lot of my ideas for this project from modern Natural Language Processing. While this project was pretty small scale I think the result we got were very promising and prove that this concept will work and I am confident it could scale up very well. We tested this project on only about 2 million lines of code, which in Deep Learning isn't really that much data, to get better embeddings its not uncommon to see corpuses upwards of 1 billion lines when creating word embeddings, this would be the number I would strive for in this project. 

# Ideas for Improvements
This project was completed in 1 semester in a Software Engineering class, so this project is not perfect and theres a lot that could be improved. Which I would like to impove given enough free time.

* Create a webcrawler to automatically download a massive dataset of source code.

* Use an imprementation of Word2Vec in PyTorch or TensorFlow because in this project we are currently using SciKit-Learn which does not utilize GPUs and will not be practical with larger datasets.

* Use a database instead of storing data to files like we are now as it will quickly get out of hand.

* Modify src/bug_generator.py to create more types of bugs.

* General code clean up and add more aurguments when running scripts as some options that should be customizable are still hard-coded.

# Sponsors
This project was sponsored by Jean Kirschner and Jason Snouffer at ASRC Federal.

# Acknowledgments
[Deep Learning to Find Bugs](http://mp.binaervarianz.de/DeepBugs_TR_Nov2017.pdf)

[Natural Language Processing tutorial with TensoFlow](https://github.com/Hvass-Labs/TensorFlow-Tutorials/blob/master/20_Natural_Language_Processing.ipynb)

[Lab41/hermes supplied some code for downloading source code (most of which we heavily modified)](https://github.com/Lab41/hermes/tree/master/src/utils/code_etl)

#















