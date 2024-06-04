def number_to_words(n):
    if n == 0:
        return "zero"
    
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]

    def _convert_hundred(num):
        word = ""
        if num >= 100:
            word += units[num // 100] + " hundred"
            num %= 100
            if num > 0:
                word += " and "
        if 10 <= num < 20:
            word += teens[num - 10]
        else:
            if num >= 20:
                word += tens[num // 10]
                num %= 10
                if num > 0:
                    word += "-" + units[num]
            else:
                word += units[num]
        return word.strip()
    
    words = ""
    if n >= 1000:
        words += units[n // 1000] + " " + thousands[1]
        n %= 1000
        if n > 0:
            words += " "
    if n > 0:
        words += _convert_hundred(n)
    
    return words.strip()

def count_letters_in_words(words):
    return sum(1 for char in words if char.isalpha())

if __name__ == "__main__":
    total_letters = 0
    for i in range(1, 1001):
        words = number_to_words(i)
        letters_count = count_letters_in_words(words)
        total_letters += letters_count
    
    print(f"The total number of letters used from 1 to 1000 is {total_letters}")
