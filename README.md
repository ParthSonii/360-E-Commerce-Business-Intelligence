#  360 E-Commerce Business Intelligence System

##  Problem Statement
An e-commerce marketplace was sitting on 119,000+ orders 
across 9 data tables with no unified view of business performance.

Key questions were unanswered:
- Who are our most valuable customers and who are we about to lose?
- Which product categories drive revenue vs which ones lose customer trust?
- Why do some regions get delivery in 8 days while others wait 30 days?
- What does the entire business look like in one single executive view?

This project answers all of these questions — from raw messy data 
to executive dashboard.

---

##  Project Objective
Build a complete 360° Business Intelligence pipeline covering:
- Data engineering — cleaning and merging 9 relational datasets
- Customer analytics — RFM segmentation (Champions, At Risk, Lost)
- Financial analytics — revenue trends, AOV, payment behavior
- Product analytics — category performance matrix
- Operational analytics — regional delivery and seller analysis
- Executive reporting — multi-panel KPI dashboard

---

##  Dataset
- **Source:** Brazilian E-Commerce Public Dataset by Olist (Kaggle)
- **Size:** 119,000+ real orders across 9 related tables
- **Period:** 2016 to 2018

---

##  Tools Used
| Tool | Purpose |
|---|---|
| Python | Core programming |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Visualization |
| Seaborn | Statistical charts |
| Jupyter Notebook | Analysis environment |

---

##  Project Structure
360-E-Commerce-Business-Intelligence/
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_customer_segmentation.ipynb
│   ├── 04_revenue_financial_analysis.ipynb
│   ├── 05_product_analysis.ipynb
│   ├── 06_regional_seller_analysis.ipynb
│   └── 07_executive_dashboard.ipynb
├── src/
│   └── analysis_utils.py
├── visuals/
│   └── [all chart PNG files]
└── README.md

---

## Key Findings

**Revenue**
- Total revenue of R$ 16.9M across 99,441 orders from 2016-2018
- Peak revenue month was November 2017 — Black Friday effect
- Average order value of R$ 154

**Customers**
- Analyzed 96,096 unique customers using RFM segmentation
- Champions drive disproportionate revenue despite small percentage
- Significant At Risk segment represents immediate win-back opportunity

**Products**
- Identified hidden gem categories — high reviews but low revenue
- Some high revenue categories show below average review scores

**Operations**
- Proved correlation between delivery time and review scores
- Seller supply concentrated in 3 states explains distant delivery delays
- Late delivery rate needs logistics investment

---

##  Business Recommendations
1. Reward Champion customers with exclusive offers
2. Launch win-back campaigns for At Risk segment immediately
3. Fix delivery in slowest states — directly improves reviews
4. Promote hidden gem categories to diversify revenue
5. Recruit sellers outside top 3 states to reduce delivery time
6. Prepare inventory for November peak 2 months in advance

---

##  How to Run
1. Clone this repository
2. Download Olist dataset from Kaggle
3. Place CSV files in `data/raw/`
4. Run notebooks in order 01 to 07
5. All charts save automatically to `visuals/`

---

##  Learning Approach
This project was built as a structured self-learning exercise.
I used Claude AI as a learning mentor to understand concepts
and debug errors — similar to using Stack Overflow or a senior
colleague. Every concept I can explain and every decision has
a specific reason behind it.

---

##  Author
**Parth Soni**
Data Analyst | Python • Pandas • SQL • Power BI • Excel
LinkedIn : www.linkedin.com/in/parthsoni16
