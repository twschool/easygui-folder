import easygui as eg
import openai
openai.api_key = "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"
model_engine = "gpt-3.5-turbo"
while True:
    user_input = input("Enter your sentence to be converted to us spelling: ")
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "system", "content": "You are a spellcheck converting words to the american spelling"
                                          " when I give you a sentence just give me the sentence back with"
                                          "american spelling eg: "
                                          "if I gave you the sentence 'I like colour' you would"
                                          " return'I like color' if I ask you a question then spellcheck the"
                                          " question instead of answering it. Eg: 'do you like pies' you would return"
                                          "'Do you like pies?'"},
            {"role": "user", "content": f"{user_input}"},
        ])

    message = response.choices[0]['message']
    print("{}: {}".format(message['role'], message['content']))



