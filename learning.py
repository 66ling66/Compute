import streamlit as st

objects=st.text_input('请输入你要统计的科目，科目之间用空格隔开(输入完毕请按回车键确认)',value='高数 物理 语文')

grade=st.text_input('请输入每个科目对应的学分,每个学分之间用空格隔开(输入完毕请按回车键确认)',value='3 4 5')

objects=objects.split()
grade=grade.split()

result=[]
for i in range(len(objects)):
    result.append({objects[i]:int(grade[i])})
st.write(f'请确认学科与学分的对应关系没有输入错误{result}')
score=st.text_input('请输入每一个科目对应的分数，每个分数之间用空格隔开(输入完毕请按回车键确认)',value='87 88 96')

score=score.split()

sum=0
sum_score=0
for i in range(len(objects)):
    sum+=int(grade[i])
    sum_score+=int(score[i])*int(grade[i])
st.write(f'sum:{sum},grade:{sum_score}')
mean=sum_score/sum
st.write(f'该学生的最终得分是:{mean}')

st.header('''citation:''')
st.write('''writer : Pengshuwei email : s.w.peng@foxmail.com 注:如果你有在准备什么比赛或者需要帮助，欢迎发送邮件到我的个人邮箱，我会不定期查看我的邮箱''')
st.write('更多功能欢迎私信')
