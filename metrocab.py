import streamlit as st
st.title("METRO+CAB BOOKING")
#metro station list
stations=[
    "Select",
    "JNTUH",
    "MYP",
    "Ameerpet",
    "LBNagar",
]
from_station=st.selectbox("From Station",stations)
to_station=st.selectbox("To Station",stations)
tickets=st.number_input("Number of Tickets",min_value=1,value=1)
need_cab=st.radio("Do You Need a Cab ?",
                  ["Yes","No"],index=None)
cab_destination=""
cab_fare=0
if need_cab=="Yes":
    cab_destination=st.text_input("Destination")
    cab_fare=130
if st.button("BOOK"):
    if from_station==to_station:
        st.error("both stations are same!")
    else:
        metro_fare=30*tickets
        total=metro_fare+cab_fare
        st.success("Booking Done!")
        st.subheader("***Bill Details***")
        st.write(f"From station:{from_station}")
        st.write(f"To station:{to_station}")
        st.write(f"Tickets:{tickets}")
        st.write(f"metro:{metro_fare}")
        if need_cab=="Yes":
            st.write(f"Cab From:{to_station}")
            st.write(f"to:{cab_destination}")
            st.write(f"cab bill:{cab_fare}")
            st.write(f"---total----{total}")
