import sqlite3

def setupDatabase():
    conn = sqlite3.connect('segurancaApp.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer1 TEXT NOT NULL,
            answer2 TEXT NOT NULL,
            answer3 TEXT NOT NULL,
            correctAnswer INTEGER NOT NULL
        )
    ''')
    
    cursor.executemany('''
        INSERT INTO quiz (question, answer1, answer2, answer3, correctAnswer) VALUES (?, ?, ?, ?, ?)
    ''', [
        ('Qual a melhor prática para criar uma senha?', 'Senhas simples e fáceis de lembrar', 'Senhas complexas e únicas', 'Usar a mesma senha para todos os sites', 1),
        ('Qual o objetivo da autenticação de dois fatores?', 'Facilitar o login', 'Adicionar uma camada extra de segurança', 'Eliminar a necessidade de senhas', 1),
        ('Qual é a melhor maneira de proteger seus dispositivos móveis?', 'Usar uma senha ou método de autenticação biométrica', 'Deixar o dispositivo desbloqueado para acesso rápido', 'Conectar-se a redes Wi-Fi públicas sem proteção', 0),
        ('Posso me conectar em redes wi-fi publicas?', 'Não posso me conectar, pois é uma rede insegura.', 'Posso me conectar e acessar informações sensíveis como de costume.', 'Posso me conectar, porém com cautela e atenção para não roubarem meus dados.', 2)
    ])
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setupDatabase()






