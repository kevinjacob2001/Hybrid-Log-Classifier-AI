# Hybrid Log Classification Framework

## Overview

This project implements a scalable hybrid log classification system that processes high-volume, unstructured log data using a combination of rule-based methods, machine learning, and large language models.

The framework is designed for real-world environments such as retail operations, supply chain systems, and enterprise platforms, where logs originate from multiple heterogeneous sources.

---

## Problem

Operational systems generate large volumes of logs that are:

- Unstructured and inconsistent across sources  
- Difficult to categorize using a single approach  
- Critical for monitoring, debugging, and analytics  

Traditional approaches relying on only rules or machine learning models often fail to scale effectively across diverse log patterns.

---

## Solution

The system adopts a hybrid classification strategy:

1. **Regular Expression (Regex)**  
   Handles predictable and repetitive log patterns with minimal latency and cost  

2. **Sentence Transformer + Logistic Regression**  
   Handles semantically similar and moderately complex logs using embeddings and supervised learning  

3. **LLM (Large Language Model)**  
   Handles ambiguous, complex, or low-data scenarios and acts as a fallback layer  

Logs are dynamically routed to the most appropriate classifier based on source and confidence.

---

## Architecture

![Architecture Diagram](resources/arch.png)

---

## System Workflow

1. Logs are ingested with metadata (`source`, `log_message`)
2. Logs from predefined legacy sources are routed directly to the LLM
3. All other logs follow a staged pipeline:
   - Regex classification (fast path)
   - If no match → ML-based classification
4. If classification confidence is insufficient → LLM fallback
5. Final labels are generated and stored

---

## Setup and Run

```bash
# Navigate to project
cd <your-project-folder>

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Set Groq API key (required for LLM)
export GROQ_API_KEY=your_api_key_here   # Mac/Linux
# set GROQ_API_KEY=your_api_key_here    # Windows

# Ensure input file exists
# resources/test.csv with columns: source,log_message

# Run the project
python main.py

# Output will be saved to:
# resources/output.csv
