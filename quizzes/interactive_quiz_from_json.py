import time
import json
import os
import random

class PythonQuiz:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.start_time = None
        
    def start_quiz(self, quiz_name):
        print(f"\n{'='*50}")
        print(f"Welcome to {quiz_name}")
        print(f"{'='*50}")
        print("Instructions:")
        print("- Answer each question by typing a, b, c, or d")
        print("- For True/False questions, type 'a' for True and 'b' for False")
        print("- Type 'quit' to exit at any time")
        print("- Good luck!\n")
        
        self.start_time = time.time()
        
    def ask_question(self, question_data):
        self.total_questions += 1
        print(f"Question {self.total_questions}:")
        
        # Show section info if available (for comprehensive quiz)
        if 'section' in question_data:
            print(f"📚 Section: {question_data['section']}")
        
        # Display question text
        print(question_data["question"])
        
        # Display code if present
        if question_data.get("code"):
            code_display = question_data["code"].replace("\\n", "\n")
            print(code_display)
        
        print()
        
        # Handle both old and new option formats
        options = question_data["options"]
        if isinstance(options, dict):
            # Old format: {"a": "option1", "b": "option2", ...}
            for key, value in options.items():
                if value:  # Only show non-empty options
                    print(f"{key}) {value}")
        elif isinstance(options, list):
            # New format: ["option1", "option2", "option3", "option4"]
            option_keys = ['a', 'b', 'c', 'd']
            for i, option in enumerate(options):
                if i < len(option_keys) and option:
                    print(f"{option_keys[i]}) {option}")
        
        while True:
            answer = input("\nYour answer: ").lower().strip()
            
            if answer in ["quit", "exit"]:
                return False
                
            if answer in ["a", "b", "c", "d"]:
                correct_answer = question_data["correct_answer"]
                
                # Handle both string and integer correct answers
                if isinstance(correct_answer, str):
                    correct_answer_key = correct_answer.lower()
                elif isinstance(correct_answer, int):
                    # Convert 0-based index to letter (0->a, 1->b, etc.)
                    option_keys = ['a', 'b', 'c', 'd']
                    correct_answer_key = option_keys[correct_answer] if correct_answer < len(option_keys) else 'a'
                else:
                    correct_answer_key = 'a'  # fallback
                
                if answer == correct_answer_key:
                    print("✅ Correct!")
                    self.score += 1
                else:
                    print(f"❌ Incorrect. The correct answer is {correct_answer_key.upper()}")
                    print(f"Explanation: {question_data['explanation']}")
                print()
                return True
            else:
                print("Please enter a, b, c, d, or 'quit'")
    
    def end_quiz(self):
        end_time = time.time()

        if self.start_time is None:
            print("Error: Quiz was not properly started!")
            return

        duration = int(end_time - self.start_time)
        
        print(f"\n{'='*80}")
        print("QUIZ COMPLETED!")
        print(f"{'='*80}")
        print(f"Score: {self.score}/{self.total_questions}")
        
        if self.total_questions > 0:
            percentage = (self.score/self.total_questions)*100
            print(f"Percentage: {percentage:.1f}%")
            
            if percentage >= 100:
                grade = "A++ - Perfect Score!"
            elif percentage >= 95:
                grade = "A+ - Outstanding!"
            elif percentage >= 90:
                grade = "A - Excellent!"
            elif percentage >= 80:
                grade = "B - Good!"
            elif percentage >= 70:
                grade = "C - Satisfactory"
            elif percentage >= 60:
                grade = "D - Needs Improvement"
            else:
                grade = "F - Needs Significant Review"
                
            print(f"Grade: {grade}")
        
        print(f"Time taken: {duration//60}:{duration%60:02d}")
        print(f"{'='*80}")
        return "completed"

    def quit_quiz(self):
        end_time = time.time()

        if self.start_time is None:
            print("Error: Quiz was not properly started!")
            return "quit"

        duration = int(end_time - self.start_time)

        print(f"\n{'='*80}")
        print("Quiz ended early.")
        print(f"{'='*80}")
        print(f"Score so far: {self.score}/{self.total_questions}")
        print(f"Time taken: {duration//60}:{duration%60:02d}")
        print(f"{'='*80}")
        return "quit"


class JSONQuizLoader:
    @staticmethod
    def load_quiz_from_json(file_path):
        """Load quiz data from JSON file"""
        if not os.path.exists(file_path):
            print(f"Error: Quiz file not found: {file_path}")
            return None
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                quiz_data = json.load(file)
            return quiz_data
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON file: {e}")
            return None
        except Exception as e:
            print(f"Error loading quiz file: {e}")
            return None
    
    @staticmethod
    def extract_questions(quiz_data):
        """Extract all questions from quiz data - handles both old and new JSON formats"""
        all_questions = []
        
        if not quiz_data:
            return all_questions
        
        # New format: direct questions array
        if 'questions' in quiz_data:
            return quiz_data['questions']
        
        # Old format: sections with nested questions
        if 'sections' in quiz_data:
            for section in quiz_data['sections']:
                if 'questions' in section:
                    all_questions.extend(section['questions'])
        
        return all_questions
    
    @staticmethod
    def select_questions(all_questions, num_questions, mode="random"):
        """Select a subset of questions based on mode"""
        if not all_questions:
            return []
        
        if num_questions >= len(all_questions):
            return all_questions
        
        if mode == "random":
            return random.sample(all_questions, num_questions)
        elif mode == "first":
            return all_questions[:num_questions]
        else:
            return all_questions[:num_questions]


def run_json_quiz(file_path, quiz_name, num_questions=None, mode="random"):
    """Run quiz from JSON file with specified number of questions"""
    
    # Load quiz data
    quiz_data = JSONQuizLoader.load_quiz_from_json(file_path)
    if not quiz_data:
        return
    
    # Extract all questions
    all_questions = JSONQuizLoader.extract_questions(quiz_data)
    if not all_questions:
        print("No questions found in the quiz file.")
        return

    total_questions = len(all_questions)
    
    # Select questions based on mode
    if num_questions:
        selected_questions = JSONQuizLoader.select_questions(all_questions, num_questions, mode)
        actual_quiz_name = f"{quiz_name} ({len(selected_questions)} Questions)"
    else:
        selected_questions = all_questions
        actual_quiz_name = f"{quiz_name} (Complete - {total_questions} Questions)"
    
    # Run the quiz
    quiz = PythonQuiz()
    quiz.start_quiz(actual_quiz_name)
    
    quit_early = False
    for question_data in selected_questions:
        if not quiz.ask_question(question_data):
            quit_early = True
            break
    
    if quit_early:
        return quiz.quit_quiz()
    return quiz.end_quiz()


def create_quiz_mode_selector(section_name, file_path):
    """Generic quiz mode selector for quiz.JSON"""
    print(f"\n🎯 {section_name}")
    print("="*80)
    print("Choose your quiz mode:")
    print("1. Flash Quiz (5 questions) - Quick review")
    print("2. Practice Quiz (10 questions) - Focused practice") 
    print("3. Standard Quiz (15 questions) - Balanced review")
    print("4. In-Depth Quiz (All questions) - Complete assessment")
    print("="*80)
    
    quiz_modes = {
        "1": (5, "Flash Quiz"),
        "2": (10, "Practice Quiz"),
        "3": (15, "Standard Quiz"),
        "4": (None, "In-Depth Quiz")  # None means all questions
    }

    while True:
        choice = input("Select mode (1-4): ").strip()

        if choice.lower() in ["quit", "exit"]:
            return "quit"
        
        if choice in quiz_modes:
            num_questions, mode_name = quiz_modes[choice]
            quiz_name = f"{section_name} - {mode_name}"
            return run_json_quiz(file_path, quiz_name, num_questions, "random")
        else:
            print("❌ Invalid choice! Please select 1-4.")


SECTION_QUIZZES = {
    "1": ("./section1_basic_syntax_quiz.json", "Section 1: Basic Syntax Quiz"),
    "2": ("./section2_data_structures_quiz.json", "Section 2: Data Structures Quiz"),
    "3": ("./section3_flow_control_quiz.json", "Section 3: Flow Control Quiz"),
    "4": ("./section4_functions_quiz.json", "Section 4: Functions Quiz"),
    "5": ("./section5_oop_quiz.json", "Section 5: Object-Oriented Programming Quiz"),
    "6": ("./section6_modules_libraries_quiz.json", "Section 6: Modules and Libraries Quiz"),
}


def run_comprehensive_quiz(sections, questions_per_section, mode_name):
    """Load questions from multiple sections and run comprehensive quiz"""
    import random
    
    print(f"\n🚀 Starting {mode_name}")
    print("Loading questions from all sections...")
    
    all_questions = []
    
    # Load questions from each section
    for file_path, section_name in sections:
        try:
            quiz_data = JSONQuizLoader.load_quiz_from_json(file_path)
            if not quiz_data:
                print(f"⚠️  Warning: Could not load {section_name}")
                continue
                
            section_questions = JSONQuizLoader.extract_questions(quiz_data)
            
            if questions_per_section is None:
                # Use all questions for complete assessment
                selected_questions = section_questions
            else:
                # Randomly sample specified number of questions
                selected_questions = random.sample(
                    section_questions, 
                    min(questions_per_section, len(section_questions))
                )
            
            # Add section info to each question for context
            for q in selected_questions:
                q['section'] = section_name
            
            all_questions.extend(selected_questions)
            print(f"✓ Loaded {len(selected_questions)} questions from {section_name}")
            
        except Exception as e:
            print(f"⚠️  Warning: Could not load {section_name}: {e}")
    
    if not all_questions:
        print("❌ No questions loaded! Please check the quiz files.")
        return
    
    # Shuffle all questions for random order
    random.shuffle(all_questions)
    
    print(f"\n📊 Total questions loaded: {len(all_questions)}")
    print("Questions will be presented in random order from all sections.")
    
    # Run the quiz using the same pattern as existing code
    quiz = PythonQuiz()
    actual_quiz_name = f"{mode_name} ({len(all_questions)} Questions)"
    quiz.start_quiz(actual_quiz_name)
    
    quit_early = False
    for question_data in all_questions:
        if not quiz.ask_question(question_data):
            quit_early = True
            break
    
    if quit_early:
        return quiz.quit_quiz()
    return quiz.end_quiz()


def final_quiz():
    """Final Comprehensive Quiz - Combines questions from all sections"""
    print()
    print()
    print()
    print("\n🎯 Final Comprehensive Quiz")
    print("="*80)
    print("Choose your comprehensive quiz mode:")
    print("1. Quick Review (30 questions) - 5 from each section")
    print("2. Standard Review (60 questions) - 10 from each section") 
    print("3. Thorough Review (90 questions) - 15 from each section")
    print("4. Complete Assessment (All 180 questions) - All questions from all sections")
    print("="*80)
    
    
    # Define section files and names
    sections = [
        ("./section1_basic_syntax_quiz.json", "Basic Syntax"),
        ("./section2_data_structures_quiz.json", "Data Structures"),
        ("./section3_flow_control_quiz.json", "Flow Control"),
        ("./section4_functions_quiz.json", "Functions"),
        ("./section5_oop_quiz.json", "Object-Oriented Programming"),
        ("./section6_modules_libraries_quiz.json", "Modules & Libraries")
    ]
    
    mode_configs = {
        "1": (5, "Quick Review"),
        "2": (10, "Standard Review"),
        "3": (15, "Thorough Review"),
        "4": (None, "Complete Assessment")  # None means all questions
    }

    while True:
        choice = input("Select mode (1-4): ").strip()

        if choice.lower() in ["quit", "exit"]:
            return "quit"

        if choice in mode_configs:
            questions_per_section, mode_name = mode_configs[choice]
            return run_comprehensive_quiz(sections, questions_per_section, mode_name)
        else:
            print("❌ Invalid choice! Please select 1-4.")


if __name__ == "__main__":
    print()
    print()
    print()
    print("Welcome to the Python A-to-Z Interactive Quiz System!")
    print("🐍 Python A-to-Z Quiz System 🐍")
    print("="*80)
    print("1. Section 1: Basic Syntax")
    print("2. Section 2: Data Structures")
    print("3. Section 3: Flow Control")
    print("4. Section 4: Functions")
    print("5. Section 5: OOP")
    print("6. Section 6: Modules & Libraries")
    print("7. Final Comprehensive Quiz")
    print("="*80)
    
    while True:
        choice = input("Choose a section (1-7): ").strip()

        if choice.lower() in ["quit", "exit"]:
            print("Exiting quiz. See you next time!")
            break

        if choice in SECTION_QUIZZES:
            file_path, section_name = SECTION_QUIZZES[choice]
            result = create_quiz_mode_selector(section_name, file_path)
        elif choice == "7":
            result = final_quiz()
        else:
            print("❌ Invalid choice! Please select 1-7.")
            continue

        if result == "completed":
            break
        if result in ["quit", "exit"]:
            print("Exiting quiz. See you next time!")
            break