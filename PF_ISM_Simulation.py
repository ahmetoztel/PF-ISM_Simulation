import numpy as np
import random
import matplotlib.pyplot as plt

def pfism_fism_simulation():
    replications = int(input("Enter the number of replications: "))
    DSS = []

    for w in range(replications):
        z = random.randint(5, 20)  # Number of experts
        x = random.randint(10, 30)  # Number of factors

        # Initialize matrices
        rndmat = np.zeros((x, x, z), dtype=int)
        PFExpert = np.zeros((x, x, z), dtype=object)
        FExpert = np.zeros((x, x, z), dtype=object)
        PFDec = np.zeros((x, x), dtype=object)
        FDec = np.zeros((x, x), dtype=object)
        PFCrispDec = np.zeros((x, x))
        FCrispDec = np.zeros((x, x))
        PFIRM = np.zeros((x, x), dtype=int)
        FIRM = np.zeros((x, x), dtype=int)

        # Fill rndmat and initialize PFExpert and FExpert
        for t in range(z):
            for i in range(x):
                for j in range(x):
                    rndmat[i, j, t] = random.choice([0, 1, 2, 3, 4, -1]) if i != j else 4

                    # Fuzzy expert opinions
                    FExpert[i, j, t] = {
                        0: {"Le": 0, "Mi": 0, "Ri": 0.25},
                        1: {"Le": 0, "Mi": 0.25, "Ri": 0.5},
                        2: {"Le": 0.25, "Mi": 0.5, "Ri": 0.75},
                        3: {"Le": 0.5, "Mi": 0.75, "Ri": 1.0},
                        4: {"Le": 0.75, "Mi": 1.0, "Ri": 1.0}
                    }[rndmat[i, j, t] if rndmat[i, j, t] != -1 else 0]

                    # Picture Fuzzy expert opinions (membership, non-membership, indeterminacy)
                    PFExpert[i, j, t] = {
                        0: {"M": 0.10, "NM": 0.00, "I": 0.85},
                        1: {"M": 0.25, "NM": 0.05, "I": 0.60},
                        2: {"M": 0.50, "NM": 0.10, "I": 0.40},
                        3: {"M": 0.75, "NM": 0.05, "I": 0.10},
                        4: {"M": 0.90, "NM": 0.00, "I": 0.05},
                        -1: {"M": 0.00, "NM": 0.20, "I": 0.00}
                    }[rndmat[i, j, t]]

        # Aggregate expert decisions
        for i in range(x):
            for j in range(x):
                Fl, Fm, Fr = 0, 0, 0
                M_sum, NM_sum, I_sum = 0, 0, 0

                for t in range(z):
                    Fl += FExpert[i, j, t]["Le"]
                    Fm += FExpert[i, j, t]["Mi"]
                    Fr += FExpert[i, j, t]["Ri"]

                    M_sum += PFExpert[i, j, t]["M"]
                    NM_sum += PFExpert[i, j, t]["NM"]
                    I_sum += PFExpert[i, j, t]["I"]

                # Fuzzy ISM aggregation and defuzzification
                FDec[i, j] = {"Le": Fl / z, "Mi": Fm / z, "Ri": Fr / z}
                FCrispDec[i, j] = (FDec[i, j]["Le"] + 2 * FDec[i, j]["Mi"] + FDec[i, j]["Ri"]) / 4

                # Picture Fuzzy ISM aggregation and defuzzification (using score function)
                PFDec[i, j] = {"M": M_sum / z, "NM": NM_sum / z, "I": I_sum / z}
                PFCrispDec[i, j] = PFDec[i, j]["M"] - PFDec[i, j]["NM"]

        # Compute thresholds
        PFThreshold = np.sum(PFCrispDec) / (x * x)
        FuzzyThreshold = np.sum(FCrispDec) / (x * x)

        # Generate binary reachability matrices
        PFIRM = (PFCrispDec >= PFThreshold).astype(int)
        FIRM = (FCrispDec >= FuzzyThreshold).astype(int)
        np.fill_diagonal(PFIRM, 1)
        np.fill_diagonal(FIRM, 1)

        # Compute Dice-Sørensen similarity
        JaccA = np.sum(PFIRM)
        JaccB = np.sum(FIRM)
        Joint = np.sum(np.logical_and(PFIRM, FIRM))
        DSS.append(2 * Joint / (JaccA + JaccB))

    # Calculate average DSS and standard error
    AveDSS = np.mean(DSS)
    SE = np.std(DSS, ddof=1)

    # Visualization
    plt.boxplot(DSS, vert=True, patch_artist=True, showmeans=True, meanline=True)
    plt.title("Dice-Sørensen Similarity: PFISM vs. FISM")
    plt.ylabel("DSS")
    plt.xticks([1], ["Simulation Results"])
    for i, value in enumerate(DSS):
        plt.scatter(1, value, alpha=0.6, color="blue", label="Data Points" if i == 0 else "")
    plt.text(1.1, np.mean(DSS), f"Mean: {np.mean(DSS):.2f}", color="red")
    plt.text(1.1, np.mean(DSS) - np.std(DSS), f"SD: {np.std(DSS, ddof=1):.2f}", color="green")
    plt.text(1.1, min(DSS), f"Replications: {len(DSS)}", color="blue")
    plt.legend()
    plt.show()

    return AveDSS, SE

# Example usage
average_dss, standard_error = pfism_fism_simulation()
print(f"Average DSS: {average_dss}")
print(f"Standard Error: {standard_error}")