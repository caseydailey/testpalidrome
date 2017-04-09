class Palindrome():

    def is_palindrome(self, source_string):
        if not isinstance(source_string, str):
            return False

        if len(source_string) < 3:
            return False

        try:
            reverse_string = source_string[::-1]
            print(reverse_string)
            if reverse_string == source_string:
                return True
            else:
                return False
        except TypeError:
            return False