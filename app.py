import streamlit as st
import PyPDF2
import io
from pylovepdf.tools.pdftojpg import PdfToJpg
import tempfile
import os
import json
import base64
import openai

def extract_page_from_pdf(input_pdf, page_number):
    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(input_pdf)
    
    # Check if the specified page number is valid
    if page_number < 1 or page_number > len(pdf_reader.pages):
        raise ValueError("Invalid page number")
    
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()
    
    # Add the specified page to the writer
    pdf_writer.add_page(pdf_reader.pages[page_number - 1])
    
    # Write the output to a BytesIO object
    output = io.BytesIO()
    pdf_writer.write(output)
    output.seek(0)
    return output

def pdf_extractor():
    st.header("PDF Page Extractor")

    # Use session state to remember the uploaded PDF file
    if 'pdf_file' not in st.session_state:
        st.session_state.pdf_file = None

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", key="pdf_uploader")
    
    # Update session state
    if uploaded_file is not None:
        st.session_state.pdf_file = uploaded_file

    if st.session_state.pdf_file is not None:
        # Display the number of pages in the uploaded PDF
        pdf_reader = PyPDF2.PdfReader(st.session_state.pdf_file)
        num_pages = len(pdf_reader.pages)
        st.write(f"Total pages in the PDF: {num_pages}")

        # Page number input
        page_number = st.number_input("Enter the page number to extract", min_value=1, max_value=num_pages, value=1)

        if st.button("Extract Page"):
            try:
                output_pdf = extract_page_from_pdf(st.session_state.pdf_file, page_number)
                st.success(f"Page {page_number} has been extracted successfully!")
                
                # Store the extracted page in session state for the next feature
                st.session_state.extracted_pdf = output_pdf
                
                # Provide download button for the extracted page
                st.download_button(
                    label="Download Extracted Page",
                    data=output_pdf,
                    file_name=f"extracted_page_{page_number}.pdf",
                    mime="application/pdf"
                )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

def pdf_to_image():
    st.header("PDF to Image Converter")

    # Use session state to remember the ilovepdf_public_key
    if 'ilovepdf_public_key' not in st.session_state:
        st.session_state.ilovepdf_public_key = ''

    ilovepdf_public_key = st.text_input("Enter your iLovePDF public key:", 
                                        type="password", 
                                        value=st.session_state.ilovepdf_public_key)
    
    # Update session state
    st.session_state.ilovepdf_public_key = ilovepdf_public_key

    if not st.session_state.ilovepdf_public_key:
        st.warning("Please enter your iLovePDF public key to use this feature.")
        return

    # Check if there's an extracted PDF from the previous feature
    if 'extracted_pdf' in st.session_state and st.session_state.extracted_pdf is not None:
        st.write("Using the extracted PDF from the previous step.")
        pdf_file = st.session_state.extracted_pdf
    else:
        pdf_file = st.file_uploader("Choose a PDF file", type="pdf")

    if pdf_file is not None:
        if st.button("Convert PDF to Image"):
            try:
                # Create a temporary directory to store the files
                with tempfile.TemporaryDirectory() as temp_dir:
                    # Save the PDF file to the temporary directory
                    temp_input_path = os.path.join(temp_dir, "input.pdf")
                    with open(temp_input_path, "wb") as f:
                        f.write(pdf_file.getvalue())

                    # Initialize the PdfToJpg tool
                    t = PdfToJpg(st.session_state.ilovepdf_public_key, verify_ssl=True, proxies=None)
                    
                    # Add the file and set the output folder
                    t.add_file(temp_input_path)
                    t.set_output_folder(temp_dir)
                    
                    # Execute the conversion
                    t.execute()
                    
                    # Download the converted files
                    t.download()
                    
                    # Delete the task to free up resources
                    t.delete_current_task()

                    # Find the converted image files
                    converted_files = [f for f in os.listdir(temp_dir) if f.endswith('.jpg')]

                    if converted_files:
                        st.success("PDF has been converted to image(s) successfully!")
                        
                        # Store the first converted image in session state for the next feature
                        with open(os.path.join(temp_dir, converted_files[0]), "rb") as file:
                            st.session_state.converted_image = file.read()
                        
                        # Provide download buttons for each converted image
                        for i, file_name in enumerate(converted_files, 1):
                            with open(os.path.join(temp_dir, file_name), "rb") as file:
                                st.download_button(
                                    label=f"Download Image {i}",
                                    data=file,
                                    file_name=file_name,
                                    mime="image/jpeg"
                                )
                    else:
                        st.error("No images were generated from the PDF.")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

def image_to_schema():
    st.header("Image to JSON Converter")

    # Use session state to remember the OpenAI API key
    if 'openai_api_key' not in st.session_state:
        st.session_state.openai_api_key = ''

    openai_api_key = st.text_input("Enter your OpenAI API key:", 
                                   type="password", 
                                   value=st.session_state.openai_api_key)

    # Update session state
    st.session_state.openai_api_key = openai_api_key

    if not openai_api_key:
        st.warning("Please enter your OpenAI API key to use this feature.")
        return

    # Check if there's a converted image from the previous feature
    if 'converted_image' in st.session_state and st.session_state.converted_image is not None:
        st.write("Using the converted image from the previous step.")
        image_file = st.session_state.converted_image
    else:
        uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
        if uploaded_file is not None:
            image_file = uploaded_file.getvalue()
        else:
            image_file = None

    if image_file is not None:
        if st.button("Convert Image to JSON"):
            try:
                # Initialize OpenAI client
                client = openai.Client(api_key=st.session_state.openai_api_key)

                # Encode the image file
                image_base64 = base64.b64encode(image_file).decode('utf-8')

                response = client.chat.completions.create(
                    model='gpt-4o-mini',
                    response_format={"type": "json_object"},
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "Analyze this image and provide a simple JSON representation of its content. Include all relevant information you can extract from the image."},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": f"data:image/jpeg;base64,{image_base64}"
                                    }
                                }
                            ]
                        }
                    ],
                    max_tokens=1000,
                )

                content = response.choices[0].message.content
                if content:
                    json_data = json.loads(content)
                    st.success("Image has been converted to JSON successfully!")
                    
                    # Display the JSON data
                    st.json(json_data)
                    
                    # Provide download button for the JSON file
                    json_string = json.dumps(json_data, indent=4)
                    st.download_button(
                        label="Download JSON",
                        data=json_string,
                        file_name="image_content.json",
                        mime="application/json"
                    )
                else:
                    st.error("No content received in the response")

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

def main():
    st.title("PDF and Image Processing App")

    # Create a sidebar for navigation
    st.sidebar.title("Features")
    
    # Use session state to remember the selected features
    if 'extract_pdf' not in st.session_state:
        st.session_state.extract_pdf = False
    if 'pdf_to_image' not in st.session_state:
        st.session_state.pdf_to_image = False
    if 'image_to_json' not in st.session_state:
        st.session_state.image_to_json = False

    # Create checkboxes for each feature
    st.session_state.extract_pdf = st.sidebar.checkbox("Extract PDF Page", value=st.session_state.extract_pdf)
    st.session_state.pdf_to_image = st.sidebar.checkbox("PDF to Image", value=st.session_state.pdf_to_image)
    st.session_state.image_to_json = st.sidebar.checkbox("Image to JSON", value=st.session_state.image_to_json)

    # Display the selected features
    if st.session_state.extract_pdf:
        pdf_extractor()
    if st.session_state.pdf_to_image:
        pdf_to_image()
    if st.session_state.image_to_json:
        image_to_schema()

if __name__ == "__main__":
    main()
