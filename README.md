# Fetal-Heart-Rate

## Previous configurations

In order to run this script, you will need:

- The necessary libraries installed
- Create .env file with the necessary environmental variables
- Obtain input file

### Installing the libraries

The script works with the following versions:
- python `3.11.5`
- pandas `2.1.0`
- numpy `1.25.2`
- matplotlib `3.7.2`
- python-dotenv `1.0.0`
- scikit-learn `1.3.0`
- Jinja2 `3.1.2`
- xlrd `2.0.1`

To install the necessary libraries, run the following code in a Python executer
``` CMD Commands
pip install python-dotenv
```

To view the version of your libraries, run the following:
``` CMD Commands
pip show python-dotenv
```

Another alternate method to view all of the installed libraries if the following:
``` CMD Commands
pip show list
```

An easier and quicker way to install is to run the following to install required packages:

``` CMD Commands
pip install -r requirements.txt
```

### Environmental variables

The `.env` file needs to have the following environmental variables for the script to work properly:

- `CTG`: Dataset with medical information on fetal heart rate experiment results.
- `CTG_sheet`: Sheetname where the main information is required from

Your `.env` file should look like this:

``` textplain
CTG = 'CTG.xls'
CTG_sheet = 'Data'
```

### Input data

The input data that used is from the UC Irvine Machine Learning Repository website, where the dataset is named "Cardiotocography". This daatset contains three tabs, the ones we're interested in are "Description" and "Data", where description focuses on explaining each of the columns used on Data where as the latter has all of the experiments' information that wee need. Here is the link to obtain it:

- `CTG`: Campos,D. and Bernardes,J.. (2010). Cardiotocography. UCI Machine Learning Repository. https://doi.org/10.24432/C51S4N.
- For more information, consult the written paper on this dataset: Diogo Ayres-de-campos, João Bernardes, Antonio Garrido, Joaquim Marques-de-sá & Luis Pereira-leite (2000) SisPorto 2.0: A Program for Automated Analysis of Cardiotocograms, Journal of Maternal-Fetal Medicine, 9:5, 311-318, DOI: 10.3109/14767050009053454

## EDA done
The next variables from CTG.xls were selected for the DataFrame 'data' with the next name changes:
- LB : bl_FHR
- AC.1 : accel
- FM.1 : fetal_mov, 
- UC.1 : uterine_contr 
- DL.1 : light_decel  
- DS.1 : severe_decel 
- DP.1 : prolong_decel 
- ASTV
- MSTV
- ALTV
- MLTV
- Width
- Min
- Max
- Nmax
- Nzeros
- Mode
- Mean
- Median
- Variance
- Tendency
- A : calm_sleep
- B : rem_sleep 
- C : calm_vig
- D : active_vig 
- E (no explanation from source)
- SH : sh_pattern 
- AD : ad_pattern 
- DE : de_pattern 
- LD : ld_pattern 
- FS : fs_pattern 
- SUSP : sus_pattern

Cutted null values, 3 rows cut

Defined outlier ranges for data with clear gaps depicted on the histograms or extremely long tails
Variables from Tendency to sus_pattern are categorical, so they where dropped for the correlation matrix and the EDA to target variable

## FE

Comparing the possibility of dropping or capping outliers resulted on finding that the best option was to drop them. This is because capping our columns
would change the values of the columns affecting the relations it has with other columns that didn't had outliers.

Dataframes with normalized and standarized values were created for comparison on the modeling stage.


## Model

For the model, the algorithm used was Random Forest Classifier due to the problem being of classification.

The three results were made to compare each of the feature engineering techniques to compare and analyze.
