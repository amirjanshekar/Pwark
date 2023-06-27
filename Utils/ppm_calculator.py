def ppm_calculator(connection, work_type, datas):
    new_data = {}
    for data in datas:
        if work_type == 'rework':
            connection.cur.execute("SELECT rework.severity, rework.detection FROM rework WHERE productId=? AND id=?",
                                   (data[10], data[7],))
            data3 = connection.cur.fetchall()[0]
        else:
            connection.cur.execute(
                "SELECT wastages.severity, wastages.detection FROM wastages WHERE productId=? AND id=?",
                (data[10], data[7],))
            data3 = connection.cur.fetchall()[0]
        if (data[10] in new_data) and (data[7] in new_data[data[10]]):
            new_data[data[10]][data[7]]['amount'] = new_data[data[10]][data[7]]['amount'] + data[9]
            new_data[data[10]][data[7]]['produce'] = new_data[data[10]][data[7]]['produce'] + data[8]
            new_data[data[10]][data[7]]['thousand'] = \
                new_data[data[10]][data[7]]['amount'] / new_data[data[10]][data[7]]['produce'] * 1000
            new_data[data[10]][data[7]]['ppm'] = new_data[data[10]][data[7]]['amount'] / new_data[data[10]][data[7]][
                'produce']
            new_data[data[10]][data[7]]['grade'] = grade_find(new_data[data[10]][data[7]]['thousand'])
            new_data[data[10]][data[7]]['rpn'] = new_data[data[10]][data[7]]['grade'] * data3[1] * data3[0]

        else:
            new_data[data[10]] = {
                data[7]: {'amount': data[9], 'produce': data[8], 'thousand': data[9] / data[8] * 1000,
                          'ppm': data[9] / data[8], 'rpn': grade_find(data[9] / data[8] * 100) * data3[0] * data3[1],
                          'grade': grade_find(data[9] / data[8] * 100)}}

    return new_data


def grade_find(thousand):
    match thousand:
        case thousand if thousand <= 0.01:
            return 1
        case thousand if thousand > 0.1:
            return 2
        case thousand if thousand > 0.5:
            return 3
        case thousand if thousand > 1:
            return 4
        case thousand if thousand > 2:
            return 5
        case thousand if thousand > 5:
            return 6
        case thousand if thousand > 10:
            return 7
        case thousand if thousand > 20:
            return 8
        case thousand if thousand > 50:
            return 9
        case thousand if thousand > 100:
            return 10
