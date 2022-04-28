import pandas as pd
import matplotlib.pyplot as plt

# read the file with data
studPerformance = pd.read_csv('StudentsPerformance.csv')

# Create new dataframe which shows mean of math score grouped by ethnicity
studPerformance_math = studPerformance.groupby('race/ethnicity')['math score'].mean()

# Print average math results for each ethnicity group
for group, avg in studPerformance_math.iteritems():
    print('%s mean math score: %s' % (group, str(avg)))

# Create new dataframe for students who completed the test preparation course 
# and their parent obtained a degree
degree_test = studPerformance.loc[(studPerformance['test preparation course'] == 'completed') & (studPerformance['parental level of education'].isin(["associate's degree", "bachelor's degree", "master's degree"]))]

# For each exam part print average results
areas = ['math', 'reading', 'writing']
for area in areas:
    print(area, degree_test[f'{area} score'].mean())
    

# plot the histogram of math scores divided by reading scores for each student
plt.hist(studPerformance['math score'] / studPerformance['reading score'])
# add plot title
plt.title('ratio')
# show plot
plt.show()
# close plot
plt.close()










