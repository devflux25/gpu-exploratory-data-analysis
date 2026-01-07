# gpu-exploratory-data-analysis
Exploratory data analysis of GPU specifications (1986–2026) focusing on performance, memory, and power trade-offs.
Project Overview

This project performs an exploratory data analysis (EDA) on GPU specifications released between 1986 and 2026.
The goal is to understand how GPU design has evolved over time in terms of release frequency, clock speeds, memory capacity (VRAM), and power consumption (TDP), and to analyze the trade-offs between performance and power.

The project focuses on trend analysis, distribution analysis, and relationship analysis, rather than prediction.

Dataset

Source: Kaggle (GPU specifications dataset)

Time Range: 1986–2026

Features Used:

Brand

Release Year

Clock Speed (MHz)

VRAM (GB)

TDP (Watts)

Data Characteristics

The dataset is highly unbalanced, with some brands (e.g., NVIDIA) dominating the number of entries.

Several columns contain missing values, inconsistent formats, and extreme outliers.

Older GPUs often lack complete specifications.

Significant preprocessing and aggregation were required before analysis.

Key Visualizations & Insights
1. GPU Release Count by Brand

NVIDIA dominates the dataset in terms of GPU releases, which may bias overall averages.

ATI and AMD also have substantial representation, while several brands have very limited data.

Insights drawn from smaller brands should be interpreted cautiously due to low sample size.

2. GPU Clock Speed Trends Over Time (Mean)

Average GPU clock speeds increased steadily from the late 1990s to around 2018.

Growth slows in recent years, suggesting thermal and power limitations rather than lack of innovation.

Mean aggregation may hide high-end or specialized GPUs released in the same year.

3. GPU VRAM Trends Over Time (Mean)

VRAM growth was slow until the early 2010s, followed by a rapid increase.

The sharp rise after 2015 reflects growing demands from gaming, AI, and data-intensive workloads.

Recent averages are influenced by high-end and professional GPUs with very large memory capacities.

4. Clock Speed vs TDP (Performance–Power Trade-off)

Higher clock speeds generally require higher power budgets, indicating a clear performance–power trade-off.

Significant variance exists, showing that some GPUs achieve higher clock speeds more efficiently than others.

Dense clustering at lower TDP values suggests many GPUs prioritize efficiency over peak performance.

Extreme outliers were excluded or limited in visualization to improve readability.

5. VRAM vs TDP (Memory–Power Trade-off)

Most GPUs operate within a similar VRAM–TDP range, indicating common design constraints.

Some GPUs deliver higher VRAM with relatively moderate power consumption, showing efficient designs.

Other GPUs require significantly higher TDP for similar VRAM levels, highlighting inefficiencies or specialized use cases.

Extremely high-VRAM GPUs likely represent workstation or server-class hardware.

Data Decisions & Methodology

Yearly trends were calculated using mean values for clock speed and VRAM.

Scatter plots were used to analyze relationships between performance metrics and power consumption.

Axis limits were applied in some visualizations to reduce the impact of extreme outliers.

AI tools were used to assist with data cleaning and exploration, with final decisions validated manually.

Limitations

Dataset imbalance across brands may bias aggregate trends.

Mean aggregation hides distribution spread and extreme GPUs.

The dataset does not represent real-world market share.

Some specifications are missing or inconsistent, especially for older GPUs.

Conclusion

This analysis highlights how GPU evolution is driven by trade-offs between performance, memory capacity, and power consumption.
While overall trends show significant growth in clock speed and VRAM, efficiency differences between GPU designs play a critical role in determining power requirements.

Tools Used

Python

Pandas

NumPy

Matplotlib

Seaborn

VS Code
