def check_for_errors(pages, page_before_pages):
    err_index = -1
    for i in range(len(pages)):
        after_me = page_before_pages.get(pages[i], [])
        if any(set(after_me).intersection(pages[:i])):
            err_index = i
            break
    return err_index


if __name__ == '__main__':
    with open('inputs/d05.txt') as fp:
        inputs_ = fp.read()
    page_before_pages = {}
    manuals = []
    for row in inputs_.splitlines(keepends=False):
        if '|' in row:
            first, second = (int(x) for x in row.split('|'))
            if first not in page_before_pages:
                page_before_pages[first] = []
            page_before_pages[first].append(second)
        if ',' in row:
            manuals.append([int(x) for x in row.split(',')])

    mid_sum_correct = 0
    mid_sum_corrected = 0
    for pages in manuals:
        error_index = check_for_errors(pages, page_before_pages)
        if error_index == -1:
            mid_sum_correct += pages[int(len(pages) / 2)]
        else:
            while error_index == -1:
                fix = pages.pop(error_index)
                pages.insert(0, fix)
                error_index = check_for_errors(pages, page_before_pages)
            mid_sum_corrected += pages[int(len(pages) / 2)]

    print(mid_sum_correct)
    print(mid_sum_corrected)
