# E.ON Energy Programming Task

## Data

Given is randomized data for customers who signed up for an E.ON energy contract in 2018.

The columns in the data are:
* original_product_name: Product the customer signed up to
* postcode: Postcode of the customer (5 digits with 0-9)
* bundesland: The state the customer lives
* total_bonus: The bonus amount we provided (reduces the first-year price)
* order_date: The date that the customer ordered the product

 This data will be used to predict new customer signups, however the data needs to be cleaned before it can be used for prediction.

## Issues identification

Identify and document the issues in the data.

I read in the data using Pandas read_csv() function into a DataFrame object.

* 'postcode' column is stored as an object data type, but it should be an integer since it is a 5-digit number. The warning "DtypeWarning" raised during the data loading also indicates that the column contains mixed types. First values end with '.0', indicating that some values are wrongly formatted as floating point numbers. There are approximately 8,699 different postcodes in Germany, but we have 20,525 different values.
* 'postcode' column contains 1 postcode with non-numeric value: '92696JAVAS'.
* 'postcode' column contains 39095 postcodes with invalid length (not 5 digits).
* 'order_date' column is an object data type, it should be converted to a datetime data type in order to enable using time-based operations, such as resampling and date filtering, and to insure a more efficient storage.
* There are 29532 rows with missing 'bundesland' values. It should be possible to impute the correct states from postcodes (after cleaning that column), but will require mapping data.

## Solution of one or two issues

Choose one or two issues and write code to solve these issues.
For this problem, code quality is more important than quantity, thus the focus on one or two issues. Do them well, instead of solving all the issues!
The code will be reused in other projects by other team members, so think about reusability and maintainability.

I chose to focus on the first 'postcode' column and the 'order_date' column issues.