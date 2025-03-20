Task Definition: An AI powered resume assistant that helps generate and refine resumes.

Prompt Flow Design: Using the flow structure in Azure's Visual Editor, we have the input node, pre-processing node, model node, post-processing node, and output node. The input node captures user provided details like job title, skills, and experience. The preprocessing node will format the data into a structured prompt. The model node uses the prompt to generate a resume draft. The post-processing node then analyzes output, and the output node will display the final draft.

Prototype Summary: The steps involved was configuring Azure OpenAI Service for LLM-based text generation, designing prompt flow, and integrated feedback mechanism to improve response accuracy.

Monitoring Insights: Key metrics to analyze was latency, error rate, and user feedback. Azure tools allow for monitoring latency and error rates.

Future Improvements: Some improvements can be multi-language support, customizing styles based on industry, or realtime collaboration.
