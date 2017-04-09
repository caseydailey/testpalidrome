class Palindrome():


    def is_palindrome(self, source_string):
        '''check a string to see if it the same when reversed
                arg--string
                returns--boolean
        '''
        if not isinstance(source_string, str):
            return False #if not string, return false

        if len(source_string) < 3:
            return False #must be at least 3 characters

        try:
            reverse_string = source_string[::-1]
            #print(reverse_string)
            if reverse_string == source_string:
                return True
            else:
                return False
        except TypeError:
            return False #check for type error