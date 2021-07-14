import streamlit as st
import pickle

pickle_in = open("RF_Model_TW.pkl", "rb")
model = pickle.load(pickle_in)



def predict(presentPrice, kmDriven, fuelType_LE, sellerType_LE,transmissionType_LE, noofOwner, noofYear):
    Prediction = model.predict([[presentPrice, kmDriven, fuelType_LE, sellerType_LE,transmissionType_LE, noofOwner, noofYear]])
    return Prediction

def main():
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h1 style="color:white;text-align:center;">Price Prediction </h1>
        </div>
        """
    st.markdown(html_temp, unsafe_allow_html=True)

    presentPrice = st.text_input("ENTER THE PRESENT EX-SHOWROOM PRICE(In Lakhs:Ex:2.31):","")
    kmDriven = st.text_input("ENTER ODOMETER READING:","")
    fuelType = st.selectbox("SELECT FUEL-TYPE: ", ('Petrol', 'Diesel','CNG'))
    if(fuelType== 'Petrol'):
        fuelType_LE = 2
    elif(fuelType=='Diesel'):
        fuelType_LE= 1
    else:
        fuelType_LE = 3
    sellerType = st.selectbox("SELECT SELLER-TYPE: ", ('Dealer', 'Individual'))
    if(sellerType =='Dealer'):
        sellerType_LE=0
    if(sellerType =='Individual'):
        sellerType_LE=1
    transmissionType = st.selectbox("SELECT TRANSMISSION: ", ('Manual', 'Automatic'))
    if(transmissionType =='Manual'):
        transmissionType_LE=1
    if(transmissionType =='Automatic'):
        transmissionType_LE=0
       

    noofOwner = st.number_input("NUMBER OF PAST OWNERS:",step=1)
    noofYear = st.slider("NUMBER OF YEARS", 1, 25)
    result = ""
    if st.button("Predict"):
        result = predict(presentPrice, kmDriven, fuelType_LE, sellerType_LE,transmissionType_LE, noofOwner, noofYear)
        print()
        st.success('This car can be sold for {} Lakhs'.format(result))
        
        

if __name__=='__main__':
    main()