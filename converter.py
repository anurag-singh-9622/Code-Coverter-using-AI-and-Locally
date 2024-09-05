from openai import OpenAI
from dotenv import load_dotenv
import os

# load environment variables from .env file
load_dotenv()

# get the environment variable
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
# client = OpenAI()

def convert_lang (input_lang, output_lang, input_code, api_key):
    '''
    :param input_lang: language that you want to convert
    :param output_lang: language into with you want to convert
    :param content: provide the code that you want to convert
    :param api_key: OpenAI API Key

    '''
    client = OpenAI(api_key=api_key)
    content = input_code
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"You are a {input_lang} to {output_lang} programming language converter you conver {input_lang} language to {output_lang}, Only respond with code as plain text without code block syntax around it, //Strictly Provide {output_lang} code, no other words"},
        # {"role": "user", "content":"""# Load libraries\nlibrary(dplyr)\nlibrary(ggplot2)\n# Create a data frame\ndata <- data.frame(\n  group = rep(c("A", "B", "C"), each = 10),\n  value = c(rnorm(10, mean = 5), rnorm(10, mean = 7), rnorm(10, mean = 10))\n)\n# Calculate summary statistics\nsummary_data <- data %>%\n  group_by(group) %>%\n  summarise(mean_value = mean(value), sd_value = sd(value))\nprint(summary_data)\n# Plot the data\nggplot(data, aes(x = group, y = value)) +\n  geom_boxplot() +\n  geom_point(aes(color = group)) +\n  theme_minimal()\n"""},
        # {"role": "assistant", "content": "# Load libraries\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n# Create a data frame\ndata = pd.DataFrame({\n    'group': np.repeat(['A', 'B', 'C'], 10),\n    'value': np.concatenate([np.random.normal(5, 1, 10), np.random.normal(7, 1, 10), np.random.normal(10, 1, 10)])\n})\n# Calculate summary statistics\nsummary_data = data.groupby('group').agg(mean_value=('value', 'mean'), sd_value=('value', 'std')).reset_index()\nprint(summary_data)\n# Plot the data\nplt.figure(figsize=(8, 6))\nsns.boxplot(x='group', y='value', data=data)\nsns.stripplot(x='group', y='value', data=data, color='black', jitter=0.2)\nplt.show()\n"},
        {"role": "user", "content":f"{content}"}
    ]
    )
    message = response.choices[0].message.content

    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"Only respond with code as plain text without code block syntax around it, // You are a quality checker for {output_lang} code, if you find any missed libraries you add them in the file and correct the code."},
        {"role": "user", "content":f"{message}"}
    ]
    )
    message = response.choices[0].message.content
    return message


def converter(input_lang, output_lang, input_file , output_file):
    '''
    :param input_lang: language that you want to convert
    :param output_lang: language into with you want to convert
    :param input_file: input_lang code file, provide with extention eg: main.py, final.r
    :param output_file: output_lang code file, provide with extention eg: main.py, final.r
    '''
    try:
        # Open the input file in read mode and output file in write mode
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            # Read the content of the input file
            content = infile.read()

            response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a {input_lang} to {output_lang} programming language converter you conver {input_lang} language to {output_lang}, Strictly Provide {output_lang} code, no other words"},
                # {"role": "user", "content":"""# Load libraries\nlibrary(dplyr)\nlibrary(ggplot2)\n# Create a data frame\ndata <- data.frame(\n  group = rep(c("A", "B", "C"), each = 10),\n  value = c(rnorm(10, mean = 5), rnorm(10, mean = 7), rnorm(10, mean = 10))\n)\n# Calculate summary statistics\nsummary_data <- data %>%\n  group_by(group) %>%\n  summarise(mean_value = mean(value), sd_value = sd(value))\nprint(summary_data)\n# Plot the data\nggplot(data, aes(x = group, y = value)) +\n  geom_boxplot() +\n  geom_point(aes(color = group)) +\n  theme_minimal()\n"""},
                # {"role": "assistant", "content": "# Load libraries\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n# Create a data frame\ndata = pd.DataFrame({\n    'group': np.repeat(['A', 'B', 'C'], 10),\n    'value': np.concatenate([np.random.normal(5, 1, 10), np.random.normal(7, 1, 10), np.random.normal(10, 1, 10)])\n})\n# Calculate summary statistics\nsummary_data = data.groupby('group').agg(mean_value=('value', 'mean'), sd_value=('value', 'std')).reset_index()\nprint(summary_data)\n# Plot the data\nplt.figure(figsize=(8, 6))\nsns.boxplot(x='group', y='value', data=data)\nsns.stripplot(x='group', y='value', data=data, color='black', jitter=0.2)\nplt.show()\n"},
                {"role": "user", "content":f"{content}"}
            ]
            )
            message = response.choices[0].message.content

            response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": f"You are a quality checker for {output_lang} code, if you find any missed libraries you add them in the file and correct the code. --> Only respond with code as plain text without code block syntax around it"},
                {"role": "user", "content":f"{message}"}
            ]
            )
            message = response.choices[0].message.content
            # Write the content to the output file
            outfile.write(message)
        print(f"{input_lang} file {input_file} Converted to {output_lang} file {output_file}")
    except FileNotFoundError:
        print(f"The file {input_file} does not exist.")
    except IOError:
        print("An error occurred while reading or writing the file.")

# Example usage
# input_file = 'input.txt'  # Replace with your input file name
# output_file = 'output.txt'  # Replace with your output file name

# converter('R', 'Python', 'calculate.r', 'final.py')


# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
#   ]
# )

# message = response.choices[0].message.content



# print(message)
# print(response.usage.total_tokens)


