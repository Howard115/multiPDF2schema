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

## Getting API Keys

To use all features of multiPDF2schema, you'll need to obtain two API keys:

### ILovePDF Public Key

1. Go to [https://www.iloveapi.com/user/projects](https://www.iloveapi.com/user/projects)
2. Sign up for a free account or log in if you already have one.
3. Once logged in, you'll see your projects listed.
4. If you don't have a project yet, create a new one.
5. Your public key will be displayed in the project details.

### OpenAI API Key

1. Visit [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. Sign up for an account or log in to your existing account.
3. On this page, you'll see your existing API keys or can create a new one.
4. Click on "Create new secret key" to generate a new API key.
5. Make sure to copy the key immediately and store it securely, as you won't be able to see it again.

Remember to keep these API keys secure and never share them publicly. 🔐

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
