import unittest

from day4 import *

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

INVALID_DATA = [
    "eyr:1972 cid:100",
    "hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926",
    "",
    "iyr:2019",
    "hcl:#602927 eyr:1967 hgt:170cm",
    "ecl:grn pid:012533040 byr:1946",
    "",
    "hcl:dab227 iyr:2012",
    "ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277",
    "",
    "hgt:59cm ecl:zzz",
    "eyr:2038 hcl:74454a iyr:2023",
    "pid:3556412378 byr:2007"
]

VALID_DATA = [
    "pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980",
    "hcl:#623a2f",
    "",
    "eyr:2029 ecl:blu cid:129 byr:1989",
    "iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm",
    "",
    "hcl:#888785",
    "hgt:164cm byr:2001 iyr:2015 cid:88",
    "pid:545766238 ecl:hzl",
    "eyr:2022",
    "",
    "iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"
]


class Test(unittest.TestCase):
    def test_part_1_known_input(self):
        self.assertEqual(2, part_one(KNOWN_INPUT))

    def test_part_2_valid_input(self):
        self.assertEqual(4, part_two(VALID_DATA))

    def test_part_2_invalid_input(self):
        self.assertEqual(0, part_two(INVALID_DATA))

    def test_part_2_birth_year(self):
        for i in ["1920", "1950", "2002"]:
            self.assertTrue(valid_birth_year(i))

    def test_part_2_invalid_birth_year(self):
        for i in ["0", "1919", "2003", "2020"]:
            self.assertFalse(valid_birth_year(i))

    def test_part_2_issue_year(self):
        for i in ["2010", "2015", "2020"]:
            self.assertTrue(valid_issue_year(i))

    def test_part_2_invalid_issue_year(self):
        for i in ["0", "1919", "2009", "2021"]:
            self.assertFalse(valid_issue_year(i))

    def test_part_2_expiration_year(self):
        for i in ["2020", "2025", "2030"]:
            self.assertTrue(valid_expiration_year(i))

    def test_part_2_invalid_expiration_year(self):
        for i in ["0", "2019", "2031", "3000"]:
            self.assertFalse(valid_expiration_year(i))

    def test_part_2_height(self):
        for i in ["60in", "190cm", "150cm", "193cm", "59in", "76in"]:
            self.assertTrue(valid_height(i))

    def test_part_2_invalid_height(self):
        for i in ["190in", "190", "149cm", "194cm", "58in", "77in"]:
            self.assertFalse(valid_height(i))

    def test_part_2_hair_color(self):
        for i in ["#123abc", "#000000", "#ffffff"]:
            self.assertTrue(valid_hair_color(i))

    def test_part_2_invalid_hair_color(self):
        for i in ["#123abz", "123abc", "#111abcd", "#1111abc", "ddddddd"]:
            self.assertFalse(valid_hair_color(i))

    def test_part_2_eye_color(self):
        for i in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            self.assertTrue(valid_eye_color(i))

    def test_part_2_invalid_eye_color(self):
        for i in ["lil", "yel", "gre", "wht", "blk", "vio", "san"]:
            self.assertFalse(valid_eye_color(i))

    def test_part_2_passport_id(self):
        for i in ["000000001", "100000001", "999999999"]:
            self.assertTrue(valid_passport_id(i))

    def test_part_2_invalid_passport_id(self):
        for i in ["0", "0123456789", "2003"]:
            self.assertFalse(valid_passport_id(i))

    def test_part_2_country_id(self):
        for i in ["000000001", "100000001", "999999999", "0", "0123456789", "2003"]:
            self.assertTrue(valid_country_id(i))


if __name__ == '__main__':
    unittest.main()
