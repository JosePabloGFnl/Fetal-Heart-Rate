# Fetal-Heart-Rate

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
