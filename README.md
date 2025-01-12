# Advanced Resume Analyzer

## Overview
The Advanced Resume Analyzer is a Streamlit application designed to help job seekers improve their resumes by evaluating them against specific job descriptions. This tool uses OpenAI's GPT-4 model to simulate an Application Tracking System (ATS) with deep knowledge of technology fields. It assesses how well a resume matches a job description and provides actionable feedback to enhance resume effectiveness in competitive job markets.

## Features
- **PDF Resume Upload**: Allows users to upload their resume in PDF format.
- **Resume Evaluation**: Compares uploaded resumes against provided job descriptions to determine fit and suggest improvements.
- **Detailed Feedback**: Offers percentage match scores and identifies missing keywords that are critical for the job application.

## How It Works
### Setup and Configuration
The application utilizes the LangChain library integrated with OpenAI's GPT-4 model to process and evaluate text data. It is built with Streamlit, making it user-friendly and easy to interact with.

### Detailed Functionality
- **PDF Processing**: The app reads PDF resumes using `PyPDF2`, extracting text while preserving the formatting such as newlines.
- **ATS Simulation**: The core functionality is a simulated ATS, implemented through a custom prompt template that instructs the GPT-4 model to analyze the resume text in comparison with the job description.
- **Output Parsing**: Uses a Pydantic model to structure the output data into a JSON format that includes the percentage match and missing keywords, ensuring the output is standardized and easy to understand.

### Streamlit Interface
The interface consists of:
- A text area for inputting the job description.
- A file uploader for the resume in PDF format.
- A submit button that triggers the evaluation process.
- Display area for results that shows the percentage match and missing keywords after processing.

## Installation
To run this application, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
