def link_verification():
    openAI_url="https://api.openai.com/v1/chat/completions"

    header={
    'Authorization':'Bearer '+secret_key,
    'Content-Type':'application/json'
    }

    payload={
    'model':'text-davinci-002',
    'messages':[
        {'role':'user','content':'''I will give you a url and you have to check if the link possibly is a news article related to cybersecurity policy/strategy by reading the url only:
Just one word answer
Yes if possible
No, if not'''},
        {'role':'system','content':'Sure, please provide the URL, and I will check if it possibly relates to a news article on cybersecurity policy or strategy.'},
        {'role':'user','content':f'URL={}'}
    ]}