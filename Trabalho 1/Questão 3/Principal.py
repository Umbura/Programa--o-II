#Gabrielly Alves Gomes - Matrícula: 20249035386
#Iago de Sousa Aragão - Matrícula: 20249014134
#Isaac Manuel Gomes Mineiro - Matrícula: 20249014170

from banco import Banco
from agencia import Agencia
from conta import Conta, Corrente, Poupanca, Automatica

def imprimir_relatorio_completo(banco_obj, titulo_relatorio="RELATORIO DO BANCO"):
    """
    Imprime um relatório detalhado do banco, suas agências e contas.
    """
    print(f"\n--- {titulo_relatorio} ---")
    if not banco_obj:
        print("Banco não existente.")
        print("--- FIM DO RELATORIO ---")
        return

    print(f"Banco Número: {banco_obj.numero}")
    if not banco_obj.lista_agencias:
        print("  Nenhuma agência cadastrada neste banco.")
    else:
        for ag in banco_obj.lista_agencias:
            print(f"  Agência Número: {ag.numero}")
            if not ag.lista_contas:
                print("    Nenhuma conta nesta agência.")
            else:
                for cta in ag.lista_contas:
                    tipo_conta = cta.__class__.__name__
                    print(f"      Conta Número: {cta.numero} (Tipo: {tipo_conta}) - Saldo: R$ {cta.saldo:.2f}")
    print(f"--- SALDO TOTAL DO BANCO: R$ {banco_obj.saldo_total:.2f} ---")
    print("--- FIM DO RELATORIO ---\n")

def main():
    # 1. Criar um banco
    meu_banco = Banco(numero_banco="B777")
    print(f"Banco {meu_banco.numero} criado.")

    # 2. Criar 2 agências
    meu_banco.cadastrar_agencia(numero_agencia="AG001")
    meu_banco.cadastrar_agencia(numero_agencia="AG002")
    print("Agências AG001 e AG002 cadastradas no banco.")

    agencia1 = meu_banco.buscar_agencia("AG001")
    agencia2 = meu_banco.buscar_agencia("AG002")

    if not agencia1 or not agencia2:
        print("ERRO: Falha ao buscar agências recém-criadas.")
        return

    todas_as_contas_criadas = []
    contador_numero_conta = 1

    # 3. Para cada agência, criar contas
    for i, ag_atual in enumerate([agencia1, agencia2]):
        print(f"\nCriando contas para a Agência {ag_atual.numero}...")

        # 1 Conta base
        num_c = f"C{contador_numero_conta:03d}"
        ag_atual.cadastrar_conta(numero_nova_conta=num_c, saldo=0.0, tipo_conta="base")
        conta_criada = ag_atual.buscar_conta(num_c)
        if conta_criada: todas_as_contas_criadas.append(conta_criada)
        contador_numero_conta += 1
        print(f"  Conta {num_c} (base) criada.")

        num_cc = f"CC{contador_numero_conta:03d}"
        ag_atual.cadastrar_conta(numero_nova_conta=num_cc, saldo=0.0, tipo_conta="corrente")
        conta_criada = ag_atual.buscar_conta(num_cc)
        if conta_criada: todas_as_contas_criadas.append(conta_criada)
        contador_numero_conta += 1
        print(f"  Conta {num_cc} (corrente) criada com taxa padrão de 1%.")

        # 2 Contas Poupanca
        for _ in range(2):
            num_cp = f"CP{contador_numero_conta:03d}"
            ag_atual.cadastrar_conta(numero_nova_conta=num_cp, saldo=0.0, tipo_conta="poupanca")
            conta_criada = ag_atual.buscar_conta(num_cp)
            if conta_criada: todas_as_contas_criadas.append(conta_criada)
            contador_numero_conta += 1
            print(f"  Conta {num_cp} (poupanca) criada.")

        # 3 Contas Automaticas
        for _ in range(3):
            nova_conta_automatica = Automatica(saldo=0.0)
            ag_atual.adicionar_conta(nova_conta_automatica) 
            todas_as_contas_criadas.append(nova_conta_automatica)
            print(f"  Conta {nova_conta_automatica.numero} (automatica) criada.")

    # 4. Para cada conta criada creditar 200.0
    print("\nCreditando R$ 200.0 em cada conta...")
    for conta_obj in todas_as_contas_criadas:
        if hasattr(conta_obj, 'creditar'):
            conta_obj.creditar(200.0)
        else:
            print(f"  Aviso: Conta {conta_obj.numero} não possui método 'creditar'.")
    print("Créditos realizados.")

    # 5. Para cada conta criada debitar 100.0
    print("\nDebitando R$ 100.0 de cada conta...")
    for conta_obj in todas_as_contas_criadas:
        if hasattr(conta_obj, 'debitar'):
            sucesso_debito = conta_obj.debitar(100.0)
            if not sucesso_debito:
                print(f"  Falha ao debitar R$ 100.0 da conta {conta_obj.numero} (Saldo: R${conta_obj.saldo:.2f}).")
        else:
            print(f"  Aviso: Conta {conta_obj.numero} não possui método 'debitar'.")
    print("Débitos realizados.")

    imprimir_relatorio_completo(meu_banco, "RELATÓRIO APÓS CRIAÇÃO, CRÉDITOS E DÉBITOS")

    # 6. Juros de 5%.
    print(f"\nRendendo juros de 5% para contas da Agência {agencia1.numero} (se aplicável)...")
    if agencia1 and agencia1.lista_contas:
        for conta_obj in agencia1.lista_contas:
            if hasattr(conta_obj, 'render_juros'):
                try:
                    conta_obj.render_juros(0.05)
                    print(f"  Juros de 5% aplicados na conta {conta_obj.numero} ({conta_obj.__class__.__name__}). Novo Saldo: R$ {conta_obj.saldo:.2f}")
                except Exception as e:
                    print(f"  Não foi possível aplicar juros na conta {conta_obj.numero}: {e}")      
    else:
        print(f"Agência {agencia1.numero if agencia1 else 'N/A'} não possui contas ou não foi encontrada.")

    imprimir_relatorio_completo(meu_banco, "RELATÓRIO APÓS RENDIMENTO DE JUROS")

    # 7. Remover 1 conta de cada agência
    print("\nRemovendo uma conta de cada agência...")
    for ag_atual in meu_banco.lista_agencias:
        if ag_atual.lista_contas:
            conta_removida = ag_atual.lista_contas.pop(0)
            if conta_removida in todas_as_contas_criadas:
                todas_as_contas_criadas.remove(conta_removida)
            print(f"  Conta {conta_removida.numero} removida da Agência {ag_atual.numero}.")
        else:
            print(f"  Agência {ag_atual.numero} não possui contas para remover.")

    imprimir_relatorio_completo(meu_banco, "RELATÓRIO APÓS REMOÇÃO DE CONTAS")

    # 8. Remover 1 agencia
    print("\nRemovendo uma agência...")
    if meu_banco.lista_agencias:
        agencia_removida = meu_banco.lista_agencias.pop(0)
        print(f"  Agência {agencia_removida.numero} removida do banco.")
    else:
        print("  Nenhuma agência no banco para remover.")

    imprimir_relatorio_completo(meu_banco, "RELATÓRIO FINAL APÓS REMOÇÃO DE AGÊNCIA")

if __name__ == "__main__":
    main()