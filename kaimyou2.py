#!/usr/share/nginx/.virtualenvs/env3.7/bin/python

import io, sys, os, json, codecs, random, datetime, cgi

# 文字化け対策
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

title_str = 'あなたの戒名は…'

form = cgi.FieldStorage()
age = int(form["age"].value)
sei = int(form["mymail"].value)
hyouka = int(form["passcode"].value)

if age <= 1 and sei == 1 :
    igo="嬰子"

elif age <= 1 and sei == 2 :
    igo="嬰女"

elif age >= 2 and age < 6 and sei == 1:
    igo="孩子"

elif age >= 2 and age < 6 and sei == 2:
    igo="孩女"

elif age >= 6 and age < 18 and sei == 1:
    igo="童子"

elif age >= 6 and age < 18 and sei == 2:
    igo="童女"

elif age >= 18 and sei == 1 and hyouka ==1:
    igo="大居士"

elif age >= 18 and sei == 2 and hyouka ==1:
    igo="大姉"

elif age >= 18 and sei == 1 and hyouka ==2:
    igo="信士"

elif age >= 18 and sei == 2 and hyouka ==2:
    igo="信女"

#文字をランダムで取得する

with open("kyouten.txt","r",encoding="utf-8_sig") as f:
    lines = f.read().splitlines()

import random

num=len(lines)-1

num1=random.randint(0,num)
num2=random.randint(0,num)
num3=random.randint(0,num)
num4=random.randint(0,num)
num5=random.randint(0,num)

mozi1 = lines[num1]
mozi2 = lines[num2]
mozi3 = lines[num3]
mozi4 = lines[num4]
mozi5 = lines[num5]
mozi6 = igo


print('''
Content-type: text/html

<!DOCTYPE html>
<html lang="ja">
  <head>
    <meta charset="utf-8">
    <title>あなたの戒名</title>
  </head>
  <body>
  <h1 style="color:red">あなたの戒名は</h1>
  <h2>戒名は<span style="color:blue;">{0}{1}院{2}誉{3}{4}{5}</span></h2>
  <h1>です！</h2>
</body>
</html>
'''[1:-1].format(mozi1,mozi2,mozi3,mozi4,mozi5,mozi6))