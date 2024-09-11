import tkinter as tk
from tkinter import PhotoImage, Label, Button
import sqlite3
import webbrowser



def openLink(url):
    webbrowser.open(url)
    

class SegurancaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconbitmap("app.ico")
        self.title("InfoSegura")
        self.geometry("663x660")
        self.configure(background="#1d1e24")
        self.resizable(width= False, height= False)
        
       

        self.logo = PhotoImage(file="background.png")
        self.image1 = Label(self, image=self.logo, bg= "#1d1e24")
        self.image1.grid(row=0, column=0, padx=0, pady=0)
        


        Button(self, text="Por que devo me preocupar? ", command=self.showPreocupar).grid(row=1, column=0, pady=10)
        Button(self, text="Informações Iniciais", command=self.showTutorial).grid(row=2, column=0, pady=10)
        Button(self, text="Ver Dicas de Segurança", command=self.showDicas).grid(row=3, column=0, pady=10)
        Button(self, text="Faça um Quiz", command=self.showQuiz).grid(row=4, column=0, pady=10)

        self.conn = sqlite3.connect('segurancaApp.db')
        self.cursor = self.conn.cursor()



    def showPreocupar(self):
        preocuparWindow = tk.Toplevel(self)
        preocuparWindow.title("Preocupações")
        preocuparWindow.geometry("400x300")
        preocuparWindow.iconbitmap("app.ico")
        preocuparWindow.resizable(width= False, height= False)


        tk.Label(preocuparWindow, text="As ferramentas de segurança da informação são uma forma eficaz de reduzir os riscos de uso indevido de seus dados, tais como:", wraplength=350).pack(pady=10)
        preocuparText = (
            "1. Utilização de senhas e números de cartões de crédito furtados;\n \n"
            "2. Acesso não autorizado à conta de internet;\n \n"
            "3. Visualização, alteração ou destruição de dados pessoais por terceiros;\n \n"
            "4. Roubo de identidade nas redes sociais;\n \n"
            "5. Envio de e-mail por terceiros; \n \n"
            "6. Invasão de computadores e disseminação de vírus.\n \n"
        )
        tk.Label(preocuparWindow, text=preocuparText, wraplength=350).pack(pady=10)



    def showTutorial(self):
        tutorialWindow = tk.Toplevel(self)
        tutorialWindow.title("Tutorial de Segurança")
        tutorialWindow.geometry("400x400")
        tutorialWindow.iconbitmap("app.ico")
        tutorialWindow.resizable(width= False, height= False)
        


        frame = tk.Frame(tutorialWindow)
        frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        


        tk.Label(frame, text="A segurança da informação é essencial no mundo digital. Veja algumas dicas para proteger seus dados contra roubos:", wraplength=350, justify=tk.LEFT).pack(pady=10)
        tutorialText = (
            "1. Senhas fortes: Use senhas complexas e únicas para cada serviço.\n \n"
            "2. Atualizações: Mantenha seus dispositivos e aplicativos atualizados.\n \n"
            "3. Phishing: Não clique em links suspeitos em emails ou mensagens.\n \n"
            "4. Backup: Faça backup regular dos seus dados importantes.\n \n"
            )

        tk.Label(frame, text=tutorialText, wraplength=350, justify=tk.LEFT).pack(pady=15)

        buttonText = ("Veja algumas dicas sobre segurança da informação.\n  \n" "Fonte: GCFAprendeLivre")
        tk.Label(frame, text=buttonText, wraplength=350, justify=tk.LEFT).pack(pady=10)
        tk.Button(frame, text="Assistir", command=lambda: openLink("https://youtu.be/QFdkggG34wo")).pack(pady=10)
    

    def showDicas(self):
        dicasWindow = tk.Toplevel(self)
        dicasWindow.title("Dicas de Segurança")
        dicasWindow.geometry("400x400")

        dicasWindow.iconbitmap("app.ico")
        dicasWindow.resizable(width= False, height= False)
    

        frame = tk.Frame(dicasWindow) 
        frame.pack(fill= tk.BOTH, expand= True, padx= 10, pady= 10)
        
        tk.Label(frame, text="Aqui estão algumas dicas práticas para manter suas informações seguras:", wraplength=350, justify=tk.LEFT).pack(pady=10)
        tutorialText = (
            "• Use autenticação de dois fatores sempre que possível.\n \n"
            "• Verifique a segurança dos sites antes de inserir informações pessoais.\n \n"
            "• Não compartilhe suas senhas com ninguém.\n \n"
            "• Tenha cuidado ao usar redes Wi-Fi públicas.\n \n"
        )
        tk.Label(frame, text=tutorialText, wraplength=350).pack(pady=10)

        buttonText = ("Abaixo uma cartilha com dicas de Segurança da Informação para nosso dia a dia.\n  \n" "Fonte: Codern")
        tk.Label(frame, text=buttonText, wraplength=350, justify=tk.LEFT).pack(pady=10)
        tk.Button(frame, text="Conferir", command=lambda: openLink("https://codern.com.br/wp-content/uploads/2021/06/Cartilha-Codern-DICAS-DE-SEGURANCA-v1.pdf")).pack(pady=10)

    def showQuiz(self):
        quizWindow = tk.Toplevel(self)
        quizWindow.title("Quiz de Segurança")
        quizWindow.geometry("600x200")
        quizWindow.iconbitmap("app.ico")
        quizWindow.resizable(width= False, height= False)
    
        
        self.conn = sqlite3.connect('segurancaApp.db')
        self.cursor = self.conn.cursor()
        
        self.questionIndex = 0
        self.score = 0
        self.questions = self.loadQuestions()
        
        self.questionLabel = tk.Label(quizWindow, text="", wraplength=350)
        self.questionLabel.grid(row=0, column=0, pady=10)
        
        self.answerVar = tk.IntVar()
        
        self.answerButtons = []
        for i in range(3):
            btn = tk.Radiobutton(quizWindow, text="", variable=self.answerVar, value=i, command=self.checkAnswer)
            btn.grid(row=i+1, column=0, sticky='w')
            self.answerButtons.append(btn)
        
        self.showQuestion()

    def loadQuestions(self):
        self.cursor.execute('SELECT * FROM quiz')
        return self.cursor.fetchall()

    def showQuestion(self):
        if self.questionIndex < len(self.questions):
            question, answer1, answer2, answer3, correctAnswer = self.questions[self.questionIndex][1:]
            self.correctAnswer = correctAnswer
            self.questionLabel.config(text=question)
            for i, answer in enumerate([answer1, answer2, answer3]):
                self.answerButtons[i].config(text=answer)
            self.questionIndex += 1
        else:
            self.showResult()
            self.conn.close()

    def checkAnswer(self):
        selectedAnswer = self.answerVar.get()
        if selectedAnswer == self.correctAnswer:
            self.score += 1
        self.showQuestion()
        
        
        
    def showResult(self):
        resultWindow = tk.Toplevel(self)
        resultWindow.title("Resultado do Quiz")
        resultWindow.geometry("400x300")
        resultWindow.iconbitmap("app.ico")
        resultWindow.resizable(width= False, height= False)
    



        tk.Label(resultWindow, text=f'Resultado do quiz: Você acertou {self.score} de {len(self.questions)}', wraplength=350).pack(pady=10)
    
       
        correctAnswersText = "Respostas corretas:\n"
        for question, *answers, correctAnswer in self.questions:
            correctAnswersText += f'{question}: Resposta correta: {answers[correctAnswer]:}\n\n'
        
        tk.Label(resultWindow, text=correctAnswersText, wraplength=350, justify=tk.LEFT).pack(pady=10)

if __name__ == "__main__":
    app = SegurancaApp()
    app.mainloop()
