import random

words = [
    "python", "algorithm", "database", "function", "variable",
    "internet", "compiler", "debugging", "framework", "backend",
    "frontend", "loop", "recursion", "binary", "decimal",
    "syntax", "virtual", "storage", "network", "server",
    "router", "protocol", "firewall", "cloud", "encryption",
    "blockchain", "neural", "machine", "learning", "dataset",
    "model", "feature", "training", "accuracy", "regression",
    "tokenization", "embedding", "iteration", "repository", "version",
    "docker", "kubernetes", "terminal", "interface", "command",
    "hashing", "thread", "pointer", "kernel", "cache"
]

word = random.choice(words)
n = len(word)
d = ['_']*n
attempts = 8
while attempts > 0 and '_' in d:
    print(' '.join(d))
    guess = input("Enter the letter: ").lower()[0]
    if guess in word:
        for i,w in enumerate(word):
            if(w == guess):
                d[i] = w
    else:
        attempts -= 1
        print(f"Nah! {attempts} left!")
    
if '_' in d:
    print(f"Better Luck next time! The word was {word}")
else:
    print("Well Done!")
