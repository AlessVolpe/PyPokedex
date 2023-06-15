class data_cleaning:
    def str_bracket(word):
        '''Add brackets around second term'''
        word_bychar = [char for char in word]
        for char_ind in range(1, len(word_bychar)):
            if word_bychar[char_ind].isupper():
                word_bychar[char_ind] = ' ' + word_bychar[char_ind]
        fin_list = ''.join(word_bychar).split(' ')
        length = len(fin_list)
        if length>1:
            fin_list.insert(1,' (')
            fin_list.append(')')
        return ''.join(fin_list)

        
    def str_break(word):
        '''Break strings at upper case'''
        word_bychar = [char for char in word]
        for char_ind in range(1, len(word_bychar)):
            if word_bychar[char_ind].isupper():
                word_bychar[char_ind] = '' + word_bychar[char_ind]
        fin_list = ''.join(word_bychar).split(' ')
        if fin_list[1] == '':
            return [fin_list[0]]
        else:
            return fin_list