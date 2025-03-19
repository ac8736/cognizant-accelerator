Task Definition: The objective is to analyze the sentiment of reviews on a product. The significance of this task is that this world is ever-increasing in consumerism, with more and more products being released. Not all products are good, which is where reviews come in. Sentiment analysis is extremely prevalent since it can label products with a certain amount of sentiment. For instance, if a new car is released, people who are interested can use the model to output a general sentiment to see if the car is worth buying. This is incredibly faster than having to sit through and read all the reviews.

Model Selection: I selected the BERT models because these models were trained as classifiers, which is what sentiment analysis is.

Management Process: I had to collect and clean the selected dataset. I then chose a pretrained model and fine-tuned it with a selected dataset, like Amazon reviews or the IMDb reviews.

Solution Development: The implementation process involved loading the data and preprocessing the data by tokenizing it with the BERT Tokenizer. Using the Foundry's cloud GPUs, I trained the model with the dataset.

Evaluation Results: I used accuracy and F1 Score to evaluate the model's performance. Overall, it performed pretty well, with accuracy and F1 Score both scoring above 90%.

Future Improvements: Improvements could be expanding the dataset and also optimizing time by leveraging DistilBERT.
