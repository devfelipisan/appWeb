# Generated by Django 3.0.2 on 2020-01-28 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro_unidade', '0002_auto_20200125_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frenteprogramada',
            name='local_desembarque',
            field=models.CharField(choices=[['SBBE', 'Aeroporto Internacional de Belém'], ['SBCJ', 'Aeroporto de Carajás'], ['SBHT', 'Aeroporto de Altamira'], ['SBIZ', 'Aeroporto de Imperatriz'], ['SBJC', 'Aeroporto Júlio César'], ['SBMA', 'Aeroporto de Marabá'], ['SBMQ', 'Aeroporto Internacional de Macapa'], ['SBSL', 'Aeroporto de São Luís'], ['SBSN', 'Aeroporto de Santarém'], ['SRBR', 'Superintendência Regional do Centro Oeste'], ['SBBR', 'Aeroporto Internacional de Brasília'], ['SBCY', 'Aeroporto Interancional de Cuiabá'], ['SBGO', 'Aeroporto de Goiânia'], ['SBPJ', 'Aeroporto de Palmas'], ['SBUL', 'Aeroporto de Uberlândia'], ['SBUR', 'Aeroporto de Uberaba'], ['SRMN', 'Superintendência Regional do Noroeste'], ['SBBV', 'Aeroporto Internacional de Boa Vista'], ['SBCZ', 'Aeroporto Internacional de Cruzeiro do Sul'], ['SBEG', 'Aeroporto Internacional de Manaus'], ['SBPV', 'Aeroporto Internacional de Porto Velho'], ['SBRB', 'Aeroporto Internacional de Rio Branco'], ['SBTF', 'Aeroporto de Tefé'], ['SBTT', 'Aeroporto Internacional de Tabatinga'], ['SRPA', 'Superintendência Regional do Sul'], ['SBBG', 'Aeroporto de Bagé'], ['SBBI', 'Aeroporto de Bacacheri'], ['SBCT', 'Aeroporto Internacional de Curitiba'], ['SBFI', 'Aeroporto Internacional de Foz de Iguaçu'], ['SBFL', 'Aeroporto Internacional de Florianópolis'], ['SBJV', 'Aeroporto de Joinville'], ['SBLO', 'Aeroporto de Londrina'], ['SBNF', 'Aeroporto de Navegantes'], ['SBPA', 'Aeroporto Internacional de Porto Alegre'], ['SBPK', 'Aeroporto Internacional de Pelotas'], ['SBUG', 'Aeroporto Internacional de Uruguaiana'], ['SRRF', 'Superintendência Regional do Nordeste'], ['SBAR', 'Aeroporto de Aracaju'], ['SBFZ', 'Aeroporto Internacional de Fortaleza'], ['SBIL', 'Aeroporto de Ilhéus'], ['SBJP', 'Aeroporto Internacional de João Pessoa'], ['SBJU', 'Aeroporto de Juazeiro do Norte'], ['SBKG', 'Aeroporto de Campina Grande'], ['SBMO', 'Aeroporto Internacional de Maceió'], ['SBNT', 'Aeroporto Internacional de Natal'], ['SBPL', 'Aeroporto de Petrolina'], ['SBRF', 'Aeroporto Internacional de Recife'], ['SBSV', 'Aeroporto Internacional de Salvador'], ['SBTE', 'Aeroporto de Teresina'], ['SBUF', 'Aeroporto Paulo Afonso'], ['SRGL', 'Superintendência Regional do Leste'], ['SBBH', 'Aeroporto da Pampulha'], ['SBCF', 'Aeroporto Internacional de Confins'], ['SBCP', 'Aeroporto de Campos'], ['SBGL', 'Aeroporto Internacional do Galeão'], ['SBJF', 'Aeroporto de Juíz de Fora'], ['SBJR', 'Aeroporto de Jacarepaguá'], ['SBME', 'Aeroporto de Macaé'], ['SBMK', 'Aeroporto de Montes Claros'], ['SBRJ', 'Aeroporto Santos Dumont'], ['SBVT', 'Aeroporto de Vitória'], ['SBPR', 'Aeroporto Carlos Prates'], ['SRGR', 'Superintendência Regional do Sudeste'], ['SBCG', 'Aeroporto Internacional de Campo Grande'], ['SBCR', 'Aeroporto Internacional de Corumbá'], ['SBGR', 'Aeroporto Internacional de Guarulhos'], ['SBKP', 'Aeroporto Internacional de Campinas'], ['SBMT', 'Aeroporto Campo de Marte'], ['SBPP', 'Aeroporto Internacional de Ponta Porã'], ['SBSJ', 'Aeroporto de São José dos Campos'], ['SBSP', 'Aeroporto Internacional de Congonhas']], max_length=64),
        ),
        migrations.AlterField(
            model_name='frenteprogramada',
            name='local_embarque',
            field=models.CharField(choices=[['SBBE', 'Aeroporto Internacional de Belém'], ['SBCJ', 'Aeroporto de Carajás'], ['SBHT', 'Aeroporto de Altamira'], ['SBIZ', 'Aeroporto de Imperatriz'], ['SBJC', 'Aeroporto Júlio César'], ['SBMA', 'Aeroporto de Marabá'], ['SBMQ', 'Aeroporto Internacional de Macapa'], ['SBSL', 'Aeroporto de São Luís'], ['SBSN', 'Aeroporto de Santarém'], ['SRBR', 'Superintendência Regional do Centro Oeste'], ['SBBR', 'Aeroporto Internacional de Brasília'], ['SBCY', 'Aeroporto Interancional de Cuiabá'], ['SBGO', 'Aeroporto de Goiânia'], ['SBPJ', 'Aeroporto de Palmas'], ['SBUL', 'Aeroporto de Uberlândia'], ['SBUR', 'Aeroporto de Uberaba'], ['SRMN', 'Superintendência Regional do Noroeste'], ['SBBV', 'Aeroporto Internacional de Boa Vista'], ['SBCZ', 'Aeroporto Internacional de Cruzeiro do Sul'], ['SBEG', 'Aeroporto Internacional de Manaus'], ['SBPV', 'Aeroporto Internacional de Porto Velho'], ['SBRB', 'Aeroporto Internacional de Rio Branco'], ['SBTF', 'Aeroporto de Tefé'], ['SBTT', 'Aeroporto Internacional de Tabatinga'], ['SRPA', 'Superintendência Regional do Sul'], ['SBBG', 'Aeroporto de Bagé'], ['SBBI', 'Aeroporto de Bacacheri'], ['SBCT', 'Aeroporto Internacional de Curitiba'], ['SBFI', 'Aeroporto Internacional de Foz de Iguaçu'], ['SBFL', 'Aeroporto Internacional de Florianópolis'], ['SBJV', 'Aeroporto de Joinville'], ['SBLO', 'Aeroporto de Londrina'], ['SBNF', 'Aeroporto de Navegantes'], ['SBPA', 'Aeroporto Internacional de Porto Alegre'], ['SBPK', 'Aeroporto Internacional de Pelotas'], ['SBUG', 'Aeroporto Internacional de Uruguaiana'], ['SRRF', 'Superintendência Regional do Nordeste'], ['SBAR', 'Aeroporto de Aracaju'], ['SBFZ', 'Aeroporto Internacional de Fortaleza'], ['SBIL', 'Aeroporto de Ilhéus'], ['SBJP', 'Aeroporto Internacional de João Pessoa'], ['SBJU', 'Aeroporto de Juazeiro do Norte'], ['SBKG', 'Aeroporto de Campina Grande'], ['SBMO', 'Aeroporto Internacional de Maceió'], ['SBNT', 'Aeroporto Internacional de Natal'], ['SBPL', 'Aeroporto de Petrolina'], ['SBRF', 'Aeroporto Internacional de Recife'], ['SBSV', 'Aeroporto Internacional de Salvador'], ['SBTE', 'Aeroporto de Teresina'], ['SBUF', 'Aeroporto Paulo Afonso'], ['SRGL', 'Superintendência Regional do Leste'], ['SBBH', 'Aeroporto da Pampulha'], ['SBCF', 'Aeroporto Internacional de Confins'], ['SBCP', 'Aeroporto de Campos'], ['SBGL', 'Aeroporto Internacional do Galeão'], ['SBJF', 'Aeroporto de Juíz de Fora'], ['SBJR', 'Aeroporto de Jacarepaguá'], ['SBME', 'Aeroporto de Macaé'], ['SBMK', 'Aeroporto de Montes Claros'], ['SBRJ', 'Aeroporto Santos Dumont'], ['SBVT', 'Aeroporto de Vitória'], ['SBPR', 'Aeroporto Carlos Prates'], ['SRGR', 'Superintendência Regional do Sudeste'], ['SBCG', 'Aeroporto Internacional de Campo Grande'], ['SBCR', 'Aeroporto Internacional de Corumbá'], ['SBGR', 'Aeroporto Internacional de Guarulhos'], ['SBKP', 'Aeroporto Internacional de Campinas'], ['SBMT', 'Aeroporto Campo de Marte'], ['SBPP', 'Aeroporto Internacional de Ponta Porã'], ['SBSJ', 'Aeroporto de São José dos Campos'], ['SBSP', 'Aeroporto Internacional de Congonhas']], max_length=64),
        ),
    ]