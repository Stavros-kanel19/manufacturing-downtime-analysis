# Manufacturing Downtime Analysis

## Project Overview

This project analyses manufacturing line productivity and downtime using Microsoft Excel, Power Query, Power Pivot Tables, Python, and statistical thinking.

The goal was to evaluate line efficiency, identify the main downtime drivers, compare operator and product performance, and use production time ratio as a normalized metric for fairer comparisons across different products.

---

## Business Questions

This analysis focuses on the following questions:

1. What is the overall production line efficiency?
2. Which products and operators show lower efficiency?
3. What are the main downtime factors?
4. Which operator/factor combinations contribute most to downtime?
5. How does production time ratio vary by operator and product?

---

## Tools Used

- Microsoft Excel
- Power Query
- Power Pivot Tables
- Excel Data Model/Star Schema
- Python
- pandas
- matplotlib
- seaborn

---

## Dashboard Pages

The Excel workbook contains three main dashboard pages:

1. **Operator Dashboard**  
   Summarizes operator performance, batch count, efficiency, time ratio, shift details, and best/worst batches.

2. **Products & Downtimes Dashboard**  
   Shows product efficiency, production counts, main downtime factors, Pareto-style downtime analysis, and downtime by operator and factor.

3. **Details Dashboard**  
   Provides additional statistical views using time ratio and product/operator efficiency comparisons.

Supporting sheets with cleaned data, pivot tables, and helper calculations  are hidden in the workbook to keep the final file user-friendly.

---

## Key Metrics

- Total Batches: 38
- Total Production Time: 3.858 minutes
- Overall Efficiency: 64,02%
- Overall Time Ratio: 1,56
- Total Batch Overtime: 1.388 minutes

---

## Key Findings

- Machine adjustment was the leading downtime factor.
- Machine failure and inventory shortage were also major contributors.
- Operator comparison should be interpreted carefully because product mix affects performance.
- Time Ratio was used to normalize actual production time against product-specific minimum batch time.
- Product/operator groups with only one batch were excluded from the boxplot comparison because boxplots require repeated observations.

---

## Methodology

The project included:

1. Cleaning and transforming the manufacturing data in Power Query.
2. Creating calculated fields for production time, batch overtime, efficiency, and time ratio.
3. Building pivot tables and supporting helper sheets.
4. Designing Excel dashboards for operational performance analysis.
5. Using Python to generate boxplots for additional statistical exploration.
6. Interpreting operator, product, and downtime factor patterns.

---
## Credits

Dataset source: Maven Analytics guided project dataset.

Some dashboard visual assets, such as icons and background images, were AI-generated for presentation purposes.

## Python Analysis

Python was used to generate the boxplot analysis included in the Details dashboard:

- Time Ratio by Operator
- Time Ratio by Product
- Product vs Operator Efficiency, filtered to groups with more than one batch

The Python script can be found in:

```text
Python_files/manufacturing_boxplots.py
```

---

## Screenshots

### Operator Dashboard

![Operator Dashboard](Dashboard/Operator_Dashboard.png)

### Products & Downtimes Dashboard

![Products and Downtimes Dashboard](Dashboard/Product%26Downtimes_Dashboard.png)

### Details Dashboard

![Details Dashboard](Dashboard/Details_Dashboard.png)


