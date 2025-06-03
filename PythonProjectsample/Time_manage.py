def test_required_field_validation(page):

    #Login to Get Dashbaord page
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    # page.pause()
    dashboard_heading = page.get_by_role("heading", name="Dashboard")
    if dashboard_heading.is_visible():
        print("Logged In Successfully:", dashboard_heading.text_content())

    #Click on Time to manage time
    page.get_by_role("button", name="").click()
    page.get_by_role("textbox", name="hh:mm").click()
    page.get_by_role("alert").get_by_role("textbox").first.fill("02")
    page.get_by_role("textbox", name="hh:mm").click()
    error_time = page.get_by_text("Punch out Time Should Be")
    if error_time.is_visible():
        print(error_time.text_content())
    else:
        print("Time selected is correct")
