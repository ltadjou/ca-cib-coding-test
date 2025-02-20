
import  re  
from pydantic import BaseModel

field_mappings = {
        "Counterparty": r"Party A \| ([^\n]+)",  # Extract Party A
        "Initial_Valuation_Date": r"Initial Valuation Date \| ([^\n]+)",
        "Notional": r"Notional Amount \(N\) \| ([^\n]+)",
        "Valuation_Date": r"Valuation Date \| ([^\n]+)",
        "Maturity": r"Termination Date \| ([^\n]+)",
        "Underlying": r"Underlying \| ([^\n]+)",
        "Coupon": r"Coupon \(C\) \| ([^\n]+)",
        "Barrier": r"Barrier \(B\) \| ([^\n]+)",
        "Calender": r"Business Day \| ([^\n]+)",
}

data_to_extract = ["Counterparty", "Initial_Valuation_Date", "Notional", "Valuation_Date", "Maturity", "Underlying", "Coupon", "Barrier", "Calendar"]

class DocContentProssecing:

    def  extract_information(file_content: str):
        extracted_data = {}
        # Extract values using regex rules
        for field, pattern in field_mappings.items():
            match = re.search(pattern, file_content)
            extracted_data[field] = match.group(1) if match else "N/A"  # Default to "N/A" if no match found

        return extracted_data

class RequestData(BaseModel):
    content: str

class CustomResponse(BaseModel):
    message: str
    data: dict