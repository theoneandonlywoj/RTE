# Power Consumption Forecast Utilizing Supervised Sequence Machine Learning Algorithms 
## Authors: Lars Nordström, Pawel Herman, Wojciech Orzechowski 
### Abstract:
Power consumption forecast is a vital tool that enables Transmission System Operator (TSO) to optimize performance of the grid and balance energy production and demand. 
It is a crucial step in order to ensure security, stability, and profitability. 

The aim of the project is to predict energy consumption for the next day (D+1) both on the national and regional level (13 districts) during public holidays in France. 

We created an artificial intelligence network based on the state-of-the-art sequence learning algorithms (GRU and LSTM) which is meant to simulate behavior of the energy consumers. 
The data was provided by RTE Transmission System Operator (http://www.rte-france.com/) through a challenge launched on platform DataScience.net (https://www.datascience.net/fr/challenge/32/details). 
#### Software requirements: 
- Python 3.5 
- Pandas 0.20 
- Matplotlib 
- Tensorflow 1.0 +, GPU support with CUDA 8.0 and cuDNN 6.0 
- Keras 
    - numpy 
    - scipy 
    - yaml 
    - HDF5 and h5py 
- Elephas (http://maxpumperla.github.io/elephas/) – library for distributed deep learning with Keras and Spark 
    - liblapack-dev 
    - libblas-dev 
    - gfortran 
    - Spark 
    - PySpark 
- Hyperas (http://maxpumperla.github.io/hyperas/) – hyperparameter optimization library for Keras