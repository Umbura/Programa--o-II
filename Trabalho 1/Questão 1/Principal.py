#Gabrielly Alves Gomes - Matrícula: 20249035386
#Iago de Sousa Aragão - Matrícula: 20249014134
#Isaac Manuel Gomes Mineiro - Matrícula: 20249014170

from banco import Banco
from agencia import Agencia 
from conta import Conta, Corrente, Poupanca, Automatica

def imprimir_relatorios_completos(banco_obj):
    """Imprime o relatório do banco, de cada agência e de cada conta."""
    print("\n--- RELATÓRIO GERAL DO BANCO ---")
    banco_obj.relatorio()
    if not banco_obj.lista_agencias:
        print("   Não há agências cadastradas neste banco.")
    for ag in banco_obj.lista_agencias:
        print(f"\n   --- Relatório da Agência: {ag.numero} ---")
        ag.relatorio()
        if not ag.lista_contas:
            print("      Não há contas nesta agência.")
        for conta_obj in ag.lista_contas:
            print("      ", end="") 
            conta_obj.relatorio()
    print("--- FIM DO RELATÓRIO GERAL ---")

# 1. Criar um banco
banco_principal = Banco(1) 
print(f"Passo 1: Banco '{banco_principal.numero}' criado.")

# 2. Criar 2 agências e cadastrá-las no banco
banco_principal.cadastrar_agencia(101)
banco_principal.cadastrar_agencia(102)
print("Passo 2: Agências 101 e 102 cadastradas no banco.")

# Obter referências às agências cadastradas
agencia1 = banco_principal.buscar_agencia(101)
agencia2 = banco_principal.buscar_agencia(102)

if not agencia1 or not agencia2:
    print("ERRO: Não foi possível encontrar as agências cadastradas.")
    exit()

# 3. Criar contas

print("Passo 3: Criando contas nas agências...")
contas_criadas_total = []

def criar_contas_em_agencia(agencia_obj, num_agencia_para_prefixo_conta):
    """Cria os tipos de conta especificados na Questão 4 para uma agência."""
    prefixo_conta = num_agencia_para_prefixo_conta * 1000

    # 1 Conta
    c1 = Conta(numero=(prefixo_conta + 1), saldo=0.0)
    agencia_obj.lista_contas.append(c1)
    contas_criadas_total.append(c1)
    print(f"   - Criada Conta {c1.get_numero()} na Agência {agencia_obj.numero}")

    # 1 Corrente 
    cc1 = Corrente(numero=(prefixo_conta + 2), saldo=0.0) 
    agencia_obj.lista_contas.append(cc1)
    contas_criadas_total.append(cc1)
    print(f"   - Criada Conta Corrente {cc1.get_numero()} na Agência {agencia_obj.numero}")

    # 2 Poupanca
    cp1 = Poupanca(numero=(prefixo_conta + 3), saldo=0.0)
    agencia_obj.lista_contas.append(cp1)
    contas_criadas_total.append(cp1)
    print(f"   - Criada Conta Poupança {cp1.get_numero()} na Agência {agencia_obj.numero}")

    cp2 = Poupanca(numero=(prefixo_conta + 4), saldo=0.0)
    agencia_obj.lista_contas.append(cp2)
    contas_criadas_total.append(cp2)
    print(f"   - Criada Conta Poupança {cp2.get_numero()} na Agência {agencia_obj.numero}")

    # 3 Automatica
    ca1 = Automatica(saldo=0.0)
    agencia_obj.lista_contas.append(ca1)
    contas_criadas_total.append(ca1)
    print(f"   - Criada Conta Automática {ca1.get_numero()} na Agência {agencia_obj.numero}")

    ca2 = Automatica(saldo=0.0)
    agencia_obj.lista_contas.append(ca2)
    contas_criadas_total.append(ca2)
    print(f"   - Criada Conta Automática {ca2.get_numero()} na Agência {agencia_obj.numero}")

    ca3 = Automatica(saldo=0.0)
    agencia_obj.lista_contas.append(ca3)
    contas_criadas_total.append(ca3)
    print(f"   - Criada Conta Automática {ca3.get_numero()} na Agência {agencia_obj.numero}")

criar_contas_em_agencia(agencia1, 101)
criar_contas_em_agencia(agencia2, 102)

# 4. Para cada conta criada creditar 200.0
print("\nPasso 4: Creditando R$200.0 em todas as contas criadas...")
for conta_obj in contas_criadas_total:
    conta_obj.creditar(200.0)

# 5. Para cada conta criada debitar 100.0
print("\nPasso 5: Debitando R$100.0 de todas as contas criadas...")
for conta_obj in contas_criadas_total:
    conta_obj.debitar(100.0)

# 6. Juros de 5%.
print("\nPasso 6: Rendendo juros de 5% nas contas da Agência 101 (onde aplicável)...")
if agencia1:
    for conta_obj in agencia1.lista_contas:
        if isinstance(conta_obj, Poupanca): 
            taxa_juros = 0.05
            saldo_anterior = conta_obj.get_saldo()
            conta_obj.render_juros(taxa_juros)
            print(f"   - Juros de {taxa_juros*100}% rendidos na Conta Poupança {conta_obj.get_numero()}. Saldo anterior: R${saldo_anterior:.2f}, Saldo novo: R${conta_obj.get_saldo():.2f}")

# 7. Imprimir relatório
print("\nPasso 7: Imprimindo relatórios após operações iniciais...")
imprimir_relatorios_completos(banco_principal)

# 8. Remover 1 conta de cada agência
print("\nPasso 8: Removendo 1 conta de cada agência...")
if agencia1 and agencia1.lista_contas:
    conta_removida_ag1 = agencia1.lista_contas.pop(0)
    print(f"   - Removida conta {conta_removida_ag1.get_numero()} da Agência {agencia1.numero}")
if agencia2 and agencia2.lista_contas:
    conta_removida_ag2 = agencia2.lista_contas.pop(0)
    print(f"   - Removida conta {conta_removida_ag2.get_numero()} da Agência {agencia2.numero}")

# 9. Imprimir relatório
print("\nPasso 9: Imprimindo relatórios após remoção de contas...")
imprimir_relatorios_completos(banco_principal)

# 10. Remover 1 agência
print("\nPasso 10: Removendo 1 agência do banco...")
if banco_principal.lista_agencias:
    agencia_removida = banco_principal.lista_agencias.pop(0) # Remove a primeira agência da lista
    print(f"   - Removida Agência {agencia_removida.numero} do banco.")
else:
    print("   - Nenhuma agência para remover.")

# 11. Imprimir relatório final
print("\nPasso 11: Imprimindo relatório final...")
imprimir_relatorios_completos(banco_principal)