# Function to compare Files
#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import streamlit as st
import os

def compareFiles(acc,podd,destination_path):

    # Change index of acc to Roll Number
    acc.index = acc["Roll Number"]
    podd.index = podd["Roll No"]

    # Define columns of interest for both DataFrames
    intrest_cols_p = ["Company - Job Offer Details", "Title - Job Offer Details", "Package - Job Offer Details"]
    intrest_cols_a = ["Campus Placement", "Designation", "CTC Offered"]

    rollnumbers_in_intrest = podd["Roll No"].tolist()

    # Create a new DataFrame by using intrest_cols_p from podd and intrest_cols_a from acc, and compare each one
    intrest_df = podd[intrest_cols_p].join(acc[intrest_cols_a], how="inner")

    # Assuming intrest_df is your DataFrame and intrest_cols_p and intrest_cols_a are lists of column names
    intrest_df["Mismatched Columns"] = intrest_df.apply(lambda row: ", ".join([col_a for col_p, col_a in zip(intrest_cols_p, intrest_cols_a) if row[col_p] != row[col_a]]), axis=1).replace('', 'No Mismatch', regex=True)

    # Save the results to Excel
    destination_path = destination_path + "\\"
    destination_path = os.path.join(destination_path, "Mismatch_Data.xlsx")
    intrest_df.to_excel(destination_path)


# Create a Streamlit app
st.title("Choose Two Excel Files and Destination Path")

# Upload the first Excel file
st.subheader("Upload the first Excel file:")
file_1 = st.file_uploader("Choose a file", type=["xlsx", "xls"])

# Upload the second Excel file
st.subheader("Upload the second Excel file:")
file_2 = st.file_uploader("Choose another file", type=["xlsx", "xls"])

# Get the destination path from the user
destination_path = st.text_input("Enter the destination path:")

# Function to read and display Excel data
def display_excel_data(file):
    if file is not None:
        df = pd.read_excel(file)
        st.dataframe(df)

# Function to read and display Excel data
def display_excel_data(file):
    if file is not None:
        df = pd.read_excel(file)
        st.dataframe(df)
        return df  # Return the DataFrame

# Display the contents of the uploaded Excel files
if file_1 is not None:
    st.subheader("Contents of the first Excel file:")
    display_excel_data(file_1)

if file_2 is not None:
    st.subheader("Contents of the second Excel file:")
    display_excel_data(file_2)

# Add a button to save the files to the destination path
if file_1 is not None and file_2 is not None and destination_path is not None:
    if st.button("Compare Files"):
        # Save the files to the specified destination path
        # st.write(destination_path)
        # st.write(type(file_1))
        df1 = display_excel_data(file_1)
        df2 = display_excel_data(file_2)
        compareFiles(df1, df2, destination_path)

