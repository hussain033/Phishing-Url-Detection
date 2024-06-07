from featureExtractor import featureExtraction
from pycaret.classification import load_model, predict_model

model = load_model('phishingdetection')


def predict(url):
  data = featureExtraction(url)
  result = predict_model(model, data = data)
  return result['prediction_label'][0]

if __name__ == "__main__":
    if(len(sys.argv) != 2):
      print("Usage: python3 app.py URL")
    else:
      url = sys.argv[1]
      print("The URL is predicted as"+predict(url))
