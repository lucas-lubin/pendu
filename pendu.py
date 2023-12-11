import pygame
import random
import sys

pygame.init()

# Paramètres du jeu
largeur_fenetre = 800
hauteur_fenetre = 600
couleur_fond = (255, 255, 255)
couleur_texte = (0, 0, 0)
taille_police = 40
liste_mots = ["python", "ROSE", "police", "ours", "arbre", "maison", "kfc", "hache", "russe", "Poutine"]

def choisir_mot():
    return random.choice(liste_mots)

# Fonction pour afficher le mot masqué
def afficher_mot_masque(mot, lettres_trouvees):
    mot_affiche = ""
    for lettre in mot:
        if lettre in lettres_trouvees:
            mot_affiche += lettre + " "
        else:
            mot_affiche += "_ "
    return mot_affiche.strip()

# Fonction principale du jeu
def jeu_pendu():
    mot_a_deviner = choisir_mot()
    lettres_trouvees = set()
    tentatives_restantes = 6

    # Paramètres de la fenêtre Pygame
    fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
    pygame.display.set_caption("Jeu du Pendu")

    # Boucle principale du jeu
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key >= 97 and event.key <= 122: 
                    if lettre not in lettres_trouvees:
                        lettres_trouvees.add(lettre)
                        if lettre not in mot_a_deviner:
                            tentatives_restantes -= 1

        fenetre.fill(couleur_fond)

  
        mot_affiche = afficher_mot_masque(mot_a_deviner, lettres_trouvees)
        font = pygame.font.Font(None, taille_police)
        text = font.render(mot_affiche, True, couleur_texte)
        fenetre.blit(text, (largeur_fenetre // 2 - text.get_width() // 2, hauteur_fenetre // 2 - text.get_height() // 2))

        # Dessiner le pendu
        pygame.draw.line(fenetre, couleur_texte, (100, 500), (100, 100), 2)  # Poteau vertical
        pygame.draw.line(fenetre, couleur_texte, (100, 100), (400, 100), 2)  # Barre horizontale supérieure

        if tentatives_restantes < 6:
            pygame.draw.circle(fenetre, couleur_texte, (400, 150), 50, 2)  # Tête

        if tentatives_restantes < 5:
            pygame.draw.line(fenetre, couleur_texte, (400, 200), (400, 350), 2)  # Corps

        if tentatives_restantes < 4:
            pygame.draw.line(fenetre, couleur_texte, (400, 250), (350, 200), 2)  # Bras gauche

        if tentatives_restantes < 3:
            pygame.draw.line(fenetre, couleur_texte, (400, 250), (450, 200), 2)  # Bras droit

        if tentatives_restantes < 2:
            pygame.draw.line(fenetre, couleur_texte, (400, 350), (350, 400), 2)  # Jambe gauche

        if tentatives_restantes < 1:
            pygame.draw.line(fenetre, couleur_texte, (400, 350), (450, 400), 2)  # Jambe droite

        pygame.display.flip()

        # Vérification de la fin du jeu
        if "_" not in mot_affiche or tentatives_restantes == 0:
            pygame.time.delay(2000)  # Pause de 2 secondes avant de quitter
            return

# Programme principal
while True:
    choix = input("Voulez-vous jouer (J) ou insérer un mot (I) dans le fichier 'mots.txt'? ").lower()

    if choix == "j":
        jeu_pendu()
    elif choix == "i":
        nouveau_mot = input("Entrez un nouveau mot : ")
        with open("mots.txt", "a") as fichier:
            fichier.write(nouveau_mot + "\n")
    else:
        print("Choix invalide. Veuillez entrer 'J' pour jouer ou 'I' pour insérer un mot.")