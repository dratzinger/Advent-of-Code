import unittest

from day4 import part_one, part_two

KNOWN_INPUT = [
    "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
    "byr:1937 iyr:2017 cid:147 hgt:183cm",
    "",
    "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
    "hcl:#cfa07d byr:1929",
    "",
    "hcl:#ae17e1 iyr:2013",
    "eyr:2024",
    "ecl:brn pid:760753108 byr:1931",
    "hgt:179cm",
    "",
    "hcl:#cfa07d eyr:2025 pid:166559648",
    "iyr:2011 ecl:brn hgt:59in"
]


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(2, part_one(KNOWN_INPUT))

    def test_part_2_known_input(self):
        self.assertEqual(0, part_two(KNOWN_INPUT))


if __name__ == '__main__':
    unittest.main()
