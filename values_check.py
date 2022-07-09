def values_check(value_check):
    if not isinstance(value_check, list):
        raise ValueError(f'List required, {type(value_check)} were passed')
    for i in value_check:
        if not isinstance(i, (int, float)):
            raise ValueError(f'Elements of list must be int/float, {type(i)} were passed')
