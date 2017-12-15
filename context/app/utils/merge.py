import pandas


def merge(frames):
    """
    Given a list of frames, merge them, potentially creating new keys.
    """
    accumulator = pandas.DataFrame()
    for frame in frames:
        accumulator = accumulator.merge(
            frame,
            how='outer',
            right_index=True,
            left_index=True)
    return accumulator

def reindex(frame, keys):
    """
    Given a dataframe that came in with no explicit index,
    identify a column whose values come from keys, and use that.
    """
    for index, row in frame.iterrows():
        matches = []
        for column_name, value in row.to_dict().items():
            if value in keys:
                matches.append(column_name)
        if len(matches) == 1:
            break
        if len(matches) == 0:
            raise Exception(
                'None of the values {} in row {} were recognized keys: {}'.format(
                    row.values, index, keys
            ))
        # Multiple matches: try the next row
    if len(matches) != 1:
        raise Exception('Could not find a row where exactly one column matched keys: {}'.format(
            keys
        ))
    return frame.set_index(matches)

