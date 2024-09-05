# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
#api_key="lm-studio"
client = OpenAI(base_url="http://localhost:1234/v1")

# completion = client.chat.completions.create(
#   model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",
#   messages=[
#     {"role": "system", "content": "Always answer in rhymes."},
#     {"role": "user", "content": "Introduce yourself."}
#   ],
#   temperature=0.7,
# )


def convert_lang (input_lang, output_lang, input_code):
    '''
    :param input_lang: language that you want to convert
    :param output_lang: language into with you want to convert
    :param content: provide the code that you want to convert
    '''
    content = input_code
    response = client.chat.completions.create(
    model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",
    messages=[
        {"role": "system", "content": f"You are a {input_lang} to {output_lang} programming language converter you conver {input_lang} language to {output_lang}, // Only respond with code as plain text without code block syntax around it. //Strictly Provide {output_lang} code, no other words"},
        # {"role": "user", "content":"""# Load libraries\nlibrary(dplyr)\nlibrary(ggplot2)\n# Create a data frame\ndata <- data.frame(\n  group = rep(c("A", "B", "C"), each = 10),\n  value = c(rnorm(10, mean = 5), rnorm(10, mean = 7), rnorm(10, mean = 10))\n)\n# Calculate summary statistics\nsummary_data <- data %>%\n  group_by(group) %>%\n  summarise(mean_value = mean(value), sd_value = sd(value))\nprint(summary_data)\n# Plot the data\nggplot(data, aes(x = group, y = value)) +\n  geom_boxplot() +\n  geom_point(aes(color = group)) +\n  theme_minimal()\n"""},
        # {"role": "assistant", "content": "# Load libraries\nimport pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n# Create a data frame\ndata = pd.DataFrame({\n    'group': np.repeat(['A', 'B', 'C'], 10),\n    'value': np.concatenate([np.random.normal(5, 1, 10), np.random.normal(7, 1, 10), np.random.normal(10, 1, 10)])\n})\n# Calculate summary statistics\nsummary_data = data.groupby('group').agg(mean_value=('value', 'mean'), sd_value=('value', 'std')).reset_index()\nprint(summary_data)\n# Plot the data\nplt.figure(figsize=(8, 6))\nsns.boxplot(x='group', y='value', data=data)\nsns.stripplot(x='group', y='value', data=data, color='black', jitter=0.2)\nplt.show()\n"},
        {"role": "user", "content":f"{content}"}
    ]
    )
    message = response.choices[0].message.content

    # response = client.chat.completions.create(
    # model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",
    # messages=[
    #     {"role": "system", "content": f"Only respond with code as plain text without code block syntax around it. //You are a quality checker for {output_lang} code, if you find any missed libraries you add them in the file and correct the code."},
    #     {"role": "user", "content":f"{message}"}
    # ]
    # )
    # message = response.choices[0].message.content
    return message


# print(completion.choices[0].message.content)

# Example: reuse your existing OpenAI setup
from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="QuantFactory/Meta-Llama-3-8B-Instruct-GGUF",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)