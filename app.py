import functions

connection = functions.connect_terminal('COM6', 9600)

functions.open_site()
while True:
    data = functions.read_terminal(connection)
    functions.click_release_key('q', 0, data)
    functions.click_release_key('w', 1, data)
    functions.click_release_key('e', 2, data)
    functions.click_release_key('r', 3, data)
    functions.click_release_key('t', 4, data)
    functions.click_release_key('y', 5, data)
    functions.click_release_key('u', 6, data)
    functions.click_release_key('i', 7, data)
