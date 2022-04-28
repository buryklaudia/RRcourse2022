import pandas as pd

# Read csv file with names of states
states = pd.read_csv(r'states.csv', 
                     usecols = ['State'])

def upper_lower_case(df):
    '''
    Function takes dataframe and returns its values converted to 
    UPPERCASE and lowercase.

    Parameters
    ----------
    df : DataFrame object

    Returns
    -------
    Dataframe object with values converted to UPPERCASE and lowercase.

    '''
    # Create copy to not overwrite the original DataFrame
    df_output = df.copy()
    
    # Convert values to upper and lowercase
    df_output = df_output.applymap(lambda s: '%s/%s' % (s.upper(), s.lower()) if type(s) == str else s)
    
    return(df_output)

result = upper_lower_case(states)

# Save results to csv file
result.to_csv('states_upper_lower.csv', index = False)