import  qrcode
import streamlit as st
from io import BytesIO

# Get input as a text or URL
st.title("**QR Code Generator**")
input_text =  st.text_input("Enter a Text or URL: ")

if input_text:
    # Generate a QR
    QR = qrcode.make(input_text)

    # Save the QR code to BytesIO buffer
    buffer = BytesIO()
    QR.save(buffer, "PNG")
    buffer.seek(0)  # Reset buffer position to the beginning

    # Display the QR code
    st.image(buffer, caption="QR Code generated successfully!")

    # Download button for the QR
    if input_text:
        st.download_button(
            label="Download this QR code",
            data = buffer.getvalue(),
            file_name="V-QRcode.png",
            mime="image/png"
        )