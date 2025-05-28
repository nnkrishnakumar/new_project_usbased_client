import replicate
import os

# Set the API token
os.environ["REPLICATE_API_TOKEN"] = ""

# Prepare input
input = {
    "top_p": 1,
    "prompt": "Tell me how to tailor a men's suit so I look fashionable.",
    "temperature": 0.75,
    "max_new_tokens": 800
}

# Run the model
output = replicate.run(
    "meta/llama-2-7b-chat",
    input=input
)

# Print result
print("".join(output))
