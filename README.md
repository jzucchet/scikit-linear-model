# Linear models

Data parsing, scattering and training with basic ML linear algorithms. Adaptations and extensions to 
Aurélien Geron exercises from [Hands-On Machine Learning with Scikit-Learn and Tensor Flow](https://www.amazon.com/Hands-Machine-Learning-Scikit-Learn-TensorFlow/dp/1491962291) 

# Exercise

Take two data sets which provides you with the Satisfaction Index and GDP per capita per Country and try to predict some 
value based on a training model using Linear Regression and KNeighbors. Try to reason on the relevance of these techniques 
for the exercise and make your comments and answer these questions:

    1. What is the Cyprus' Life Satisfaction?
    2. What is the form of the linear function which describes better the Life Satisfaction in function of GDP per Capita?
    3. In what way KNeighbors could improve your estimates with Cyprus' GDP per Capita? What is the Cyprus' Life Satisfaction?
   

## Getting Started

Project available thru Jupyter notebook or by simply running the python script

### Data sets

* Better Life Index data at [oecd.org](https://stats.oecd.org/index.aspx?DataSetCode=BLI)
* International Monetary Fund data [imf.org](http://goo.gl/j1MSKe) 

### Built With

* [scikit-learn](http://scikit-learn.org/stable/) - The ML library
* [matpotLib](https://matplotlib.org/) - The plotting library
* [numpy](https://www.numpy.org/) - The package for scientific computing
* [Jupyter](https://jupyter.org/) - The open-source web application for the notebook

### Installing

Install third-party libraries

```
pip install -r requirements.txt
```

### Running

Simply run the script by executing:

```
./main.py
```

### Acknowledgments

* Aurélien Geron - Handsome Machine Learning [GitHub](https://github.com/ageron/handson-ml)

