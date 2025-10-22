def process_data(data, fn_callback):
    ## Process some data
    processed_result = data.upper()
    print(processed_result)

    ## Call the callback function with the result
    fn_callback(processed_result)


def print_result(result):
    print(f"Processed result: {result}")


## Using the callback
process_data("hello world", print_result)
