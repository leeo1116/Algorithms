def decode_ways(s):
    """
    Find out how many possible ways to decode s with rule "A" --> 1, "B" --> 2, ... "Z" --> 26
    :param s: an input string containing characters from '0' to '6' 
    :return: total number decode ways
    """
    # Construct an array with length = len(s) + 1 to account for the case s = ""
    # decodes[i] denotes the number of decode ways of substring from s[0] to s[i - 1]
    decodes = [0] * (len(s) + 1)
    decodes[0] = 1  # Notice that decodes[i] = decodes[i - 1] = 1 when i = 1
    for i in range(1, len(s) + 1):
        if s[i - 1] != '0':
            decodes[i] = decodes[i - 1]
        if i != 1 and "09" < s[i - 2:i] < "27":  # string comparison
            decodes[i] += decodes[i - 2]
    return decodes[len(s)]


