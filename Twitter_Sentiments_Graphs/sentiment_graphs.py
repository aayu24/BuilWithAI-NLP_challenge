# -*- coding: utf-8 -*-
"""sentiment_graphs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EXd88xU35IdMU5OjxAnIkmNPO_rO_8ls
"""

!pip install -U kaleido
import pandas as pd

df = pd.read_excel(r'/content/drive/My Drive/CNN_articles_tones.xlsx')
df.head()

df['published_date'] =pd.to_datetime(df.published_date)
df_joy = df.groupby('published_date').count().reset_index()
df_joy = df_joy[25:]

df_joy.head()

!pip install plotly==4.7.1
!wget https://github.com/plotly/orca/releases/download/v1.2.1/orca-1.2.1-x86_64.AppImage -O /usr/local/bin/orca
!chmod +x /usr/local/bin/orca
!apt-get install xvfb libgtk2.0-0 libgconf-2-4
import plotly.graph_objects as go

import os

if not os.path.exists("images"):
    os.mkdir("images")

import plotly.express as px
fig = px.line(df_joy,x='published_date',y='Joy',title='Joy')
fig.update_xaxes(rangeslider_visible=True)
# fig.write_html('joy_graph.html')
fig.write_image("images/joy_graph.png")
fig.show()

fig = px.line(df_joy,x='published_date',y='Fear',title='Fear')
fig.update_xaxes(rangeslider_visible=True)
# fig.write_html('fear_graph.html')
fig.write_image('fear_graph.png')
fig.show()

fig = px.line(df_joy,x='published_date',y='Analytical',title='Analytical')
fig.update_xaxes(rangeslider_visible=True)
fig.write_image('analytical_graph.png')
fig.show()

fig = px.line(df_joy,x='published_date',y='Sadness',title='Sadness')
fig.update_xaxes(rangeslider_visible=True)
fig.write_image('sadness_graph.png')
fig.show()

fig = px.line(df_joy,x='published_date',y='Confident',title='Confidence')
fig.update_xaxes(rangeslider_visible=True)
fig.write_image('confident_graph.png')
fig.show()

fig = px.line(df_joy,x='published_date',y='Anger',title='Angry')
fig.update_xaxes(rangeslider_visible=True)
fig.write_image('anger_graph.png')
fig.show()

fig = px.line(df_joy,x='published_date',y='Tentative',title='Hesitant')
fig.update_xaxes(rangeslider_visible=True)
fig.write_image('tentative_graph.png')
fig.show()



df_twitter = pd.read_csv(r'/content/drive/My Drive/vis/Book2.csv')
df_twitter.head()

# df_twitter.columns.name= "Emotions"

df_twitter.dropna()

!pip install emoji --upgrade
import emoji

title = emoji.emojize('Love :heart:',use_aliases=True)
fig = px.line(df_twitter,x='Date',y='Love',title=title)
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(title_text=title, title_x=0.5)
fig.write_image('love_twitter_graph.png')
fig.write_html('love_twitter_graph.html')
fig.show()

title = emoji.emojize('Anger :angry:',use_aliases=True)
fig = px.line(df_twitter,x='Date',y='Anger',title=title)
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(title_text=title, title_x=0.5)
fig.write_image('anger_twitter_graph.png')
fig.write_html('anger_twitter_graph.html')
fig.show()

title = emoji.emojize('Joy :joy:',use_aliases=True)
fig = px.line(df_twitter,x='Date',y='Joy',title=title)
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(title_text=title, title_x=0.5)
fig.write_image('joy_twitter_graph.png')
fig.write_html('joy_twitter_graph.html')
fig.show()

title = emoji.emojize('Fear :fearful:',use_aliases=True)
fig = px.line(df_twitter,x='Date',y='Fear',title=title)
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(title_text=title, title_x=0.5)
fig.write_image('fear_twitter_graph.png')
fig.write_html('fear_twitter_graph.html')
fig.show()

title = emoji.emojize('Sadness :cry:',use_aliases=True)
fig = px.line(df_twitter,x='Date',y='Sad',title=title)
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(title_text=title, title_x=0.5)
fig.write_image('sadness_twitter_graph.png')
fig.write_html('sadness_twitter_graph.html')
fig.show()

title = emoji.emojize('Surprise :astonished:',use_aliases=True)
fig = px.line(df_twitter,x='Date',y='Surprise',title=title)
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(title_text=title, title_x=0.5)
fig.write_image('surprise_twitter_graph.png')
fig.write_html('surprise_twitter_graph.html')
fig.show()

