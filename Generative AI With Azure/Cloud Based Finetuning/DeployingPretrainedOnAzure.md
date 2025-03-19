Task Definition: Legal Document Summarization

The significance of this task is that it helps improve the efficiency, decision-making, and assessibility in law. Legal documents are often lengthy and complex, making it difficult for the general public to extract information from them. With summarization, these tasks can be simplified, which will positively impact the legal field.

Dataset Insights

When preparing the dataset, I had to make the data came from reliable sources. These sources include legal textbooks, cases, and law documents that are publicly available. Since we are only interested in the actually text, we can remove things like metadata, citations, and footnotes. The text then had to be normalized, like lowercasing the text, removing extra whitespace, and special characters. The data then had to be split into training, validation, and testing.

Model Training Summary

When fine-tuning, I decided to select the LegalBERT model. This is because LegalBERT is an optimized model for understanding legal text and BERT models are well-suited summarization tasks. I then selected a set of hyperparameters and adjusted while experimenting to see if I can improve the model.

Evaluation Results

The metrics I used were the ROUGE Score and BLEU Score.

Deployment

To deploy, I just created a workspace and followed instructors to upload my model.

Future Improvements

Future improvements could be adding multi-language support and optimizing the speed of the model.
