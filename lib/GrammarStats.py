class GrammarStats:
    def __init__(self):
        self._texts_checked_so_far = 0
        self._texts_that_passed_check_method = 0

    def check(self, text: str):
        '''Checks whether a text starts with a capital letter and has appropriate end-puncutuation'''
        self._texts_checked_so_far += 1
        if text == "" or not isinstance(text, str):
            raise Exception("Text must be a string and cannot be empty.")
        elif text[0].isupper() and text[-1] in ".!?":
            self._texts_that_passed_check_method += 1
            return True
        else:
            return False

    def percentage_good(self):
        '''Returns the percentage of texts checked so far that passed check(), as an integer'''
        percentage = round((self._texts_that_passed_check_method / self._texts_checked_so_far) * 100)
        return percentage
