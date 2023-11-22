import random

def reviserTables(n_questions=10, n_tables=10):
    bonnesReponses = 0
    totalQuestions = 0
    for i in range(n_questions):
        a = random.randint(0, n_tables)
        b = random.randint(0, n_tables)
        reponseUtilisateur = int(input(f"Combien font {a} * {b} ? ")) #on formate la str
        if reponseUtilisateur == a * b:
            bonnesReponses += 1
        else:
            bonnesReponses -= 1
        totalQuestions += 1
    scoreFinal = bonnesReponses if bonnesReponses >= 0 else 0
    reussi = scoreFinal >= (totalQuestions / 2)
    return reussi, scoreFinal

reviserTables()