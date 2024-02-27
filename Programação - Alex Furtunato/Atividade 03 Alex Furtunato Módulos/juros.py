def juroscompostos(principal, periodo, juros): #Recebendo os dados como argumentos Ex.: juroscomposto(argv1,argv2,argv3)
    montante = principal * ((1 + juros/100)**periodo)
    juros = montante-principal

    return print("O montante final foi de: " + str(f"R$ {montante:.2f}")+".\nOs juros foram de: "+ str("R$ {juros:.2f}"))

# if __name__=='__main__':
#     main()