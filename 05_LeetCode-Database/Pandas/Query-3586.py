import pandas as pd

def find_covid_recovery_patients(patients: pd.DataFrame, covid_tests: pd.DataFrame) -> pd.DataFrame:
    tests = covid_tests.sort_values(["patient_id", "test_date"])
    
    results = []

    for pid, group in tests.groupby("patient_id"):
        g = group.sort_values("test_date")

        positives = g[g["result"] == "Positive"]
        if positives.empty:
            continue
        
        first_pos_date = positives.iloc[0]["test_date"]

        negatives = g[(g["result"] == "Negative") & (g["test_date"] > first_pos_date)]
        if negatives.empty:
            continue
        
        first_neg_date = negatives.iloc[0]["test_date"]

        recovery_days = (pd.to_datetime(first_neg_date) - pd.to_datetime(first_pos_date)).days

        results.append([pid, recovery_days])

    if not results:
        return pd.DataFrame(columns=["patient_id","patient_name","age","recovery_time"])

    recovered_df = pd.DataFrame(results, columns=["patient_id", "recovery_time"])

    final = recovered_df.merge(patients, on="patient_id")

    final = final[["patient_id", "patient_name", "age", "recovery_time"]]

    final = final.sort_values(["recovery_time", "patient_name"]).reset_index(drop=True)

    return final    