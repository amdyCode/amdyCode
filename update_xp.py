import re
from datetime import datetime

# Par défaut, mis à aujourd'hui
START_DATE = datetime(2026, 8, 30)

def main():
    today = datetime.now()
    delta = today - START_DATE
    days_passed = delta.days

    # 1 an = 365 jours. On calcule les années et les jours en plus.
    additional_years = days_passed // 365
    remaining_days = days_passed % 365

    total_years = 2 + additional_years

    # Construction de la phrase
    if remaining_days > 0:
        xp_text = f"🔭 With {total_years} years and {remaining_days} days of experience, I build smooth and performant applications using Flutter and Angular."
    else:
        xp_text = f"🔭 With {total_years} years of experience, I build smooth and performant applications using Flutter and Angular."

    # Lecture du README
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Remplacement en utilisant une expression régulière pour trouver le texte entre les marqueurs
    new_readme = re.sub(
        r'(?<=<!-- experience_start -->\n).*?(?=\n<!-- experience_end -->)',
        xp_text,
        readme_content,
        flags=re.DOTALL
    )

    # Sauvegarde
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)
        
    print("README.md mis à jour avec succès !")

if __name__ == "__main__":
    main()
