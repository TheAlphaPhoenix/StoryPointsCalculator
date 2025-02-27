import streamlit as st

def calculate_story_points(scope, stakeholders, compliance, data_analysis, operations, time_commitment, risk):
    scores = {"Low": 1, "Medium": 3, "High": 5}
    
    # Calculate total score based on inputs
    total_score = (scores[scope] + scores[stakeholders] + scores[compliance] + 
                   scores[data_analysis] + scores[operations] + scores[time_commitment] + scores[risk])
    
    # Map total score to Fibonacci-based story points
    if total_score <= 8:
        story_points = 1
    elif total_score <= 12:
        story_points = 2
    elif total_score <= 16:
        story_points = 3
    elif total_score <= 22:
        story_points = 5
    elif total_score <= 28:
        story_points = 8
    elif total_score <= 34:
        story_points = 13
    else:
        story_points = 21
    
    complexity_level = "Simple" if story_points <= 3 else "Moderate" if story_points <= 8 else "Complex"
    suggested_sprint = "Short-Term" if story_points <= 5 else "Mid-Term" if story_points <= 13 else "Long-Term"
    
    return total_score, story_points, complexity_level, suggested_sprint

# Streamlit UI
st.title("Story Points Calculator")

st.sidebar.header("Select Complexity Levels")
options = ["Low", "Medium", "High"]

scope = st.sidebar.selectbox("Scope Complexity", options)
stakeholders = st.sidebar.selectbox("Stakeholder Engagement", options)
compliance = st.sidebar.selectbox("Regulatory & Compliance Complexity", options)
data_analysis = st.sidebar.selectbox("Data Analysis & Financial Modeling", options)
operations = st.sidebar.selectbox("Operational Change & Implementation Effort", options)
time_commitment = st.sidebar.selectbox("Time Commitment", options)
risk = st.sidebar.selectbox("Risk & Uncertainty", options)

if st.sidebar.button("Calculate Story Points"):
    total_score, story_points, complexity_level, suggested_sprint = calculate_story_points(
        scope, stakeholders, compliance, data_analysis, operations, time_commitment, risk
    )
    
    st.subheader("Results")
    st.write(f"**Total Score:** {total_score}")
    st.write(f"**Story Points:** {story_points}")
    st.write(f"**Complexity Level:** {complexity_level}")
    st.write(f"**Suggested Sprint Length:** {suggested_sprint}")

# Footer with Copyright Notice
st.markdown("---")
st.markdown("© 2024 Rise Informatics. All Rights Reserved.")

