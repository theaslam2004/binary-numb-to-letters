import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

last_output = ""


def binary_to_letter(binary):
    # Remove any spaces from the binary string
    binary = binary.replace(" ", "")

    # Check if the binary string length is a multiple of 8
    if len(binary) % 8 != 0:
        return "Invalid binary number."

    # Split the binary string into 8-bit chunks
    chunks = [binary[i:i + 8] for i in range(0, len(binary), 8)]
    # Convert each 8-bit chunk to its corresponding character
    letters = [chr(int(chunk, 2)) for chunk in chunks]
    # Join the characters to form the resulting string
    return ''.join(letters)


def letter_to_binary(letter):
    # Convert character to decimal
    decimal = ord(letter)
    # Convert decimal to binary
    binary = bin(decimal)[2:].zfill(8)  # Ensure 8 bits
    return binary


def string_to_binary(string):
    binary_result = ''
    for letter in string:
        binary_result += letter_to_binary(letter)
    return binary_result


def speak(text):
    global last_output
    last_output = text

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Speak the text
    engine.say(text)
    engine.runAndWait()


def main():
    speak("hi")
    speak("This is the Binary number to letters Converter")
    print("Binary Converter")
    print("================")
    while True:
        print("\nMenu:")
        print("1. Convert binary number to letter")
        print("2. Convert string to binary number")
        print("3. Speak the last output")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            binary = input("Enter a binary number: ")
            letter = binary_to_letter(binary)
            print("Corresponding letter(s):", letter)
            speak("The corresponding letter is " + letter)
        elif choice == '2':
            string = input("Enter a string: ")
            binary = string_to_binary(string)
            print("Binary representation:", binary)
            speak("The binary representation is " + binary)
        elif choice == '3':
            if last_output:
                speak("Speaking the last output: " + last_output)
            else:
                print("No previous output to speak.")
        elif choice == '4':
            print("Exiting...👋")
            speak("bye bye")
            break
        else:
            print("Invalid choice. Please enter a valid option.")



if __name__ == "__main__":
    main()
