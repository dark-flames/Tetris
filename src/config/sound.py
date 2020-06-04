import pyxel


def play_sound():
    pyxel.sound(0).set(
        "E3E3E3E3 D3D3D3D3 C3C3C3C3 D3D3D3D3",
        "S",
        "6",
        "FFFF FFFF FFFF FFFF",
        60
    )
    pyxel.play(0, 0, loop=True)

    pyxel.sound(1).set(
        "E1E1E1E1 D1D1D1D1 C1C1C1C1 D1D1D1D1",
        "S",
        "6",
        "FFFF FFFF FFFF FFFF",
        60
    )
    pyxel.play(1, 1, loop=True)

    pyxel.sound(2).set(
        "C2D2E2F2G2A2B2C3",
        "S",
        "6",
        "FFFF FFFF ",
        60
    )
    pyxel.play(2, 2, loop=True)

