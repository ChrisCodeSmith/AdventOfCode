import re

MUST_CONTAIN = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl',
                'pid'}


VALID_DATA = {'byr': re.compile('^(19[2-9][0-9]|200[0-2])$'),
              'iyr': re.compile('^(201[0-9]|2020)$'),
              'eyr': re.compile('^(202[0-9]|2030)$'),
              'hgt': re.compile('^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$'),
              'hcl': re.compile('^#[0-9a-f]{6}$'),
              'ecl': re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$'),
              'pid': re.compile('^[0-9]{9}$')}


def solve(with_validator: bool = False):
    """ This gets solved by working with a list of passports. Every passport is a list of fields.
        Valid are passports with 8 fields and passports with 7 fields that contain at least the fields
        described above in MUST_HAVE.
        While checking for 8 fields is rather simple, for the 7 fields we split the fields and convert their keys
        to a set. We then check if this is a subset of the MUST_CONTAIN set.

        with_validator=True for part 2: validate the input based on the regexes saved in VALID_DATA dict above.
    """
    with open('03_input.txt', 'r') as f:
        lines = f.read().split('\n\n')  # get total passports i.e.: list of strings
        lines = [line.split() for line in lines]  # logically combine the passports to a list of passport fields.
        valid_pps = 0
        for passport in lines:
            if len(passport) == 8:
                if with_validator:
                    if validate_passport(passport):
                        valid_pps += 1
                else:
                    valid_pps += 1
            elif len(passport) == 7 and set([field.split(':')[0] for field in passport]).issubset(MUST_CONTAIN):
                if with_validator:
                    if validate_passport(passport):
                        valid_pps += 1
                else:
                    valid_pps += 1
        return valid_pps


def validate_passport(passport: list):
    """ Validate passport: passport is a list of fields, first remove 'cid' fields, then convert it to a dict of fields
        and test it against the VALID_DATA dict from top of the file which contains regex
    """
    fil = list(filter(lambda x: x.startswith('cid:'), passport))
    if fil:
        passport.remove(fil[0])
    passport = {field.split(':')[0]: field.split(':')[1] for field in passport}
    for field in passport:
        valid = re.match(VALID_DATA[field], passport[field])
        if not valid:
            return False
    return True


if __name__ == '__main__':
    print(solve())
    print(solve(with_validator=True))
