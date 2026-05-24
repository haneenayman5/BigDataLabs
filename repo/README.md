# 🐘 Big Data Labs — Haneen Ayman

Hands-on labs covering core Big Data technologies using **Hadoop**, **HBase**, and **HDFS**, completed as part of a Big Data course.

---

## 📁 Repository Structure

```
├── HBase/
│   ├── commands/
│   │   ├── lab1_basics.md        # Create, Insert, Scan, Get
│   │   └── lab2_advanced.md      # Filters, Versioning, Alter, Lifecycle
│   └── exercises/
│       ├── beginner_answers.md   # Q1–Q8 beginner exercises
│       └── intermediate_answers.md # Q1–Q8 intermediate exercises
│
├── MapReduce/
│   ├── lab1/   → Word Count (Fruits dataset)
│   ├── lab2/   → Word Count (Shakespeare dataset)
│   ├── lab3/   → Apache Log IP Counter
│   └── lab4/   → City Score Statistics (Mean & Std)
│
├── HDFS-Control-Panel/
│   ├── app.py          # Flask web app entry point
│   ├── hdfs_runner.py  # Command execution engine
│   └── ui.py           # Terminal-style HTML UI
│
└── README.md
```

---

## 🧪 Labs Overview

### 🗄️ HBase
NoSQL wide-column store on top of Hadoop. Labs cover:
- Creating tables and column families
- Inserting, scanning, and getting data
- Filters: `ValueFilter`, `SingleColumnValueFilter`, `PrefixFilter`, `RowFilter`
- Versioning, `alter`, table lifecycle (`disable` / `drop`)

📄 Full lab document: [`HBase/HBase_Student_Lab.docx`](HBase/HBase_Student_Lab.docx)  
🖼️ Lab screenshot: [`HBase/screenshots/hbase_lab2.jpeg`](HBase/screenshots/hbase_lab2.jpeg)

### ⚙️ MapReduce
Distributed processing framework. Four labs of increasing complexity:

| Lab | Dataset | Task |
|-----|---------|------|
| Lab 1 | Fruits | Basic word count |
| Lab 2 | Shakespeare | Word count on large text |
| Lab 3 | Apache access log | Count requests per IP |
| Lab 4 | City scores | Compute mean & std per city |

### 🖥️ HDFS Control Panel
A browser-based GUI built with Flask to interact with HDFS without using the terminal directly. Features: start/stop DFS & YARN, browse paths, list files, copy/move/delete, create directories.

---

## 🛠️ Technologies Used

- Apache Hadoop (HDFS + MapReduce + YARN)
- Apache HBase
- Python 3 (MapReduce streaming)
- Flask (HDFS Control Panel)
- VMware Workstation (lab environment)
