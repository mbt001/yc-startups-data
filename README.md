# YC Startups Data Extractor

Fetch, analyze, and explore all Y Combinator-funded startups from the past two years (2023–2024) with detailed information including long descriptions, industry, and more.

---

## 📦 What’s in this repo?

- **`YCList.py`** – Python script to fetch YC startups via the public API and save the results as Excel
- **`yc_companies_with_long_desc.xlsx`** – Example data export (run the script to get the latest data!)
- **`requirements.txt`** – Quick install for all Python dependencies

---

## 🛠️ Setup

1. **Clone the repo:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/yc-startups-data.git
    cd yc-startups-data
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(or individually: `pip install requests pandas openpyxl`)*

---

## 🚀 Usage

Run the script to download the latest YC startup data (2023–2024) and save as Excel:

```bash
python yc_companies.py
