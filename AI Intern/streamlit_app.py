import streamlit as st
from collide_core import run_collide_demo

st.set_page_config(page_title="COLLIDE AI Demo", page_icon="🤖", layout="wide")
st.title("COLLIDE AI – Brand Advisory Demo")
st.markdown("Click **Run Demo** to execute the consultation flow and view results.")

if st.button("Run Demo", type="primary"):
    results = run_collide_demo()
    st.success("Demo completed")
    st.subheader("Assessment")
    st.json(results.get("assessment", {}))
    st.subheader("Strategy")
    st.json(results.get("strategy", {}))
    st.subheader("Report")
    st.write(results.get("report", {}).get("executive_summary", ""))
else:
    st.info("Press the button to start the demo.")
