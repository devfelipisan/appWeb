from django.http import HttpResponseRedirect
from django.shortcuts import render
from random import randint
from cadastro_funcionario.models import cadastroFuncionario

def gerar_banco(request):
    nomes = [("Alice", 48439120001, 450538886), ('Miguel', 35145684053, 433035912), ('Sophia', 91617092045, 457021718), ('Arthur', 57592829053, 419148322), ('Helena', 68316465060, 482526506), ('Bernardo', 35959741075, 202262017), ('Valentina', 71405908009, 364578075), ('Heitor', 96997763073, 236694935), ('Laura', 87177237011, 505238706), ('Davi', 90050385003, 171741237), ('Isabella', 24666134093, 339232298), ('Lorenzo',                                                                                                                                                                                                                                                                                                                                                                                                                  9095856011, 256247882), ('Manuela', 58580501075, 374690108), ('Théo', 89207469073, 493158467), ('Júlia', 24678291032, 406826018), ('Pedro', 83888390044, 156630278), ('Heloísa', 82757793080, 196353403), ('Gabriel', 23778938053, 196353403), ('Luiza', 64482418099, 166693856), ('Enzo', 72668263069, 325084956), ('Maria', 8790817087, 385042164), ('Luiza', 22042722057, 180375581), ('Matheus', 36840120090, 105199345), ('Clara', 20681272023, 8885697), ('AnaBeatriz', 93526181578, 5794530), ('Vitória', 71181015839, 4018394), ('Olívia', 4073876686, 1562785), ('MariaFernanda', 4886616097, 1077963), ('Emilly', 36537142229, 8802574), ('MariaValentina', 63655833709, 2767881), ('Milena', 83372746201, 4230348), ('MariaHelena', 64106198630, 7282054), ('Bianca', 71342748964, 8198357),
             ('Larissa', 51343534682, 9005272), ('Mirella', 63463348403, 1950261), ('MariaFlor', 3106555289, 6882948), ('Allana', 57807486910, 2008369), ('AnaSophia', 24622204886, 5696739), ('Clarice', 72397006235, 6116149), ('Pietra', 1281371424, 8491659), ('MariaVitória', 934915903, 4727043), ('Maya', 73222436681, 4417353), ('Laís', 70504690094, 4132623), ('Ayla', 46606408172, 6159146), ('AnaLívia', 27085617748, 1435259), ('Eduarda', 14902943506, 6408492), ('Mariah', 12947061101, 5480832), ('Stella', 18218187685, 1918962), ('Ana', 85246212220, 2646059), ('Gabrielly', 84933391300, 6432850), ('Sophie', 50313412200, 6003442), ('JoãoVictor', 80301914990, 7156702), ('LuizMiguel', 46628498611, 6231385), ('Francisco', 61093209780, 3450559), ('Kaique', 67483998660, 6142399), ('Otávio', 60749915021, 2125915), ('Augusto', 78203799876, 6568953), ('Levi', 46632136346, 6805184), ('Yuri', 66089179299, 2303879), ('Enrico', 55895934927, 5471527), ('Thiago', 29368135304, 8673066), ('Ian', 8240018009, 5634227), ('VictorHugo', 66030988735, 2853580), ('Thomas', 19048438241, 6971423), ('Henry', 80488375010, 4739499), ('LuizFelipe', 40055540, 3903842), ('Ryan', 12446808930, 3954370), ('ArthurMiguel', 54777596826, 5847869), ('DaviLuiz', 20828691487, 8700582), ('Nathan', 37388063420, 9170520), ('PedroLucas', 35817391511, 4439528), ('DaviMiguel', 89287466807, 3527625), ('Raul', 38515785463, 3687872), ('PedroMiguel', 31876573708, 7672152), ('LuizHenrique', 85228230572, 8786771), ('Luan', 47609283401, 4223131), ('Erick', 62258315417, 4180643), ('Martin', 18163421819, 4367603), ('Bruno', 73321779005, 5242094)]
    funcao = ['supervisor', 'opGuincho', 'opOxCorte', 'rigger']

    for nome in nomes:
        f = funcao[randint(0, 3)]
        matricula = randint(100000, 555555)
        new_funcionario = cadastroFuncionario(
            matricula_funcionario = matricula,
            nome_completo_funcionario = nome[0],
            funcao_funcionario = f,
            cpf_funcionario = nome[1],
            sispat_funcionario = nome[2],
            disponibilidade_funcionario = True,
        )
        new_funcionario.save()

    print('processado com sucesso')
    return HttpResponseRedirect('index/')

def limpar_banco(request):
    cadastroFuncionario.fullclean()
    

#Dicionários com os aeroportos Brasileiros
Aeroportos_Brasileiros={
    "SBBE":"Aeroporto Internacional de Belém",
    "SBCJ":"Aeroporto de Carajás",
    "SBHT":"Aeroporto de Altamira",
    "SBIZ":"Aeroporto de Imperatriz",
    "SBJC":"Aeroporto Júlio César",
    "SBMA":"Aeroporto de Marabá",
    "SBMQ":"Aeroporto Internacional de Macapa",
    "SBSL":"Aeroporto de São Luís",
    "SBSN":"Aeroporto de Santarém",
    "SRBR":"Superintendência Regional do Centro Oeste",
    "SBBR":"Aeroporto Internacional de Brasília",
    "SBCY":"Aeroporto Interancional de Cuiabá",
    "SBGO":"Aeroporto de Goiânia",
    "SBPJ":"Aeroporto de Palmas",
    "SBUL":"Aeroporto de Uberlândia",
    "SBUR":"Aeroporto de Uberaba",
    "SRMN":"Superintendência Regional do Noroeste",
    "SBBV":"Aeroporto Internacional de Boa Vista",
    "SBCZ":"Aeroporto Internacional de Cruzeiro do Sul",
    "SBEG":"Aeroporto Internacional de Manaus",
    "SBPV":"Aeroporto Internacional de Porto Velho",
    "SBRB":"Aeroporto Internacional de Rio Branco",
    "SBTF":"Aeroporto de Tefé",
    "SBTT":"Aeroporto Internacional de Tabatinga",
    "SRPA":"Superintendência Regional do Sul",
    "SBBG":"Aeroporto de Bagé",
    "SBBI":"Aeroporto de Bacacheri",
    "SBCT":"Aeroporto Internacional de Curitiba",
    "SBFI":"Aeroporto Internacional de Foz de Iguaçu",
    "SBFL":"Aeroporto Internacional de Florianópolis",
    "SBJV":"Aeroporto de Joinville",
    "SBLO":"Aeroporto de Londrina",
    "SBNF":"Aeroporto de Navegantes",
    "SBPA":"Aeroporto Internacional de Porto Alegre",
    "SBPK":"Aeroporto Internacional de Pelotas",
    "SBUG":"Aeroporto Internacional de Uruguaiana",
    "SRRF":"Superintendência Regional do Nordeste",
    "SBAR":"Aeroporto de Aracaju",
    "SBFZ":"Aeroporto Internacional de Fortaleza",
    "SBIL":"Aeroporto de Ilhéus",
    "SBJP":"Aeroporto Internacional de João Pessoa",
    "SBJU":"Aeroporto de Juazeiro do Norte",
    "SBKG":"Aeroporto de Campina Grande",
    "SBMO":"Aeroporto Internacional de Maceió",
    "SBNT":"Aeroporto Internacional de Natal",
    "SBPL":"Aeroporto de Petrolina",
    "SBRF":"Aeroporto Internacional de Recife",
    "SBSV":"Aeroporto Internacional de Salvador",
    "SBTE":"Aeroporto de Teresina",
    "SBUF":"Aeroporto Paulo Afonso",
    "SRGL":"Superintendência Regional do Leste",
    "SBBH":"Aeroporto da Pampulha",
    "SBCF":"Aeroporto Internacional de Confins",
    "SBCP":"Aeroporto de Campos",
    "SBGL":"Aeroporto Internacional do Galeão",
    "SBJF":"Aeroporto de Juíz de Fora",
    "SBJR":"Aeroporto de Jacarepaguá",
    "SBME":"Aeroporto de Macaé",
    "SBMK":"Aeroporto de Montes Claros",
    "SBRJ":"Aeroporto Santos Dumont",
    "SBVT":"Aeroporto de Vitória",
    "SBPR":"Aeroporto Carlos Prates",
    "SRGR":"Superintendência Regional do Sudeste",
    "SBCG":"Aeroporto Internacional de Campo Grande",
    "SBCR":"Aeroporto Internacional de Corumbá",
    "SBGR":"Aeroporto Internacional de Guarulhos",
    "SBKP":"Aeroporto Internacional de Campinas",
    "SBMT":"Aeroporto Campo de Marte",
    "SBPP":"Aeroporto Internacional de Ponta Porã",
    "SBSJ":"Aeroporto de São José dos Campos",
    "SBSP":"Aeroporto Internacional de Congonhas",
}

def index(request):
    return render(request, 'index/inicial.html', {'gerar_banco':gerar_banco})