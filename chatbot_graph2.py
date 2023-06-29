#!/usr/bin/env python3
# coding: utf-8

from question_classifier import *
from question_parser import *
from answer_search import *
import ttkbootstrap as tk


class ChatBotGraph:
    """问答类"""

    def __init__(self):
        self.classifier = QuestionClassifier()
        self.parser = QuestionPaser()
        self.searcher = AnswerSearcher()

    def chat_main(self, question):
        answer = '抱歉没有找到您想要的答案！'
        res_classify = self.classifier.classify(question)
        print('chat_main question→', question)
        if not res_classify:
            print('chat_main answer1→', answer)
            return answer
        res_sql = self.parser.parser_main(res_classify)
        final_answers = self.searcher.search_main(res_sql)
        if not final_answers:
            print('chat_main answer2→', answer)
            return answer
        else:
            print('chat_main answer3→', final_answers)
            return '\n'.join(final_answers)


def get_answer(event=None):
    """显示问答结果"""
    print("e2: ", qa_input.get())
    answer = handler.chat_main(qa_input.get())
    text.delete("0.0", 'end')
    text.insert('insert', answer)


if __name__ == '__main__':
    handler = ChatBotGraph()
    root = tk.Window()
    root.title('医疗知识图谱智能问答')
    root.geometry('500x550')
    qa_input = tk.Entry(root, width=65, bootstyle='PRIMARY')
    qa_input.grid(row=10, column=1, sticky=tk.W, padx=10, pady=10)

    tk.Button(root, width=5, text="提问", bootstyle=('PRIMARY', "outline-toolbutton"),
              command=get_answer).grid(row=10, column=1, sticky=tk.W, padx=420, pady=10)
    # 结果展示区
    text = tk.Text(root, width=65, height=25)
    text.grid(row=30, column=1, sticky=tk.W, padx=10, pady=10)

    root.bind('<Return>', get_answer)  # 回车搜索
    root.mainloop()
