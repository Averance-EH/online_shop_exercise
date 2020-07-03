link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_submit_button(browser):
    browser.get(link)
    button_len = len(browser.find_elements_by_class_name('btn-add-to-basket'))
    assert button_len > 0, 'The button does not exist'