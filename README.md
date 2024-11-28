# Reaction Yield Optimization Using Genetic Algorithm

## Overview

This project uses a **Genetic Algorithm (GA)** to optimize reaction yield by varying key reaction parameters: **temperature**, **pressure**, and **catalyst concentration**. The project utilizes a **Linear Regression model** trained on synthetic data stored in a CSV file. This modular approach makes the dataset easily replaceable for more realistic or real-world data.

---

## Table of Contents

1. [Project Objective](#project-objective)
2. [Dataset](#dataset)
3. [Methodology](#methodology)
4. [Requirements](#requirements)
5. [How to Run](#how-to-run)
6. [Key Outputs](#key-outputs)
7. [File Structure](#file-structure)
8. [Future Enhancements](#future-enhancements)
9. [License](#license)

---

## Project Objective

The goal of this project is to:

1. Predict reaction yield using a **Linear Regression model** trained on reaction parameters.
2. Optimize the predicted yield by identifying the best combination of reaction parameters using a **Genetic Algorithm**.

---

## Dataset

The synthetic dataset is stored in a CSV file named `reaction_data.csv`. It contains information about reaction parameters and corresponding yields:

- **Columns**:

  - Temperature (°C)
  - Pressure (atm)
  - Catalyst Concentration (%)
  - Yield (%)

- **Sample Rows**:

| Temperature (°C) | Pressure (atm) | Catalyst Concentration (%) | Yield (%) |
| ---------------- | -------------- | -------------------------- | --------- |
| 300              | 50             | 1.0                        | 85        |
| 320              | 55             | 1.2                        | 87        |
| ...              | ...            | ...                        | ...       |

You can replace this dataset with a real-world dataset to make the optimization more meaningful.

---

## Methodology

1. **Data Loading**:

   - The dataset is loaded from the `reaction_data.csv` file.

2. **Linear Regression**:

   - A regression model predicts yield based on reaction parameters (temperature, pressure, and catalyst concentration).

3. **Fitness Function**:

   - The fitness function uses the regression model to compute the yield for a given set of parameters.
   - The GA minimizes the negative yield to find the optimal parameters.

4. **Genetic Algorithm**:
   - Explores the parameter space to maximize the predicted yield by optimizing:
     - Temperature (°C)
     - Pressure (atm)
     - Catalyst Concentration (%)

---

## Requirements

Install the required Python libraries before running the project:

```bash
pip install geneticalgorithm numpy scikit-learn pandas
```

## How To Run

1. **Prepare the Dataset**:

   - Ensure the file reaction_data.csv is in the same directory as the Python script.
     -The dataset must have four columns: Temperature, Pressure, Catalyst Concentration, Yield.

2. **Run the Script**:

   -Execute the Python script:

```bash
python reaction_yield_optimization.py
```

3. **Outputs**:

   - The script will output:
     -The optimal reaction parameters.
     -The maximum predicted yield.

---

## Key Outputs

1. **Optimal Parameters**:
   - Example:

```bash
Optimal Parameters (T, P, C): [420, 80, 2.5]
```

2. **Maximum Predicted Yield**:

   - Example:

```bash
Maximum Predicted Yield: 95.0
```

## Future Enhancements

1. **Use Real-World Data**:
   Replace the synthetic dataset with data from experiments or chemical databases.

2. **Enhanced Models**:
   Incorporate more complex models like Polynomial Regression or Machine Learning models for better predictions.

3. **Visualization**:
   Add charts to visualize how parameters affect yield and the GA optimization process.

4. **Parameter Constraints**:
   Include constraints or penalties for infeasible parameter combinations.
