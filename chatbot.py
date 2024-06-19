from nltk.chat.util import Chat,reflections,pairs
pairs=[
    [r'hi',['hiii']],
    [r'hii|hey|hello',['hi there']],
    [r'how are you',['i am fine hoping you good']],
    [r'what is your name',['my name is chatbot']],
    [r'who invented you',['i am invented by Narayanamma']],
    [r'who is your boss',['my boss is Narayanamma']],
    [r'what can tell you for viewers',['please subscribe the my youtube channel']],
    [r'are you mad',['nice joke']],
    [r'sorry',['machine cannot have feelings its ok']],
    [r'what is python',['it is a programming language']],
]
chat=Chat(pairs,reflections)
chat.converse()
def quit():
    print("hi i am chatbot ask me something")

