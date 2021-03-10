from typing import List


def testRunner(inputs: List[any], Solution):
    if not inputs:
        return
    for func_name, handler in Solution.__dict__.items():
        if func_name.startswith('_'):
            continue
        print(func_name, ":")
        result = []
        for i, data in enumerate(inputs):
            try:
                output = handler(None, data)
            except:
                output = handler(None, *data)
            result.append(output)
            if expects:
                print('result: {0}, {1}'.format(
                    output, 'passed' if expects[i] == output else 'failed'))
            else:
                print(output)

        if expects:
            print('all test passed' if result == expects else 'some test failed')
        print()
