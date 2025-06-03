from conftest import login
def test_successful_login():
    page = login()
    page.wait_for_timeout(2000)
    dashboard_heading = page.get_by_role("heading", name="Dashboard")
    if dashboard_heading.is_visible():
        print("Logged In Successfully:", dashboard_heading.text_content())

    #Click on Time to manage time
    page.get_by_role("button", name="").click()
    page.get_by_role("textbox", name="hh:mm").click()
    page.get_by_role("alert").get_by_role("textbox").first.fill("225")
    page.locator("input[name=\"am\"]").click()
    page.get_by_role("textbox", name="hh:mm").click()
    page.wait_for_timeout(2000)
    error_time = page.get_by_text("Punch out Time Should Be")
    if error_time.is_visible():
        print(error_time.text_content())
    else:
        print("Time selected is correct")
