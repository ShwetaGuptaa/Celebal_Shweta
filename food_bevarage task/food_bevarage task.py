import pandas as pd
df_1=pd.read_excel('tata salt and tea data.xlsx',0,header=0)
df_2=pd.read_excel('tata salt and tea data.xlsx',1,header=0)

# df_merged=pd.merge(df_1,df_2,how='inner', on=['phone','customerGSTINno'])
# duplicateRowsDF_1 = df_merged[df_merged.duplicated(['phone','customerGSTINno'])]
# print(duplicateRowsDF_1)

# print(df_merged)
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

def checker(food_customer_names,bevarage_customer_names):
    names_array=[]
    ratio_array=[]
    
    for food_customer_name in food_customer_names:
        if food_customer_name in bevarage_customer_names:
            names_array.append(food_customer_name)
            ratio_array.append('100')
        else:   
            x=process.extractOne(food_customer_name,bevarage_customer_names,scorer=fuzz.token_set_ratio)
            names_array.append(x[0])
            ratio_array.append(x[1])
    return names_array,ratio_array
    
    # for food_customer_name,correct_option in zip(food_customer_names,bevarage_customer_names):
        # if food_customer_name == bevarage_customer_name:
           # names_array.append(food_customer_name)
           # ratio_array.append('100')
        # else:   
            # x=fuzz.WRatio(food_customer_name,bevarage_customer_name)
            # # x=process.extractOne(food_customer_name,bevarage_customer_names,scorer=fuzz.token_set_ratio)
            # # names_array.append(x[0])
            # # ratio_array.append(x[1])
            # ratio_array.append(x)
    
    # return ratio_array
   
name_match,ratio_match=checker(df_1['customerName'],df_2['customerName'])
# ratio_match=checker(df_1['customerName'],df_2['customerName'])
# print(len(name_match))

df=pd.DataFrame()
df['food__customer_names_1']=pd.Series(list(df_1['customerName']))
df['bevarge_customer_names_2']=pd.Series(list(df_2['customerName']))
df['correct_names_bevarage']=pd.Series(name_match)
df['correct_ratio']=pd.Series(ratio_match)
# df.to_csv('matched_names_file.csv')
customer_unmatched_food=[]
customer_unmatched_bevarage=[]
customer_matched_food=[]
customer_matched_bevarage=[]
for ind in df.index:
    if df.loc[ind]['correct_ratio']<85:
        customer_unmatched_food.append(df.loc[ind]['food__customer_names_1'])
        customer_unmatched_bevarage.append(df.loc[ind]['correct_names_bevarage'])
    else:
        customer_matched_food.append(df.loc[ind]['food__customer_names_1'])
        customer_matched_bevarage.append(df.loc[ind]['correct_names_bevarage']) 

# print(len(customer_unmatched_food))
# print(len(customer_unmatched_bevarage)) 
# print(len(customer_matched_food))
# print(len(customer_matched_bevarage)) 

## to create dataframe of matched and unmatched customer names

df_food_unmatched=pd.DataFrame()
df_food_unmatched['customerName']=pd.Series(customer_unmatched_food)

df_bevarage_unmatched=pd.DataFrame()
df_bevarage_unmatched['customerName']=pd.Series(customer_unmatched_bevarage)

df_food_matched=pd.DataFrame()
df_food_matched['customerName']=pd.Series(customer_matched_food)

df_bevarage_matched=pd.DataFrame()
df_bevarage_matched['customerName']=pd.Series(customer_matched_bevarage)


# ## To convert dataframe into excel file
df_foodonly_unmatched=pd.merge(df_1,df_food_unmatched,how='inner',on='customerName')
df_foodonly_unmatched.to_csv('unmatched_names_file_food.csv',index=False)

df_bevargeonly_unmatched=pd.merge(df_2,df_bevarage_unmatched,how='inner',on='customerName')
df_bevargeonly_unmatched.to_csv('unmatched_names_file_bevarage.csv',index=False)

df_foodonly_matched=pd.merge(df_1,df_food_matched,how='inner',on='customerName')
df_foodonly_matched.to_csv('matched_names_file_food.csv',index=False)

df_bevargeonly_matched=pd.merge(df_2,df_bevarage_matched,how='inner',on='customerName')
# df_bevargeonly_matched=pd.concat([df_2,df_bevarage_matched],join='inner',axis=1)
df_bevargeonly_matched.to_csv('matched_names_file_bevarage.csv',index=False)


