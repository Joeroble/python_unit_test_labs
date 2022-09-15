import requests

question = input('Enter your question for the magic 8 ball: ')

magic_8_ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'

response = requests.get(magic_8_ball_url).json()

answer = response['magic']['answer']

print(f'The magic 8 ball says....  {answer}')
