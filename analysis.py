import markdown
import pandas as pd

df = pd.read_csv('claims.csv')

print(df.head())

markdown_string = '''
# Using the data dictionary, the data was validated and cleaned accordingly.

claim_id: There are 2000 unique claim_id values in the dataset, and none of them are null. This means that each claim in the dataset has a unique identifier. No changes were made to this column.

time_to_close: There are 256 unique time_to_close values in the dataset, and none of them are null. This means that the time between when the food was consumed and when the symptoms appeared is known for each claim in the dataset. No changes were made to this column.

claim_amount: There are 2000 unique claim_amount values in the dataset, and none of them are null. This means that the amount of money paid out for each claim is known. The data must be continuous and hence was transformed to a float type. The median value in claim_amout is 24821.08, however there were no null values.

amount_paid: There are 1963 unique amount_paid values in the dataset, ranging from 1516.72 to 52498.75. 36 of them are null. This means that the amount of money paid out for 36 claims is not known. All missing values were replaced with the overall median value of 20105.70

location: There are 4 unique location values in the dataset, and none of them are null. This means that the location of each claim is known. No change was made in this column.

individuals_on_claim: There are 15 unique individuals_on_claim values in the dataset, and none of them are null. This means that the number of individuals who filed a claim for each claim is known. No change was made in this column.

linked_cases: There are 2 unique linked_cases values in the dataset, TRUE or FALSE. 26 of them are null. This means that the values for 26 linked cases is not known. All missing values were replaced with FALSE.

cause: There are 5 unique cause values in the dataset, and none of them are null. Upon careful inspection it is revealed that two values were not entered correctly. Here are the changes made: ' Meat' was updated to 'meat', and 'VEGETABLES' was updated to 'vegetable'
'''

print(markdown_string)