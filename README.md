# multiPDF2schema 📄➡️🔢

This project is a Streamlit application that allows users to extract pages from PDF files, convert them to images, and generate JSON schemas based on the content. 🚀

## Features

1. PDF Page Extraction 📄✂️
2. PDF to Image Conversion 📄➡️🖼️
3. JSON Schema Generation 🖼️➡️🔢

## Usage

To get started with multiPDF2schema, simply click the following link:

[https://multipdf2schema.zeabur.app/](https://multipdf2schema.zeabur.app/) 🌐

This will take you to the live application where you can immediately begin using the features without any installation required. 🎉

## Step-by-Step Guide

1. **Upload PDF File** 📤
   - Use the file uploader to select the PDF file you want to process.

2. **Extract PDF Page** 📄✂️
   - Enter the page number you wish to extract.
   - Click the "Extract Page" button.
   - You can download the extracted page if needed.

3. **Convert PDF to Image** 📄➡️🖼️
   - Enter your iLovePDF public key in the provided field.
   - Click the "Convert PDF to Image" button.
   - The extracted page will be converted to a JPG image.

4. **Generate JSON Schema** 🖼️➡️🔢
   - Enter your OpenAI API key in the designated field.
   - Click the "Convert Image to JSON" button.
   - The application will analyze the image and generate a JSON schema representing its content.

5. **Download Results** 💾
   - You can download the extracted PDF page, converted image, or generated JSON schema at each step as needed.

Note: You can perform these steps sequentially or use individual features as required. Make sure to have the necessary API keys for PDF-to-image conversion and JSON schema generation. 🔑

## Local Installation (For Developers) 👨‍💻👩‍💻

If you want to run the application locally or contribute to the project:

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/multiPDF2schema.git
   cd multiPDF2schema
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app locally:
   ```
   streamlit run app.py
   ```

Enjoy using multiPDF2schema! 🎈🎉
