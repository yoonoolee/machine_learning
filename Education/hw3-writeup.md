# Education Data Analysis

## Why is the `bar_chart_high_school` ineffective, and what do you suggest to improve the plot?
# We can see from the bar chart that there is not much of a difference between the values for A, M, and F, 
# or at least it seems like it. In order to see those differences more easily, you will have to set the 
# y-axis min and max to see the differences more close up. Basically, you are "zooming into" the data to
# see the differences between the percentage values. 


## How and why did you choose the plot for `plot_hispanic_min_degree`?
# I chose to do a line plot using the relplot() function because they are effective at 
# showing the progression of a value over time. Another benefit is that you can draw multiple 
# lines, so in this case, one line for high school and another for bachelors, and 
# distinguish them with different colors.


## Describe a possible bias present in this dataset and why it might have occurred.
# It seems like there are quite a lot of missing values that was removed from the data. It is better than 
# setting them to 0 because we cannot just assume it to be 0, but having that many missing values can be a problem.
# There can also be bias in only looking at the Race not the Ethnicity. For example, 
# generally speaking within the Asian Race, South and East Asians tend to have gotten more education
# than Southeast Asians, etc. Grouping them all into one category can be misleading. 
# Another possible bias is assuming 'high school' is the 'lowest' rank, where some people might not
# have graduated high school. And assuming 'masters' is the 'highest' rank, instead of PhD, etc.
# Another problem is the '2+ Races'. It is too general and could have altered data. 


## Describe an application, analysis, or decision motivated by this dataset with the intended goal of improving educational equity but that ultimately exacerbates social injustice.
# An example would be the problem with Asian Race stated above. For example, 
# a school might want to give a college scholarship to an underrepresented group based on this data.
# Let's assume that group A of Asians have had lots of opportunities for college education historically, 
# whereas group B of Asians have not. Seeing from this dataset that Asians in general have had 
# lots of opportunities, the school might give the scholarship to a different group.
# In real life, some companies and schools have started to remove 'Asians' as a 'minority' category because
# many Asians have already benefited for being categorized as such, but not all subgroups of Asians have benefited, 
# such as Filipinos, Indonesians, etc.


