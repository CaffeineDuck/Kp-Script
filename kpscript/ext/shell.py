def shell():
    lexer = KpLexer()
    parser = KpParser()
    print(f"KpScript: {VERSION}")
    while True:
        try:
            text = input("KpScript > ")
        except EOFError:
            break
        tree = parser.parse(lexer.tokenize(text))
        evaluate(tree)