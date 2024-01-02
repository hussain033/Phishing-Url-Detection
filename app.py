import gradio as gr
from featureExtractor import featureExtraction
from pycaret.classification import load_model, predict_model

model = load_model('phishingdetection')


def predict(url):
  data = featureExtraction(url)
  result = predict_model(model, data = data)
  return result['prediction_label'][0]

app = gr.Interface(fn=predict,
             inputs="text",
             outputs="text",
            )
if __name__ == "__main__":
    app.launch(debug = True)
