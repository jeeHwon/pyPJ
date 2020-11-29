from slacker import Slacker

slack = Slacker('xoxb-1526706418517-1544433012337-Jh2RJyugEq7L8GoAPbaatwTU')
# slack.chat.post_message('#general', '안녕!!')

markdown_text = """
This message is plain.
*This message is bold.*
'This message is code.'
_This message is italic._
~This message is strike.~
"""

attach_dict = {
    'color'         :'#ff0000',
    'author_name'   :'Jswon',
    'author_link'   :'github/jeeHwon',
    'title'         :'오늘의 증시 KOSPI',
    'title_link'    :'https://finance.naver.com/sise/sise_index.nhn?code=KOSPI',
    'text'          :'2,633.45 ^7.54 +0.29%',
    'image_url'     :'https://ssl.pstatic.net/imgstock/chart3/day/KOSPI.png'
}

attach_list = [attach_dict]
slack.chat.post_message(channel="#general", text=markdown_text, attachments=attach_list)