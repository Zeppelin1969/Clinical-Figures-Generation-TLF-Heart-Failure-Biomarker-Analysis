# Clinical Figures Generation (TLF): Heart Failure Biomarker Analysis

## Project Overview
This project focuses on the "Figures" component of clinical Tables, Listings, and Figures (TLFs). Using the real-world "Heart Failure Clinical Records" dataset, this pipeline demonstrates how to perform Exploratory Data Analysis (EDA) and generate publication-ready clinical visualizations that communicate patient survival trends.

Rather than just wrangling data, the goal of this project is visual storytelling: transforming raw biomarkers (like Serum Creatinine) into clear, interpretable charts that would assist biostatisticians and medical reviewers in assessing drug efficacy and patient safety.

## Key Features & Visualizations
* **Real-World Clinical Data:** Processed a dataset containing critical heart failure biomarkers (Age, Ejection Fraction, Serum Creatinine) and follow-up survival data.
* **Distribution Analysis (Histogram):** Generated a distribution of patient age, stratified by survival outcome (`DEATH_EVENT`), to identify high-risk demographic clusters.
* **Biomarker Correlation (Scatterplot):** Mapped `serum_creatinine` levels against patient follow-up `time`, utilizing color hue to differentiate survival outcomes, highlighting potential safety thresholds.
* **Automated Figure Generation:** Built a Python script that automatically styles and exports charts as high-resolution `.png` files using clinical color palettes.

## Tech Stack
* **Language:** Python
* **Libraries:** `pandas` (Data Ingestion), `matplotlib` & `seaborn` (Data Visualization)

## How to Run
1. Clone this repository.
2. Ensure the `heart_failure_clinical_records_dataset.csv` is located in the root directory.
3. Run the Python script to execute the visualization pipeline.
4. The script will automatically generate and save the clinical figures as `.png` files in your directory.
