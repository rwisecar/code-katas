"""An implementation of the string pyramid kata."""


def watch_pyramid_from_the_side(characters):
    """Show view of pyramid from the side."""
    if characters:
        chars = characters[::-1]
        row = 1
        spaces = len(chars) - 1
        pyramid = []
        while chars:
            pyramid.append((" " * spaces) + chars[0] * row + (" " * spaces))
            row += 2
            spaces -= 1
            chars = chars[1:]
        return "\n".join(pyramid)
    return characters


def watch_pyramid_from_above(characters):
    """Show view of pyramid from the top."""
    if characters:
        pyramid = []
        length = len(characters)
        for i in range(length):
            pyramid.append(
                characters[:i] + characters[i] * len(characters[i:]))
        for i in range(length):
            pyramid[i] += pyramid[i][-2::-1]
        for i in range(length - 2, -1, -1):
            pyramid.append(pyramid[i])
        return "\n".join(pyramid)
    return characters


def count_visible_characters_of_the_pyramid(characters):
    if characters:
        width = 2 * len(characters) - 1
        return width ** 2
    return -1


def count_all_characters_of_the_pyramid(characters):
    if characters:
        chars = characters
        sum = 0
        while chars:
            sum += (2 * len(chars) - 1) ** 2
            chars = chars[1:]
        return sum
    return -1
