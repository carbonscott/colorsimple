# colorsimple/__init__.py

version = "0.1.3"

def rgb_to_hex(r, g, b):
    ''' Convert rgb to hex code.
        r (red)  : [0, 255]
        g (green): [0, 255]
        b (blue) : [0, 255]
    '''
    # Exit the program upon illegal input
    assert 0 <= r <= 255, f"r (red) value out of range (0-255)."
    assert 0 <= g <= 255, f"g (green) value out of range (0-255)."
    assert 0 <= b <= 255, f"b (blue) value out of range (0-255)."

    # Define the dictionary for hex code...
    hex_dict = { 0  : "0", 1  : "1", 2  : "2", 3  : "3", 4  : "4",
                 5  : "5", 6  : "6", 7  : "7", 8  : "8", 9  : "9",
                 10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 
                 15 : "F" }
    len_hex = 16

    hex_res = ""
    for i in (r, g, b):
        # Obtain the quotient and remainder...
        q, r = i // len_hex, i % len_hex

        # Find hex code...
        hex_res += f"{hex_dict[q]}{hex_dict[r]}"

    return hex_res




def hsv_to_hex(h, s, v):
    ''' Convert hsv to hex code.
        h (hue)       : [0, 360]
        s (saturation): [0, 100]
        v (value)     : [0, 100]
    '''
    from colorsys import hsv_to_rgb

    # Exit the program upon illegal input
    assert 0 <= h <= 360, f"h (hue) value out of range (0-360)."
    assert 0 <= s <= 100, f"s (saturation) value out of range (0-100)."
    assert 0 <= v <= 100, f"v (value) value out of range (0-100)."

    # Convert hsv to rgb...
    h /= 360
    s /= 100
    v /= 100
    r, g, b = hsv_to_rgb(h, s, v)
    r, g, b = ( round(i * 255) for i in (r, g, b) )

    # Convert rgb to hex...
    hex_res = rgb_to_hex(r, g, b)

    return hex_res




def hex_to_rgb(h):
    ''' Reference: https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python

        e.g. hex_to_rgb('ffffff') returns (255, 255, 255)
    '''
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))




def color_species(items, s = 50, v = 100, hexsym = '#', b = 0, e = 360, clockwise = False):
    ''' 
    '''
    assert len(set(items)) == len(items), \
        "Duplicate item is not allowed in the input."

    # Get number of colors...
    num = len(items)

    # Divide the color palette...
    div = abs(int((e - b) / num))

    # Assign color to each item...
    # Hooray, dictionary follows insertion order in Python3.6 or later
    # Refer to https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6
    d = 1.0    # Couterclockwise by default
    if clockwise: d *= -1.0
    color_dict = {}
    for i, item in enumerate(items): 
        h = b + d * i * div
        while h < 0: h += 360
        while h > 360: h -= 360
        color_dict[item] = hexsym + hsv_to_hex(h, s, v)

    return color_dict




def color_table(color_dict):
    import GnuplotPy3
    gp = GnuplotPy3.GnuplotPy3()

    gp( "set terminal postscript eps  size 3.5, 2.62 \\")
    gp( "                             enhanced color \\")
    gp( "                             font 'Helvetica,14' \\")
    gp( "                             linewidth 2")
    gp(f"set output 'color_table.eps'")
    gp("set xrange [1:2]")
    gp("set yrange [1:2]")
    gp("unset border")
    gp("unset xtics")
    gp("unset ytics")

    gp("plot \\")
    for n, c in color_dict.items():
        gp(f"'-' using 1:2 with points pointtype 7 linecolor rgb '{c}' title '{n}',\\")
    gp("")

    for i in range(len(color_dict)):
        gp(f"0 0")
        gp( "e")
    gp("exit")

    return None

