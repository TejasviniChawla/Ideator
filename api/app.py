from flask import Flask, render_template, url_for, request
from api.example import add2
from api.ml import add

app= Flask(__name__)

@app.route('/')
def index():

    Heading = request.args.get("Heading")
    desc = request.args.get("desc")
    return render_template("index.html", Heading= Heading, desc= desc)

@app.route('/summary')
def summary():
   
    Heading = request.args.get("Heading")
    head= Heading
    desc = request.args.get("desc")
    # ml_pipeline(head, name)
    # descrip=['python based project on image caption generator - learn to build a working model of image caption generator by implementing cnn &amp; a type of rnn (lstm) together."', 'a neural network to generate captions for an image using cnn and rnn with beam search. - dabasajay/image-caption-generator"', 'an overview of image caption generation methods" name="title"/>', 'explore and run machine learning code with kaggle notebooks | using data from flicker8k_dataset"', '/exchanges/models/all/max-image-caption-generator/--https://developer.ibm.com/technologies/artificial-intelligence" name="madeupmeta"/>', 'Image caption generator', 'Image caption generator', '/exchanges/models/all/max-image-caption-generator/--https://developer.ibm.com/technologies/artificial-intelligence" name="madeupmeta"/>', 'explore and run machine learning code with kaggle notebooks | using data from flicker8k_dataset"', 'python based project on image caption generator - learn to build a working model of image caption generator by implementing cnn &amp; a type of rnn (lstm) together."']

    return render_template("results.html",  Heading= Heading, desc= desc, options=add(10, head, desc))

if __name__== "__main__":
    app.run(debug=True)