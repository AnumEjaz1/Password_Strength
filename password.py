import streamlit as st
import re

# Set page config
st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔐 Password Strength Checker")

st.markdown("""
Welcome to the **Password Strength Checker**!  
This tool helps you determine how **strong** your password is and provides **suggestions** for improvement.
""")

# Password input field
password = st.text_input("Enter your password", type="password")

# Show info message when no password is entered
if not password:
    st.info("Please enter your password to get started.")
else:
    feedback = []
    score = 0

    # Check length (stronger weight for longer passwords)
    if len(password) >= 12:
        score += 2
    elif len(password) >= 10:
        score += 1
    else:
        feedback.append("🔴 Password should be at least 10 characters long.")

    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("🟠 Include at least **one uppercase letter** (A-Z).")

    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🟠 Include at least **one lowercase letter** (a-z).")

    # Check for digit
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🟠 Include at least **one number** (0-9).")

    # Check for special character (updated regex to include more characters)
    if re.search(r'[!@#$%^&*(),.?":{}|<>[\]\\/~_+=-]', password):
        score += 1
    else:
        feedback.append("🟠 Include at least **one special character** (e.g., !@#$%, ^&*).")

    # Display password strength
    strength_level = ["❌ Weak", "⚠️ Moderate", "✅ Strong"]
    
    if score >= 5:
        st.success(f"{strength_level[2]} Password!")
        strength = 100
        # Display unique remark when all suggestions are completed
        st.markdown("### 🌟 Remark: Excellent choice! Your password is very secure.")
    elif score >= 3:
        st.warning(f"{strength_level[1]} Password! Consider improving it.")
        strength = 60
    else:
        st.error(f"{strength_level[0]} Password! It needs significant improvement.")
        strength = 30

    # Progress bar for visual strength indicator
    st.progress(strength / 100)

    # Show feedback
    if feedback:
        st.markdown("### 🔍 Suggestions to improve your password:")
        for tip in feedback:
            st.markdown(f"- {tip}")
