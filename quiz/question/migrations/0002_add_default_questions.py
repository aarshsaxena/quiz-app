from django.db import migrations

def add_default_questions(apps, schema_editor):
    Question = apps.get_model('question', 'Question')
    questions = [
        {"text": "What is the capital of France?", 
     "option_a": "Berlin", "option_b": "Madrid", "option_c": "Paris", "option_d": "Rome", "correct_option": "C"},
    {"text": "Which planet is known as the Red Planet?", 
     "option_a": "Earth", "option_b": "Mars", "option_c": "Jupiter", "option_d": "Venus", "correct_option": "B"},
    {"text": "Who wrote 'Romeo and Juliet'?", 
     "option_a": "William Shakespeare", "option_b": "Charles Dickens", "option_c": "Mark Twain", "option_d": "Leo Tolstoy", "correct_option": "A"},
    {"text": "What is the largest mammal?", 
     "option_a": "Elephant", "option_b": "Blue Whale", "option_c": "Giraffe", "option_d": "Polar Bear", "correct_option": "B"},
    {"text": "What is the smallest prime number?", 
     "option_a": "0", "option_b": "1", "option_c": "2", "option_d": "3", "correct_option": "C"},
    {"text": "What is H2O commonly known as?", 
     "option_a": "Hydrogen Peroxide", "option_b": "Oxygen", "option_c": "Water", "option_d": "Salt", "correct_option": "C"},
    {"text": "What is the capital city of Japan?", 
     "option_a": "Seoul", "option_b": "Tokyo", "option_c": "Beijing", "option_d": "Bangkok", "correct_option": "B"},
    {"text": "Who discovered gravity?", 
     "option_a": "Isaac Newton", "option_b": "Albert Einstein", "option_c": "Galileo Galilei", "option_d": "Marie Curie", "correct_option": "A"},
    {"text": "Which gas is most abundant in Earth's atmosphere?", 
     "option_a": "Oxygen", "option_b": "Carbon Dioxide", "option_c": "Nitrogen", "option_d": "Helium", "correct_option": "C"},
    {"text": "How many continents are there on Earth?", 
     "option_a": "5", "option_b": "6", "option_c": "7", "option_d": "8", "correct_option": "C"},
    {"text": "What is the boiling point of water at sea level?", 
     "option_a": "100°F", "option_b": "100°C", "option_c": "212°F", "option_d": "Both B and C", "correct_option": "D"},
    {"text": "Which is the largest planet in our solar system?", 
     "option_a": "Earth", "option_b": "Mars", "option_c": "Jupiter", "option_d": "Saturn", "correct_option": "C"},
    {"text": "What is the chemical symbol for gold?", 
     "option_a": "Au", "option_b": "Ag", "option_c": "Gd", "option_d": "Go", "correct_option": "A"},
    {"text": "Who painted the Mona Lisa?", 
     "option_a": "Leonardo da Vinci", "option_b": "Vincent van Gogh", "option_c": "Pablo Picasso", "option_d": "Claude Monet", "correct_option": "A"},
    {"text": "What is the hardest natural substance?", 
     "option_a": "Gold", "option_b": "Diamond", "option_c": "Platinum", "option_d": "Iron", "correct_option": "B"},
    {"text": "What is the speed of light?", 
     "option_a": "300,000 km/s", "option_b": "150,000 km/s", "option_c": "300,000 m/s", "option_d": "150,000 m/s", "correct_option": "A"},
    {"text": "What is the square root of 64?", 
     "option_a": "6", "option_b": "7", "option_c": "8", "option_d": "9", "correct_option": "C"},
    {"text": "Which ocean is the largest?", 
     "option_a": "Atlantic", "option_b": "Indian", "option_c": "Arctic", "option_d": "Pacific", "correct_option": "D"},
    {"text": "What is the freezing point of water?", 
     "option_a": "0°C", "option_b": "32°F", "option_c": "Both A and B", "option_d": "None of these", "correct_option": "C"},
    {"text": "Who is known as the Father of Computers?", 
     "option_a": "Alan Turing", "option_b": "Charles Babbage", "option_c": "John von Neumann", "option_d": "Tim Berners-Lee", "correct_option": "B"},
    ]
    for q in questions:
        Question.objects.create(
            text=q['text'],
            option_a=q['option_a'],
            option_b=q['option_b'],
            option_c=q['option_c'],
            option_d=q['option_d'],
            correct_option=q['correct_option'],
        )

class Migration(migrations.Migration):
    dependencies = [
        ('question', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_default_questions),
    ]
