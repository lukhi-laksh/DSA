import pandas as pd

def find_overbooked_employees(employees: pd.DataFrame, meetings: pd.DataFrame) -> pd.DataFrame:
    meetings["meeting_date"] = pd.to_datetime(meetings["meeting_date"])
    meetings["meeting_week"] = meetings["meeting_date"].dt.isocalendar().week
    meetings["meeting_year"] = meetings["meeting_date"].dt.year

    meetings = meetings.groupby(["employee_id", "meeting_week", "meeting_year"],as_index=False).agg(
        meeting_time=("duration_hours", "sum"),
    )

    meetings = meetings[meetings["meeting_time"] > 20]
    meetings = meetings.groupby("employee_id").agg(meeting_heavy_weeks=("employee_id", "count")).merge(employees, on="employee_id")
    meetings = meetings[meetings["meeting_heavy_weeks"] > 1]

    return meetings[[
        "employee_id", 
        "employee_name", 
        "department", 
        "meeting_heavy_weeks"
    ]].sort_values(by=["meeting_heavy_weeks", "employee_name"], ascending=[False, True])