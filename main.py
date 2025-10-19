def main():
    name = "toto"
    print(name)
    with open('/Users/Soufiane/Downloads/global_finance_data.csv', encoding="utf8") as f:
        for line in f:
            print(line)
    


if __name__ == "__main__":
    main()
