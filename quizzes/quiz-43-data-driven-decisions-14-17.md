# Week 43 Quiz — Data-Driven Decisions — Ages 14–17

> *10 code-focused, CBE-aligned questions for Week 43: Data-Driven Decisions.*

## Questions

1. Write a Python function that recommends a conservation action based on population trend.
2. What is a false positive and a false negative in decision systems?
3. How would you visualise a time series of turtle nest counts?
4. Explain the difference between correlation and causation.
5. Write code to find the month with the highest plastic collection.
6. What is a dashboard and why is it useful?
7. How do you handle conflicting data sources?
8. What is a confidence interval in simple terms?
9. How would you turn data into a recommendation?
10. Map data-driven decisions to CBE Data/Critical Thinking outcomes.

## Answer Key

1. def action(trend):
    if trend < -0.1: return 'urgent protection'
    elif trend < 0: return 'monitor'
    else: return 'stable'
2. False positive: alert when nothing is wrong. False negative: miss a real problem.
3. Line plot with date on x-axis and count on y-axis.
4. Correlation means variables move together; causation means one causes the other.
5. max(collections, key=lambda m: collections[m])
6. A live display of key metrics; it helps monitor situations quickly.
7. Check methodology, recency, and source credibility.
8. A range that likely contains the true value.
9. Analyse trends, identify thresholds, and propose an action.
10. Learners use evidence to make and justify decisions.
