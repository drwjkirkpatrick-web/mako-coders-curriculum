# Week 23 Quiz — Plot the Coast — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 23: Plot the Coast.*

## Questions

1. Write code to plot a line graph of turtle sightings over 7 days.
2. What is the difference between plt.plot() and plt.scatter()?
3. How do you save a chart to a file instead of showing it?
4. Explain why adding labels and titles matters.
5. Write code to plot multiple species on the same chart.
6. What is a histogram used for?
7. How would you handle missing data before plotting?
8. Write code to set the colour of a bar chart.
9. What is a misleading graph and how do you avoid it?
10. Map plotting to a CBE Data outcome.

## Answer Key

1. plt.plot(days, sightings); plt.xlabel('Day'); plt.ylabel('Sightings'); plt.show()
2. plot connects points; scatter shows individual points.
3. plt.savefig('chart.png')
4. It makes the chart readable and trustworthy.
5. plt.plot(days, dolphins, label='Dolphins'); plt.plot(days, turtles, label='Turtles'); plt.legend()
6. Showing how often values fall into ranges.
7. Skip the missing point or use a placeholder/mean.
8. plt.bar(species, counts, color=['blue','green','red'])
9. A graph that distorts scale or omits context; use clear labels and consistent scales.
10. Learners visualise data to identify patterns and communicate findings.
