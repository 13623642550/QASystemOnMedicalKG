#!/usr/bin/env python3
# coding: utf-8
# File: chatbot_graph.py
# Author: lhy<lhy_in_blcu@126.com,https://huangyong.github.io>
# Date: 18-10-4

from question_classifier import *
from question_parser import *
from answer_search import *
import ttkbootstrap as tk

'''问答类'''


class ChatBotGraph:
    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, sent):
        answer = '您好，我是小勇医药智能助理，希望可以帮到您。如果没答上来，可联系https://liuhuanyong.github.io/。祝您身体棒棒！'
        res_classify = self.classifier.classify(sent)
        print('chat_main sent→', sent)
        if not res_classify:
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            return answer
        else:
            return '\n'.join(final_answers)


def get_entry_contetn():
    print("e2: ", qa_input.get())
    answer = handler.chat_main(qa_input.get())
    text.delete("0.0", 'end')
    text.insert('insert', answer)


if __name__ == '__main__':
    handler = ChatBotGraph()
    root = tk.Window()
    root.geometry('500x550')
    qa_input = tk.Entry(root, width=65, bootstyle='PRIMARY')
    qa_input.grid(row=10, column=1, sticky=tk.W, padx=10, pady=10)

    tk.Button(root, width=5, text="提问", bootstyle=('PRIMARY', "outline-toolbutton"),
              command=get_entry_contetn).grid(row=10, column=1, sticky=tk.W, padx=420, pady=10)

    # 结果展示区
    text = tk.Text(root, width=65, height=25)
    text.grid(row=30, column=1, sticky=tk.W, padx=10, pady=10)

    root.mainloop()
