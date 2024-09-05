# 🌟 **Code to Code Converter** 🌟

The **Code to Code Converter** is a tool that translates code from one programming language to another using powerful language models. You can use the OpenAI API for language model processing or run it locally via the **LMStudio** application.

---

## 🎯 **Features**

- 🔄 Convert code between multiple programming languages.
- 🌍 Supports a wide range of programming languages.
- 🔑 Option to use OpenAI API or a locally hosted LLM server.
- ⚡ Easy to set up and use.

---

## 🚀 **Getting Started**

### 🛠 **Prerequisites**

To use this tool, you need:

1. An OpenAI API key (if you choose to use OpenAI's models).
2. Alternatively, you can set up a locally hosted LLM server using the **LMStudio** application.

### 🔧 **Setup**

#### **Option 1: Using OpenAI API**

1. **Clone this repository:**
    ```bash
    git clone https://github.com/your-username/code-to-code-converter.git
    cd code-to-code-converter
    ```

2. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set your OpenAI API key as an environment variable:**
    ```bash
    export OPENAI_API_KEY='your_openai_api_key'
    ```

4. **Run the application:**
    ```bash
    python main.py
    ```

#### **Option 2: Using LMStudio for Local LLM Server**

1. Download and install the **LMStudio** application from [LMStudio's official website](https://lmstudio.ai/).

2. Set up the LLM server following the instructions provided by **LMStudio**.

3. Update the configuration file (`config.json`) in the repository to point to your locally hosted LLM server:
    ```json
    {
        "llm_server": "http://localhost:5000"
    }
    ```

4. **Run the application:**
    ```bash
    python main.py
    ```

---

## 📚 **Usage**

- The tool provides a simple command-line interface to convert code. You can specify the source language, target language, and the code you want to convert.
  
  **Example:**
  ```bash
  python main.py --source_language "Python" --target_language "JavaScript" --code "print('Hello World')"
  ```

- The output will display the converted code in the target language.

---

## 🌐 **Supported Languages**

The **Code to Code Converter** currently supports the following programming languages:

- ✅ Python
- ✅ JavaScript
- ✅ C++
- ✅ Java
- ✅ Ruby
- ✅ PHP
- ✅ Go
- 🚀 And more!

---

## 🤝 **Contributing**

Contributions are welcome! Please feel free to submit a pull request or open an issue.

---

## 📄 **License**

This project is licensed under the **MIT License**.



### 🎨 **Feel free to customize the content further to suit your specific requirements!**

---

This version uses emojis and Markdown for a more visually engaging README while adhering to GitHub's formatting rules.
