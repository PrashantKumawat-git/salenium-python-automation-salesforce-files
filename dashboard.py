import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt

# Load JSON report
with open('reports/results.json') as f:
    data = json.load(f)

st.set_page_config(page_title="Test Dashboard", layout="wide")
st.title("📊 Pytest Execution Dashboard")

# ---------- Summary Bar Chart ----------
st.header("✅ Summary")
summary = data.get('summary', {})
summary_df = pd.DataFrame.from_dict(summary, orient='index', columns=['Count'])

col1, col2 = st.columns([2, 2])
with col1:
    st.bar_chart(summary_df)

# ---------- Detailed Test Data ----------
tests = pd.DataFrame(data.get('tests', []))
if not tests.empty:
    tests['file'] = tests['nodeid'].apply(lambda x: x.split("::")[0])
    tests['test'] = tests['nodeid'].apply(lambda x: x.split("::")[-1])
    outcome_counts = tests['outcome'].value_counts()

    # ---------- Outcome Pie Chart ----------
    with col2:
        st.subheader("🧁 Test Result Distribution (Pie)")
        fig1, ax1 = plt.subplots()
        ax1.pie(outcome_counts, labels=outcome_counts.index, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)

    # ---------- Charts by Outcome ----------
    st.header("📌 Breakdown by Outcome")

    col_passed, col_failed = st.columns(2)
    with col_passed:
        passed = tests[tests['outcome'] == 'passed']
        st.subheader("✅ Passed Tests")
        st.bar_chart(passed['file'].value_counts())

    with col_failed:
        failed = tests[tests['outcome'] == 'failed']
        st.subheader("❌ Failed Tests")
        if not failed.empty:
            st.bar_chart(failed['file'].value_counts())
        else:
            st.info("No failed tests.")

    col_skipped, col_error = st.columns(2)
    with col_skipped:
        skipped = tests[tests['outcome'] == 'skipped']
        st.subheader("⚠️ Skipped Tests")
        if not skipped.empty:
            st.bar_chart(skipped['file'].value_counts())
        else:
            st.info("No skipped tests.")

    with col_error:
        error = tests[tests['outcome'] == 'error']
        st.subheader("🚨 Errors")
        if not error.empty:
            st.bar_chart(error['file'].value_counts())
        else:
            st.info("No errors.")

    # ---------- All Test Details Table ----------
    st.header("🔎 Detailed Test Cases")
    st.dataframe(tests[['file', 'test', 'outcome']])
else:
    st.warning("No test results found.")
