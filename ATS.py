import os
import streamlit as st

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from PyPDF2 import PdfReader
from dotenv import load_dotenv


load_dotenv()

llm = ChatOpenAI(temperature = 0.7, openai_api_key = os.getenv("OPENAI_API_KEY"), model_name = "gpt-4") 


def get_doc_with_newlines(pdf_docs):
    text = ""
    pdf_reader = PdfReader(pdf_docs)
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        lines = page_text.split('\n')
        
    return "\n".join(lines)

class EvaluationOutput(BaseModel):
    percentage_matching: float
    missing_keywords: list

    

def ats(job_desc, resume):
    prompt_text = """
    Hey act like a skilled or very experienced ATS(Application Tracking System) with deep understanding of tech fields. Your task is to evaluate
    the resume based on the given job description. You must consider the job market is very competitive, and you should provide
    the best assistance for improving the resumes. Assign the percentage matching based on job description and missing keywords
    with high accuracy.

    Resume: {resume}
    Job Description: {job_desc}

    I want the response as JSON in the following format:
    {{
        "percentage_matching": float,
        "missing_keywords": ["keyword1", "keyword2", ...]
    }}
    """
    
    ats = PromptTemplate(
        input_variables = ["job_desc", "resume"],
        template = prompt_text
    )
    
    output_parser = PydanticOutputParser(pydantic_object=EvaluationOutput)
    
    result = LLMChain(
        llm=llm,
        prompt=ats
    )
    
    raw_output = result.run({"job_desc": job_desc, "resume": resume})
    
    try:
        # Parse the raw output using the Pydantic parser
        parsed_result = output_parser.parse(raw_output)
        return parsed_result
    except Exception as e:
        return f"Error parsing response: {e}\nRaw Output: {raw_output}"

st.set_page_config("ATS")

st.title("Improve your resume")

job_desc = st.text_area("Job Description")

resume = st.file_uploader("Upload Resume", type = "pdf", help = "please upload the pdf")

submit = st.button("Submit")


if submit:
    if resume is not None:
        text = get_doc_with_newlines(resume)
        response = ats(job_desc, text)
        st.write(response)


    
