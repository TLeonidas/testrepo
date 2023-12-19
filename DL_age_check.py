# Drive License age check (in Portuguese)
print('-----------------' + 'DEPARTAMENTO DE TRANSITO' + '-----------------')
print('- - - - - - - -  DRIVE LICENSE AGE CHECK  - - - - - - - -')

ano_atual = int(2023)
ano_nasc = int(input('Digite o ano do seu nascimento: '))
quanto_falta = int(18 - (ano_atual - ano_nasc))

if (ano_atual - ano_nasc) >= 18:
  print('Voce ja possui maioridade')
else:
  print('Voce ainda precisa aguardar ' + str(quanto_falta) + ' anos para poder tirar a carteira.')
