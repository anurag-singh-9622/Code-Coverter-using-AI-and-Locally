import streamlit as st
import converter as con
import io, os

import streamlit as st
import lmstudio as lms

try:

    with st.sidebar:        
        # Set the title of the app
        st.title("Examples")
        
        # Create a selectbox for language selection
        language = st.selectbox("Select a language", ["Python", "JavaScript", "Go", "Ruby", "Java"])
        
        # Create a container for code examples
        with st.container():
            if language == "Python":
                st.title("Python Code Examples")
                st.markdown("## Python Code 1")
                st.code("""
        x = 5
        if x > 10:
            print("x is greater than 10")
        else:
            print("x is less than or equal to 10")
        """, language="python")
                st.markdown("## Python Code 2")
                st.code("""
        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            print(fruit)
        """, language="python")
                st.markdown("## Python Code 3")
                st.code("""
        def greet(name):
            print("Hello, " + name)
        greet("John")
        """, language="python")
                st.markdown("## Python Code 4")
                st.code("""
        x = 5
        y = 3
        print(x + y)
        """, language="python")
                st.markdown("## Python Code 5")
                st.code("""
        numbers = [1, 2, 3, 4, 5]
        print(sum(numbers))
        """, language="python")
        
            elif language == "JavaScript":
                st.title("JavaScript Code Examples")
                st.markdown("## JavaScript Code 1")
                st.code("""
        let x = 5;
        if (x > 10) {
            console.log("x is greater than 10");
        } else {
            console.log("x is less than or equal to 10");
        }
        """, language="javascript")
                st.markdown("## JavaScript Code 2")
                st.code("""
        let fruits = ["apple", "banana", "cherry"];
        fruits.forEach(fruit => console.log(fruit));
        """, language="javascript")
                st.markdown("## JavaScript Code 3")
                st.code("""
        function greet(name) {
            console.log("Hello, " + name);
        }
        greet("John");
        """, language="javascript")
                st.markdown("## JavaScript Code 4")
                st.code("""
        let x = 5;
        let y = 3;
        console.log(x + y);
        """, language="javascript")
                st.markdown("## JavaScript Code 5")
                st.code("""
        let numbers = [1, 2, 3, 4, 5];
        console.log(numbers.reduce((a, b) => a + b, 0));
        """, language="javascript")
        
            elif language == "Go":
                st.title("Go Code Examples")
                st.markdown("## Go Code 1")
                st.code("""
        x := 5
        if x > 10 {
            fmt.Println("x is greater than 10")
        } else {
            fmt.Println("x is less than or equal to 10")
        }
        """, language="go")
                st.markdown("## Go Code 2")
                st.code("""
        fruits := []string{"apple", "banana", "cherry"}
        for _, fruit := range fruits {
            fmt.Println(fruit)
        }
        """, language="go")
                st.markdown("## Go Code 3")
                st.code("""
        package main
        import "fmt"
        func greet(name string) {
            fmt.Println("Hello, " + name)
        }
        func main() {
            greet("John")
        }
        """, language="go")
                st.markdown("## Go Code 4")
                st.code("""
        x := 5
        y := 3
        fmt.Println(x + y)
        """, language="go")
                st.markdown("## Go Code 5")
                st.code("""
        numbers := []int{1, 2, 3, 4, 5}
        sum := 0
        for _, num := range numbers {
            sum += num
        }
        fmt.Println(sum)
        """, language="go")
        
            elif language == "Ruby":
                st.title("Ruby Code Examples")
                st.markdown("## Ruby Code 1")
                st.code("""
        puts "Hello, World!"
        """, language="ruby")
                st.markdown("## Ruby Code 2")
                st.code("""
        x = 5
        y = 3
        puts x + y
        """, language="ruby")
                st.markdown("## Ruby Code 3")
                st.code("""
        fruits = ["apple", "banana", "cherry"]
        fruits.each do |fruit|
            puts fruit
        end
        """, language="ruby")
                st.markdown("## Ruby Code 4")
                st.code("""
        def greet(name)
            puts "Hello, #{name}"
        end
        greet("John")
        """, language="ruby")
                st.markdown("## Ruby Code 5")
                st.code("""
        numbers = [1, 2, 3, 4, 5]
        puts numbers.inject(:+)
        """, language="ruby")
            elif language == "Java":
                st.title("Java Code Examples")
                st.markdown("## Java Code 1")
                st.code("""
        System.out.println("Hello, World!");
        """, language="java")
                st.markdown("## Java Code 2")
                st.code("""
        int x = 5;
        int y = 3;
        System.out.println(x + y);
        """, language="java")
                st.markdown("## Java Code 3")
                st.code("""
        String[] fruits = {"apple", "banana", "cherry"};
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
        """, language="java")
                st.markdown("## Java Code 4")
                st.code("""
        public static void greet(String name) {
            System.out.println("Hello, " + name);
        }
        greet("John");
        """, language="java")
                st.markdown("## Java Code 5")
                st.code("""
        int[] numbers = {1, 2, 3, 4, 5};
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        System.out.println(sum);
        """, language="java")
    
    
# Set the title of the app
    st.title("Code Converter")
    options = ['Locally', 'OpenAI']
    api_key = ''

        
    selected_model = st.select_slider("Select the Model", options)
    if selected_model == 'OpenAI': 
        st.info('To use OpenAI option you have to provide your api key. You can get your API key from https://beta.openai.com/account/api-keys')
        st.info('You could message me on linkdin personally and I could provide you one time api key to use, linkedin https://www.linkedin.com/in/anuragsingh9622/')
        api_key = st.text_input('Provide your OpenAI API key here', type="password")
    if selected_model == 'Locally': 
        st.warning('You are using Locally model, Use it when you have set up the local server on your machine go to docs to set it up. Link https://lmstudio.ai/docs/', icon="⚠️")
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
        
        try:
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
        except Exception as e:
            st.error(f"An unexpected occurred: {str(e)}")

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
            def create_downloadable_file(text, filename="output.txt") -> io.BytesIO:
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

except Exception as e:
      st.error(f"An unexpected error occurred: {e}")


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