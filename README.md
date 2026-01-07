# GPU Exploratory Data Analysis (1986–2026)

## Project Overview
This project performs an exploratory data analysis (EDA) on GPU specifications released between 1986 and 2026.  
The goal is to understand how GPU hardware has evolved over time and to analyze trade-offs between performance, memory capacity (VRAM), and power consumption (TDP).

The analysis focuses on:
- Distribution of GPU releases across brands
- Trends in clock speeds and VRAM over time
- Performance–power and memory–power trade-offs

This is an **exploratory analysis**, not a predictive modeling project.

---

## Dataset
- **Source:** Kaggle – GPU specifications dataset  
- **Time Range:** 1986–2026  

### Features Used
- Brand
- Release Year
- Clock Speed (MHz)
- VRAM (GB)
- TDP (Watts)

### Data Characteristics
- The dataset is **highly unbalanced**, with NVIDIA dominating the number of GPU entries.
- Several columns contain **missing values**, inconsistent formats, and extreme outliers.
- Older GPUs often lack complete specifications.

Significant preprocessing and aggregation were required before analysis.

---

## Key Visualizations & Insights

### 1. GPU Release Count by Brand
- NVIDIA dominates GPU releases, which biases overall averages toward NVIDIA designs.
- ATI and AMD have notable representation, while several brands have very limited data.
- Comparisons involving smaller brands should be interpreted cautiously due to low sample size.

---

### 2. GPU Clock Speed Trends Over Time (Mean)
- Average GPU clock speeds increased steadily from the late 1990s to around 2018.
- Growth slows in recent years, suggesting thermal and power limitations rather than lack of innovation.
- Yearly mean values may hide high-end or specialized GPUs released in the same year.

---

### 3. GPU VRAM Trends Over Time (Mean)
- VRAM growth was slow until the early 2010s, followed by a rapid increase.
- The sharp rise after 2015 reflects increasing demand from gaming, AI, and data-intensive workloads.
- Recent averages are influenced by high-end GPUs with very large memory capacities.

---

### 4. Clock Speed vs TDP (Performance–Power Trade-off)
- Higher clock speeds generally require higher power budgets, indicating a clear performance–power trade-off.
- Significant variation exists, showing that some GPUs achieve higher clock speeds more efficiently than others.
- Dense clustering at lower TDP values suggests many GPUs prioritize efficiency over peak performance.
- Extreme outliers were limited or excluded to improve visualization clarity.

---

### 5. VRAM vs TDP (Memory–Power Trade-off)
- Most GPUs operate within a similar VRAM–TDP range, indicating common design constraints.
- Some GPUs deliver higher VRAM with relatively moderate power consumption, showing efficient designs.
- Other GPUs require significantly higher TDP for similar VRAM levels, highlighting inefficiencies or specialized use cases.
- Extremely high-VRAM GPUs likely represent workstation or server-class hardware.

---

## Data Decisions & Methodology
- Yearly trends were calculated using **mean aggregation**.
- Scatter plots were used to analyze relationships between performance metrics and power consumption.
- Axis limits were applied in some plots to reduce the influence of extreme outliers.
- AI tools were used to assist with data cleaning and exploration, with final decisions and validation performed manually.

---

## Limitations
- Dataset imbalance across brands may bias aggregate trends.
- Mean aggregation hides distribution spread and extreme GPUs.
- The dataset does not represent real-world market share.
- Some specifications are missing or inconsistent, especially for older GPUs.

---

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code

---

## Conclusion
This analysis highlights how GPU evolution is driven by trade-offs between performance, memory capacity, and power consumption.  
While overall trends show significant growth in clock speed and VRAM, efficiency differences between GPU designs play a critical role in determining power requirements.

---

## Final Notes
This project focuses on **exploratory reasoning and visualization**, not model building.  
The emphasis is on understanding trends, constraints, and design trade-offs in GPU hardware.

