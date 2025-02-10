# PF-ISM_Simulation
# PF-ISM vs FISM Simulation

This repository contains a Python-based simulation comparing **Picture Fuzzy Interpretive Structural Modeling (PF-ISM)** with the classical **Fuzzy Interpretive Structural Modeling (FISM)** method. The comparison is based on the **Dice-Sørensen Similarity (DSS)** metric, providing insights into the structural differences and similarities between these two methodologies.

## Overview

- **PF-ISM:** Incorporates Picture Fuzzy Sets to better handle uncertainty by considering membership, non-membership, and indeterminacy degrees.
- **FISM:** Classical fuzzy logic-based method that models relationships with fuzzy numbers.

This simulation helps evaluate the robustness and sensitivity of PF-ISM compared to the classical FISM approach.

## Features

- Random generation of expert opinions and factor interactions.
- Aggregation and defuzzification of both fuzzy and picture fuzzy numbers.
- Calculation of reachability matrices and thresholding.
- Similarity analysis using Dice-Sørensen Similarity.
- Visualization of results through boxplots.

## Prerequisites

Ensure you have Python 3.6 or higher installed. The following libraries are required:

```bash
pip install numpy matplotlib
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/yourusername/pfism-fism-simulation.git
cd pfism-fism-simulation
```

2. Run the simulation script:

```bash
python pfism_fism_simulation.py
```

3. Enter the number of replications when prompted to start the simulation.

## Output

- **Dice-Sørensen Similarity (DSS):** The similarity scores between PF-ISM and FISM reachability matrices are displayed.
- **Visualization:** A boxplot showing the distribution of DSS across all replications.
- **Console Output:** Average DSS and standard error of the simulation.

## Example

```bash
Enter the number of replications: 10
Average DSS: 0.85
Standard Error: 0.03
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This simulation is part of a comparative study on fuzzy modeling techniques.
- Inspired by methodologies in **multi-criteria decision-making** and **structural modeling** research.
