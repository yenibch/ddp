import math

def tambah(bil1, bil2):
    hasil= bil1 + bil2
    print("hasil tambah dari", bil1, "+", bil2, "=", hasil)


def kurang(bil1, bil2):
    hasil= bil1 - bil2
    print("hasil kurang dari", bil1, "-", bil2, "=", hasil)


def kali(bil1, bil2):
    hasil= bil1 * bil2
    print("hasil kali dari", bil1, "*", bil2, "=", hasil)


def bagi(bil1, bil2):
    hasil= bil1 / bil2
    print("hasil bagi dari", bil1, "/", bil2, "=", hasil)


def pangkat(bil1, bil2):
    hasil= math.pow(bil1, bil2)
    print("hasil pangkat dari", bil1, "^", bil2, "=", hasil)