# Wechat-Model-Training-Q-A-bot

#Description: This project is designed to create a WeChat bot capable of answering questions, with code derived from ChatGPT. This implementation references a project by zhayujie and is deployed on Railway to achieve automatic replies on WeChat through GPT. It is currently ongoing with updates being made periodically.

Data fine-tuning for this project utilizes 40,380 WeChat group chat records and has set roles such as group admin and student representative as “assistance” during fine-tuning.
Implementation Steps:

#Export Chat History
        Use WechatExporter to export chat histories as txt files.
        Utilize the script import json(step2).py to convert txt to json for export. This script not only helps in exporting but also uploads to the API cloud database directly, providing a file ID needed for subsequent steps.

#Fine-tuning Process
        Run the script fine tune(step4).
        Input your API credentials and the obtained file ID.
        Initiate fine-tuning (Note: Ensure that the necessary fees are paid beforehand, or the process will fail).
        This script is divided into two parts:
        a. Upload the jsonl to GPT's cloud and begin training.
        b. Check the training status. Generally, a quick look is sufficient, and you will be notified via email upon completion.

#Deployment on Railway
        Once the model is trained, follow the one-click setup mentioned in assemble railway(step5).txt.
        Input the trained model ID and your API credentials, then scan using WeChat to start using your trained model.

#Subsequent Fine-tuning
        Repeat the previous steps for any subsequent adjustments.
        When deploying on Railway, set more tokens for memory and have more dialogues and corrections with it. Then, use the new chat data to further refine the model.

Note:

This project is aimed at those who wish to leverage a fine-tuned model to create a WeChat bot with Q&A capabilities. Ensure that you follow each step carefully and consult the referenced projects for any additional clarifications. Regular updates and refinements are being made to enhance the functionality and performance of the bot.
Additional Comments:

#When exporting chat history, please ensure data privacy and comply with relevant laws and platform policies.
The performance of the model depends on the quality and quantity of the training data, and further refinements may be necessary based on real-world interactions and feedback.
