from django.http import HttpResponseRedirect
from django.shortcuts import render
from random import randint
from cadastro_funcionario.models import cadastroFuncionario,certificadoFuncionario
from cadastro_curso.models import cadastroCurso

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
        
        for i in range(randint(1,2)):
            new_certificado = certificadoFuncionario(
                nome_funcionario=cadastroFuncionario.objects.get(matricula_funcionario=matricula),
                curso_funcionario=cadastroCurso.objects.get(id=randint(1,8)),
                data_realizada='2020-02-22',
                valido_ate='2020-03-22',
                )
            new_certificado.save()

    print('processado com sucesso')
    return HttpResponseRedirect('/')

def index(request):
    return render(request, 'index/inicial.html', {'gerar_banco':gerar_banco})

def limparBanco(request):
    cadastroFuncionario.objects.all().delete()
    return HttpResponseRedirect('/')

def limparCertificado(request):
    certificadoFuncionario.objects.all().delete()
    return HttpResponseRedirect('/')