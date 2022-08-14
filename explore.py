# Hey, fellow Leavittitians! This is the method I used to put the columns and datatypes of those columns into lists based on if they are a numeric or categorical type. You can use it on the front-end and back-end of your cleaning phase to help you set up for analysis like Maggie Giust did during the explore lesson (though she named her list num_vars and cat_vars in cell 49 of the lesson notebook). [From Peter Chavez]
#def dtypes_to_list(df):
#    num_type_list = []
#    cat_type_list = []
#    for column in df:
#        col_type =  df[column].dtype
#        if col_type == 'object':
#            cat_type_list.append([column, col_type])
#        if col_type in ["int64", "uint8"] and \
#             ((df[column].max() + 1) / df[column].nunique())  == 1:
#            cat_type_list.append([column, col_type])
#        if col_type in ["float64", "int64", "uint8"] and \
#            ((df[column].max() + 1) / df[column].nunique()) != 1:
#            num_type_list.append([column, col_type])
#    return num_type_list, cat_type_list

# https://numpy.org/doc/stable/reference/generated/numpy.issubdtype.html 
# is a nice one to utilize too, since you can use np.number as a bit of 
# a catch-all.
# be mindful of things that may be represented numerically that we may want to interpret as discrete, etc
import numpy as np
import pandas as pd

# Updated with Madeleine's suggestion:
def dtypes_to_list(df):
    num_type_list, cat_type_list = [], []
    for column in df:
        col_type =  df[column].dtype
        if col_type == "object" :
            cat_type_list.append(column)
        if np.issubdtype(df[column], np.number) and \
            ((df[column].max() + 1) / df[column].nunique())  == 1 :
            cat_type_list.append(column)
        if np.issubdtype(df[column], np.number) and \
            ((df[column].max() + 1) / df[column].nunique()) != 1 :
            num_type_list.append(column)
    return num_type_list, cat_type_list