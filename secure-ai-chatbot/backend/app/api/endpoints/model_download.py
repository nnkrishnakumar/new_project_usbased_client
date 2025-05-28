# Load model directly
from transformers import AutoProcessor, AutoModelForImageTextToText

processor = AutoProcessor.from_pretrained("google/medgemma-4b-pt")
model = AutoModelForImageTextToText.from_pretrained("google/medgemma-4b-pt")