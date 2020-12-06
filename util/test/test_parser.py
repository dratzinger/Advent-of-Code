import unittest
from util.parser import get_input_lines, get_input_grouped

TEST_LINES = ["eyr:2033",
              "hgt:177cm pid:173cm",
              "ecl:utc byr:2029 hcl:#efcc98 iyr:2023",
              "",
              "pid:337605855 cid:249 byr:1952 hgt:155cm",
              "ecl:grn iyr:2017 eyr:2026 hcl:#866857",
              "",
              "cid:242 iyr:2011 pid:953198122 eyr:2029 ecl:blu hcl:#888785"]

TEST_GROUPS = [["eyr:2033",
              "hgt:177cm", "pid:173cm",
              "ecl:utc","byr:2029","hcl:#efcc98","iyr:2023"],
              ["pid:337605855","cid:249","byr:1952","hgt:155cm",
              "ecl:grn","iyr:2017","eyr:2026","hcl:#866857",],
              ["cid:242","iyr:2011","pid:953198122","eyr:2029","ecl:blu","hcl:#888785"]]

class Test(unittest.TestCase):
    def test_get_input_lines(self):
        self.assertEqual(TEST_LINES, get_input_lines("test_parser_input.txt"))

    def test_get_input_grouped(self):
        self.assertEqual(TEST_GROUPS, get_input_grouped("test_parser_input.txt"))


if __name__ == '__main__':
    unittest.main()