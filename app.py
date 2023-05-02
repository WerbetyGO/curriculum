from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '''<p><strong><P><strong><font size="6">Olá, este é o meu curriculo online
</font></strong></p> 
<p>Meu nome é Werbety, estudante do curso de Sistemas de Informações</p>

<p><a href="{}">/sobre:</a> Página pessoal.</p>
<p><a href="{}">/experiencia:</a> Experiencias proficionais.</p>
<p><a href="{}">/formacao:</a> Formação academica.</p>
<p><a href="{}">/contato:</a> Página de contato.</p></p>
'''.format(url_for('sobre'), url_for('experiencia'), 
url_for('formacao'), url_for('contato'))

 
@app.route('/sobre')
def sobre():
    return '''<P><strong><font size="6">Sobre</font></strong></p>
<p>Olá!</p>   
<p>Olá, me chamo Geraldo Werbety de Souza Pereira, estudante do instituto federal no curso de sistemas de informação. 
atualmente trabalho prestando assessoria para prefeitura municipal de Várzea Alegre.</p>
<p><a href="{}">/home</a>
'''.format(url_for('home'))
@app.route('/experiencia')
def experiencia():
    return '''<P><strong><font size="6">Experiencia</font></strong></p>
Como Experiencias profissinais, estagiei 6 meses como monitor de informática na EEEP Dr. Jose iran costa.<p><a href="{}">/home</a>
 '''.format(url_for('home'))
@app.route('/formacao')
def formacao():
    return '''<P><strong><font size="6">Formação</font></strong></p>
<p><strong>Superior - Cursando:</strong></p>
<p>Instituto Federal de Educação, Ciência e Tecnologia do Ceará
Bacharelado, Tecnologia em Tecnologia da Informação/Sistemas da
Informação·</p>
<p><strong>Cursos complementares:</strong></p>
<p>Manutenção de portateis 40H</p>
<p>Tecnico de Informática 1.200H</p>
<a href="{}">/home</a>
'''.format(url_for('home'))
@app.route('/contato')
def contato(): 
    return ''' <P><strong><font size="6">Contato</font></strong></p>

<p>Werbetygo@gmail.com</p>
<p>(88) 99635 - 6296 (comercial)</p><p><a href="{}">/home</a>

'''.format(url_for('home'))
if __name__ == '__main__':
    app.run()