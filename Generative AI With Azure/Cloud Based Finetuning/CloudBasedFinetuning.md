### Part 1: Fundamentals of Fine-Tuning

What is the key benefit of fine-tuning a pre-trained model?

A) It reduces the need for computational resources

Which of the following tools optimizes model deployment in Azure?

A) ONNX Runtime

Legal Document Summarization: GPT-4

Legal documents contain specialized terminology and lengthy, complex sentences. Fine-tuning on a dataset of legal texts improves the model’s ability to extract key information while preserving legal accuracy.

Sentiment Analysis on Financial News: BERT

Financial sentiment differs from general sentiment and fine-tuning on labeled financial news articles refines the model’s ability to detect nuances.

Image Captioning for Medical Imaging: BLIP

Medical terminology and diagnostic findings require precision and fine-tuning ensures that captions align with expert radiology reports.

### Part 2: Implementing Fine-Tuning on Azure

I would select GPT-4 from Azure AI Studio’s catalog and fine-tune it for a customer service chatbot that specializes in handling refund and return inquiries for an e-commerce platform. The dataset would include: customer service transcripts and receipts, customer FAQs, and some synthetic data to help cover edge cases. The synthetic data would most likely be generated using another chatbot. To prepare the data, I would first have to remove any personal data and normalize the formatting of the text. I would then ensure the text is correctly labeled with correct categories, like refund or inquiries, and balance out the data so each category is equally represented. After fine-tuning, I would measure the accuracy of the chatbot to see if it's responding to prompts correctly. Some challenges that the model may face are answering unclear prompts. For instance, there may be prompts the model did not train for or it might struggle answering multi-part inquires. The model may also overfit to the training data and will not be general enough to cover the majority of questions.

### Part 3: Evaluating and Deploying Models

Fine-tuning eliminates the need for evaluation metrics. (False)

Azure Machine Learning provides tools for real-time monitoring of deployed models. (True)

Using metrics like F1 score and cross-validation is crucial to ensure that a fine-tuned model is trained to be reliable and general. The F1 score is especially important when handling important tasks, such as medical diagnosis, where false positives and false negatives can have large impacts on the individuals being diagnosed. Cross-validation ensures the model can generalize well to unseen data, reducing the risk of overfitting. Skipping these metrics can lead to major pitfalls. For example, a chatbot trained for customer service may generate polite but factually incorrect responses if precision is prioritized over recall. Similarly, sentiment analysis models may wrongly classify sentiments, and in a financial environment, it can cause crashes in the market. By using these metrics, we can mitigate these risks as much as possible to ensure models that are reliable and accurate.
