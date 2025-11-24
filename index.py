def main():
    print("Hello World!")
    try:
        from PIL import Image
        print("Pillow is working!")
    except ImportError:
        print("Pillow not found!")

if __name__ == "__main__":
    main()