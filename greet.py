def greet(name: str):
    print(
        f"hello, {name}, men seni bundan keyin ko'rmasam kerak deb \
                o'ylagan edim, lekin unday emas shekilli. Nimalar\
                bilan bandsan? Bu 80 qatordan oshdimi"
    )


def main():
    for name in "James", "Subscriber", "other":
        greet(name)


if __name__ == "__main__":
    main()
