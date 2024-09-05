import streamlit as st
import converter as con
import io, os

import streamlit as st
import lmstudio as lms

# Set the title of the app
st.title("Code Converter")
options = ['Locally', 'OpenAI']
api_key = ''

    
selected_model = st.select_slider("Select the Model", options)
if selected_model == 'OpenAI': 
    api_key = st.text_input('Provide your OpenAI API key here', type="password")
# List of programming languages
language_extensions = {
    "Python": "py",
    "JavaScript": "js",
    "Java": "java",
    "C++": "cpp",
    "Ruby": "rb",
    "Go": "go",
    "R": "r",
    "Swift": "swift",
    "Kotlin": "kt",
    "C#": "cs",
    "PHP": "php",
    "TypeScript": "ts",
    "Objective-C": "m",
    "Perl": "pl",
    "Scala": "scala",
    "Rust": "rs",
    "Dart": "dart",
    "Haskell": "hs",
    "Lua": "lua",
    "Matlab": "m",
    "Shell": "sh",
    "SQL": "sql",
    "Visual Basic": "vb",
    "F#": "fs",
    "Elixir": "ex",
    "Erlang": "erl",
    "Groovy": "groovy",
    "Clojure": "clj",
    "Fortran": "f90",
    "COBOL": "cob",
    "Pascal": "pas",
    "Assembly": "asm",
    "VHDL": "vhdl",
    "Verilog": "v",
    "Ada": "ada",
    "APL": "apl",
    "Awk": "awk",
    "Bash": "sh",
    "Batch": "bat",
    "Delphi": "pas",
    "Lisp": "lisp",
    "Logo": "logo",
    "Modula-2": "mod",
    "Prolog": "pl",
    "Scheme": "scm",
    "Smalltalk": "st",
    "Tcl": "tcl",
    "ActionScript": "as",
    "Crystal": "cr",
    "D": "d",
    "Julia": "jl",
    "Nim": "nim",
    "OCaml": "ml",
    "PL/SQL": "pls",
    "PostScript": "ps",
    "Racket": "rkt",
    "REXX": "rexx",
    "SAS": "sas",
    "Simula": "sim",
    "SPARK": "s",
    "SML": "sml",
    "Solidity": "sol",
    "Turing": "t",
    "Zig": "zig",
    "XQuery": "xq",
    "YAML": "yaml",
    "Zsh": "zsh"
}


# Create two side-by-side columns with fixed width and height
col1, col2 = st.columns([1, 1])

with col2:
    st.subheader("Output Language")
    selected_language_output = st.selectbox("Select Language for Output:", list(language_extensions.keys()), key = 'output_language')

# First column: Input text container
with col1:
    st.subheader("Input Language")

    # Language selection for input text
    selected_language_input = st.selectbox("Select Language for Input:", list(language_extensions.keys()), key = 'input_language')

    # File uploader
    uploaded_file = st.file_uploader("Upload a text file", type=None)
    
    if uploaded_file is not None:
        # Read the uploaded file
        input_text = uploaded_file.read().decode("utf-8")
        st.text_area("Uploaded Content:", input_text, height=200)

        # Input for new filename
        new_filename = st.text_input("Enter new filename (without extension):", value=os.path.splitext(uploaded_file.name)[0], key = 'text_input1')
        if not new_filename:
            new_filename = os.path.splitext(uploaded_file.name)[0]
    else:
        # Use text area for manual input
        input_text = st.text_area("Enter your text here:", height=200)
        # # Input for new filename
        new_filename = st.text_input("Enter new filename (without extension):", value='output', key = 'text_input2')
        if not new_filename:
            new_filename = 'output'
    

    # Button to convert text to uppercase, placed below the first container
    if st.button("Convert"):
        if input_text:
            # Convert the input text to uppercase
            # upper_text = input_text.upper()
            if selected_model == 'Locally':
                final_text = lms.convert_lang(selected_language_input, selected_language_output, input_text)
            else:
                final_text = con.convert_lang(selected_language_input, selected_language_output, input_text,api_key)

        else:
            final_text = "No text provided!"

# Second column: Output text container
with col2:
    # st.subheader("Output Language")

    # selected_language_output = st.selectbox("Select Language for Output:", list(language_extensions.keys()), key = 'output_language')

    if 'final_text' in locals():
        # Display the converted text
        st.text_area("Converted text:", final_text, height=200)

        # # Input for new filename-------------------
        # new_filename = st.text_input("Enter new filename (without extension):", value='output', key = 'text_input2')
        # if not new_filename:
        #     new_filename = 'output'
        #-------------------------------------------


        # Create a downloadable file
        def create_downloadable_file(text, filename="output.txt"):
            return io.BytesIO(text.encode())
        
        file_extension = language_extensions.get(selected_language_output, "txt")
        file_name = f"{new_filename}.{file_extension}"

        # Provide download button
        st.download_button(
            label="Download Output File",
            data=create_downloadable_file(final_text),
            file_name=file_name,
            mime="text/plain"
        )
    else:
        st.text_area("Converted Code:", "", height=200)




#------------------------------OLD CODE------------------------------
# # Set the title of the app
# st.title("Text Uppercase Converter")

# # Create two side-by-side columns
# col1, col2 = st.columns(2)

# # First column: Input text container
# with col1:
#     st.subheader("Input Text")
#     input_text = st.text_area("Enter your text here:")

# # Second column: Output text container
# with col2:
#     st.subheader("Uppercase Text")
#     # Placeholder for the output text area to keep it aligned
#     output_text = st.empty()

# # Button to convert text to uppercase
# if st.button("Convert"):
#     if input_text:
#         # Convert the input text to uppercase
#         upper_text = input_text.upper()
#         # Display the uppercase text in the second column
#         output_text.text_area("Converted text:", upper_text, height=200)
#     else:
#         # Display a message if no text was provided
#         output_text.text_area("Converted text:", "No text provided!", height=200)
#------------------------------END OLD CODE------------------------------