import streamlit as st
from api import dat
from datesetter import date_formatter



date = st.date_input("select")
new_date = date_formatter(date)
new_date
st.write('Enter your pin code')
pin = st.text_input('Enter Here')
data =""
if (st.button('Search')==True):
    
    data=dat(pin,new_date)
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")



try :
    
    for centre in data['centers']:
        st.write("Centre Name : ",centre['name'])
        st.write("Address : ",centre['address']) 
        st.write("Block Name",centre['block_name'])
        st.write("From : ",centre['from'])
        st.write("To : ",centre['to']) 
        st.write("Free/Paid : ",centre['fee_type'])
        for session in centre['sessions']:
            if session['date'] != new_date:
                break
            st.write("Date : ",session['date'])
            st.write("Available Doses",session['available_capacity'])
            st.write("Minimum Age Limit : ",session['min_age_limit'])
            st.write("Vaccine Name : ",session['vaccine'])
            st.write("Slots : ")
            for slot in session['slots']:
                st.write(slot)
            st.write("Available capacity of First dose : ",session['available_capacity_dose1'])
            st.write("Available capacity of Second dose : ",session['available_capacity_dose2'])
        
        for obj in centre['vaccine_fees']:
            try:
                st.write("Vaccine Name: ",obj['vaccine'])
                st.write("Vaccine Fee : ",obj['fee'])
            except:
                " "
        
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")

except:
    " "        
        