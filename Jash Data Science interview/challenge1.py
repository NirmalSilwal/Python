

"""
implement function 'subtract_months' to subtract 'n' number of months from a given year and month.

Inputs: Is a list of tuples [(year1, month1, months_to_subtract1), (year2, month2, months_to_subtract2), ...] 
where, year is a 4 digit integer
month is an interger value between 1 to 12, 1=January, 2=February, ... 12=December) and 
months_to_subtract is an integer

Output: Is a list of tuples [(result_year1, result_month1), (result_year2, result_month2), ...] 
year (4 digit integer) month (interger value between 1 to 12, 1=January, 2=February, ... 12=December)

For example: subtract 3 months from May 2020. This should result in an output Feb 2020
In this example inputs: year=2020 month=5
output: year=2020 month=2

Code evaluation criteria:
1. Correctness for all possible cases
2. Code should be clean and readable
3. optimal with respect to time and space complexity (e.g. avoid unnecessary extra variables and loops) 

"""

def subtract_months(input_list):
    output_list = []
    
    #TODO: implement your code here
    
    for input_data in input_list:
    
        assert len(input_data) == 3

        year = input_data[0]
        month = input_data[1]
        months_to_subtract = input_data[2]

        if months_to_subtract > 12:
            left_month = months_to_subtract - month

            if left_month >= 12:

                minus_year = left_month // 12
                output_year = year - minus_year - 1
                months_to_be_subtracted = left_month - (12 * minus_year)    
                output_list.append((output_year, 12 - months_to_be_subtracted))

            else:
                output_list.append((year-1, 12 - left_month))

        else:
            if months_to_subtract < month:
                output_month = month - months_to_subtract
                output_list.append((year, output_month))

            else:
                output_year = year - 1
                output_month = 12 - (months_to_subtract - month)
                output_list.append((output_year, output_month))
                
    return output_list



# subtract_months([(2020, 5, 3), (2020, 6, 7), (2020, 5, 30), (2020, 5, 15), (2020, 5, 8)])
