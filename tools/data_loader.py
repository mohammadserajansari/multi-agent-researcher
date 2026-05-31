####


import os
import pandas as pd
from bs4 import BeautifulSoup
from pypdf import PdfReader

# Import your central application logger
from core.logger import logger 

class DataLoader:

    # ==========================================
    # TXT Loader
    # ==========================================
    @staticmethod
    def load_txt(file_path: str) -> str:
        logger.info(f"[DataLoader] Reading TXT file: {os.path.basename(file_path)}")
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            text = file.read()
        return text

    # ==========================================
    # HTML Loader
    # ==========================================
    @staticmethod
    def load_html(file_path: str) -> str:
        logger.info(f"[DataLoader] Parsing HTML file: {os.path.basename(file_path)}")
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            html_content = file.read()

        soup = BeautifulSoup(html_content, "html.parser")

        # Remove noisy semantic wrappers
        for tag in soup(["script", "style", "header", "footer", "nav"]):
            tag.decompose()

        text = soup.get_text(separator="\n")
        return text.strip()

    # ==========================================
    # PDF Loader
    # ==========================================
    @staticmethod
    def load_pdf(file_path: str) -> str:
        logger.info(f"[DataLoader] Extracting PDF layout: {os.path.basename(file_path)}")
        reader = PdfReader(file_path)
        text = ""

        for i, page in enumerate(reader.pages):
            extracted_text = page.extract_text()
            if extracted_text and extracted_text.strip():
                text += f"\n--- Page {i+1} ---\n" + extracted_text + "\n"

        return text.strip()

    # ==========================================
    # CSV Loader
    # ==========================================
    @staticmethod
    def load_csv(file_path: str) -> str:
        logger.info(f"[DataLoader] Converting CSV to Markdown matrix: {os.path.basename(file_path)}")
        df = pd.read_csv(file_path)
        return df.to_markdown(index=False)

    # ==========================================
    # Excel Loader
    # ==========================================
    @staticmethod
    def load_excel(file_path: str) -> str:
        logger.info(f"[DataLoader] Converting Excel sheet rows: {os.path.basename(file_path)}")
        df = pd.read_excel(file_path)
        return df.to_markdown(index=False)

    # ==========================================
    # Generic Loader Wrapper
    # ==========================================
    @staticmethod
    def load(file_path: str) -> str:
        if not os.path.exists(file_path):
            logger.error(f"[DataLoader] Target path target missing: {file_path}")
            raise FileNotFoundError(f"Target file does not exist at: {file_path}")

        file_name = os.path.basename(file_path)
        extension = os.path.splitext(file_path)[1].lower()
        extracted_content = ""

        # Router conditions
        if extension == ".txt":
            extracted_content = DataLoader.load_txt(file_path)
        elif extension in [".html", ".htm"]:
            extracted_content = DataLoader.load_html(file_path)
        elif extension == ".pdf":
            extracted_content = DataLoader.load_pdf(file_path)
        elif extension == ".csv":
            extracted_content = DataLoader.load_csv(file_path)
        elif extension in [".xlsx", ".xls"]:
            extracted_content = DataLoader.load_excel(file_path)
        else:
            logger.error(f"[DataLoader] Rejecting execution for unsupported extension: {extension}")
            raise ValueError(f"Unsupported file format: {extension}")

        # Basic text content guard
        if not extracted_content or extracted_content.strip() == "":
            logger.error(f"[DataLoader] Validation failed. Blank extraction string generated for: {file_name}")
            raise ValueError(
                f"Parsing Failure: Extracted text from '{file_name}' is completely empty."
            )

        # =========================================================
        # Centralized Debug Logging Block
        # =========================================================
        logger.info("==================================================")
        logger.info(f" DEBUG PARSE SUMMARY FOR: {file_name}")
        logger.info(f" Total Character Length: {len(extracted_content)}")
        logger.info(f" Preview (First 500 characters):\n")
        logger.info(f"{extracted_content[:500]}")
        if len(extracted_content) > 500:
            logger.info("\n... [Truncated for Log View] ...")
        logger.info("==================================================")

        return extracted_content.strip()