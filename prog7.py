# In streamlit we do NOT have the option to create multiple pages in single app.
# But we can create an illusion of multiple pages using  sidebar and widgets.

# ------------------------------------------
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")
data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}
df = pd.DataFrame(data = data)
# ------------------------------------------
navigation = st.sidebar.radio(
    label = "My Project",
    options = ["Home", "About Us", "Contact"],
    index = 1
)

if navigation == "Home":

    selected_col = st.sidebar.selectbox(
        label = "Select a column: ",
        options = df.columns
    )
    fig, ax = plt.subplots()
    ax.plot(df["num"], df[selected_col])
    st.pyplot(fig)
    # Except write(), echo() and spinner(), everything else can be done on sidebars.
    selected_col = st.sidebar.multiselect(
        label = "Select multiple columns: ",
        options = df.columns
    )
    fig, ax = plt.subplots()
    for col_name in selected_col:
        ax.plot(df["num"], df[selected_col])
    st.pyplot(fig)

elif navigation == "About Us":
    st.title("About Us")
    st.write("I am CSE student in the prefinal year at DSCE, Bangalore.")

elif navigation == "Contact":
    st.title("Contact")
    st.write("You can reachout to me at aum123@gmail.com")