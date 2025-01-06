import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(layout='wide')
#################
def plot_feature_by_msn(temp, msn_list, feature):
    mean_df=pd.read_excel("mean.xlsx")
    sum_df=pd.read_excel("sum.xlsx")
    if temp=='mean':
        df=mean_df
    else:
        df=sum_df
    # """
    # Function to plot a specific feature against 'ts' for multiple 'msn' values.
    # Parameters:
    # df (DataFrame): The dataframe containing the data.
    # msn_list (list): A list of msn values to filter by.
    # feature (str): The feature to plot (e.g., 'v_ave', 'i_ave', etc.).
    # """
    # Ensure 'ts' is in datetime format
    df['ts'] = pd.to_datetime(df['ts'])
    # Filter the dataframe for the selected msn values
    df_filtered = df[df['msn'].isin(msn_list)]
    # Check if the feature exists in the dataframe
    if feature not in df_filtered.columns:
        print(f"Error: Feature '{feature}' not found in the dataframe.")
        return
    # Plotting the chosen feature against 'ts'
    fig, ax = plt.subplots(figsize=(10, 6))
    # Plot each msn's data
    for msn in msn_list:
        df_msn = df_filtered[df_filtered['msn'] == msn]
        # Check if there's data for the current msn
        if not df_msn.empty:
            ax.plot(df_msn['ts'], df_msn[feature], label=f'{msn} - {feature}', marker='o')
        else:
            print(f"Warning: No data found for msn {msn}")
    ax.set_title(f'{feature} for msn(s) {", ".join(msn_list)}')
    ax.set_xlabel('Date')
    ax.set_ylabel(feature)
    ax.grid(True)
    plt.xticks(rotation=45)  # Rotate the x-axis labels for better visibility
    plt.tight_layout()
    plt.legend()
    st.pyplot(fig) 
###################
col1,col2=st.columns([3, 5]) 

with col1: 
    col11,col22=st.columns([1,1])
    # st.subheader('Please Select DataFrame Type(mean or sum)')
    # option2 = st.selectbox('',('mean','sum'))
    with col11:
        
        
        
        st.write('Please Select Msn Number')
        option_check1=st.checkbox('SM11065227')
        option_check2=st.checkbox('SM11066826')
        option_check3=st.checkbox('SM11101308')
        option_check4=st.checkbox('SM11150862')
        option_check5=st.checkbox('SM11150914')
        option_check6=st.checkbox('SML3000263')
    ############################################
    with col22:
        st.write('Please Select DataFrame Type(mean or sum)')
        option2 = st.selectbox('',('mean','sum'))
        st.write(f"you have selected : {option2}")
        st.write('Please Select Parameter')
        option3 = st.selectbox('',('v_ave','i_ave','wh_imp','vah_imp'))
        st.write(f"you have selected: {option3}")
        checkbox_labels = [
            'SM11065227', 
            'SM11066826', 
            'SM11101308', 
            'SM11150862', 
            'SM11150914', 
            'SML3000263'
        ]

        selected_msn = []
        if option_check1:
            selected_msn.append('SM11065227')
        if option_check2:
            selected_msn.append('SM11066826')
        if option_check3:
            selected_msn.append('SM11101308')
        if option_check4:
            selected_msn.append('SM11150862')
        if option_check5:
            selected_msn.append('SM11150914')
        if option_check6:
            selected_msn.append('SML3000263')
######################################################################
with col2:
    if len(selected_msn)==0:
        st.write("No MSN selected ,please select from above list")
    else:
        st.write(f"Selected MSN list:{selected_msn}")
        if option2=='mean':
            st.write('THIS IS MEAN AGGREGATED GRAPH')
            plot_feature_by_msn(option2,selected_msn,option3)
        else:
            st.write("THIS IS SUM AGGEGRATED GRAPH ")
            plot_feature_by_msn(option2,selected_msn,option3)
