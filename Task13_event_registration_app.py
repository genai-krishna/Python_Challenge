# ============================================================
# 📅 Event Registration System using Streamlit
# ============================================================
# Features:
# - Collect user details (Name, Email, Ticket Type)
# - Validate inputs before submission
# - Store all registration data into a CSV file
# - Display confirmation message on successful registration
# ============================================================

import streamlit as st
import pandas as pd
import os

# File path to store registrations
CSV_FILE = "event_registrations.csv"

# ------------------------------------------------------------
# Function: Save registration details to CSV
# ------------------------------------------------------------
def save_registration(name, email, ticket_type):
    """Saves registration details to a CSV file."""
    data = {"Name": [name], "Email": [email], "Ticket Type": [ticket_type]}
    df = pd.DataFrame(data)

    # If file exists, append; otherwise, create a new file
    if os.path.exists(CSV_FILE):
        df.to_csv(CSV_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(CSV_FILE, index=False)


# ------------------------------------------------------------
# Streamlit UI
# ------------------------------------------------------------
st.set_page_config(page_title="🎟️ Event Registration", layout="centered")

st.title("🎉 Event Registration Form")
st.write("Welcome! Please fill in the details below to register for the event.")

# Create a form for user input
with st.form("registration_form", clear_on_submit=True):
    st.subheader("📝 Personal Information")

    name = st.text_input("Full Name")
    email = st.text_input("Email Address")

    st.subheader("🎫 Ticket Details")
    ticket_type = st.selectbox(
        "Select Ticket Type",
        ["-- Select --", "General Admission", "VIP", "Student Pass"]
    )

    submit = st.form_submit_button("Register")

    # --------------------------------------------------------
    # Form Validation
    # --------------------------------------------------------
    if submit:
        if not name or not email or ticket_type == "-- Select --":
            st.error("⚠️ Please fill in all fields before submitting.")
        elif "@" not in email or "." not in email:
            st.error("📧 Please enter a valid email address.")
        else:
            save_registration(name, email, ticket_type)
            st.success(f"✅ Thank you, {name}! You have successfully registered.")
            st.info(f"📩 A confirmation will be sent to: **{email}** (optional feature).")


# ------------------------------------------------------------
# Optional: Display current registrations
# ------------------------------------------------------------
st.markdown("---")
st.subheader("📋 Registered Participants (Preview)")

if os.path.exists(CSV_FILE):
    data = pd.read_csv(CSV_FILE)
    st.dataframe(data)
else:
    st.write("No registrations yet. Be the first to register! 🎉")
