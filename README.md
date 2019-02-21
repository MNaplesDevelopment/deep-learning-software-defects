# Deep Learning to Detect Software Defects

## Abstract

Modern bug detection algorithms rely on hand written rules to ensure source code follows a certain format. As software engineering progresses and source code becomes more complicated the number of different bugs and their complexity increases.  Building algorithms by hand to detect more subtle bugs is almost impossible. To build a more robust bug detector this project takes a natural language processing approach to solving this problem. This project uses information normal bug detectors usually dont consider, like variable names. Even though developers are free to create their own variable names it is good programming practice to use names that are meaningful. The idea is with enough data we can create embeddings for variable names that will do a decent job at describing how those variables are usually used. Using deep learning we create word embeddings on source code and use a recurrent neural network to distinguish between buggy and non-buggy code. To frame bug detection as a machine learning task large amounts of source code, both buggy and non-buggy are required. Our program can download a list of GitHub repositories, extract the source code and we use simple code transformations that take clean code and alter it in some way to make it buggy. This allows us to collect an arbitrarily large amount of labeled buggy and non-buggy code. This program is far from being a commercial product but as a proof of concept we achieved an accuracy of 85% predicting swapped parameters in previously unseen code.

## How to use

NOTE: This project is designed to work best on Linux.

### Step 1

Edit src/download_data.sh and enter a list of GitHub repositories. Then run this script and a json file will be created and stored in the src/jsons/ folder. Note that all repos you enter should be java projects as this program will only extract code from .java files. You can experiment with other languages if you modify the line 98 in src/repo_to_json, but keep in mind the project is optimized to work with java syntax, however it should work with languages with similar syntax such as c#, c++, javascript, etc.

### Step 2

Run src/json_to_vector.py - this script will load the json created in the previous step, tokenize the syntax, and feed the source code to SciKit's Word2Vec. A pickle file will be created and stored in src/py2vec/, this file will contain a dictionary with all the word embeddings I intened to recreate this file using PyTorch to take advantage of a GPU.

### Step 3 (optional)
Run src/vector_explorer.py - this script loads the embeddings and feeds them to a custom kmeans clustering algorithm we wrote and will display the clustered embedding in MatPlotLib.

### Step 4

Run src/bug_generator.py - this file will look through the corpus of source code and look for specific logic patterns and alter them in a structured way, to goal is to take clean code and transform it into buggy code. This will give us an arbitrarily large amount of buggy and clean code. This creates 2 pickle files, and stores them in src/py2vec/ - These 2 files will contain arrays containing buggy and non-buggy code examples.

### Step 5

Run src/RNN_model/.ipynb - This notebook loads the embeddings and buggy and non-buggy examples, creates an embedding matrix, builds an LSTM-RNN using Keras with a TensorFlow backend and trains it on the code examples.






