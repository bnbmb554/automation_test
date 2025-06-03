def test_required_field_validation(browser_page):
    page = browser_page
    # Email & Password Required validation
    page.get_by_role("button", name="Login").click()
    required_element = page.get_by_text("Required").first
    page.wait_for_timeout(2000)

    if required_element.is_visible():
        print("Username and password are:", required_element.text_content())
    else:
        print("No error validation displayed")


    # Login with Wrong Credientials
    page.get_by_placeholder("Username").fill("vive.yadav@yopmail.com")
    page.get_by_placeholder("Password").fill("Ganesha@5050")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(2000)
    error_element = page.get_by_text("Invalid credentials")
    if error_element.is_visible():
        print("Error Message Displayed:",error_element.text_content())
    else:
        print("Not able to Print error message")
        page.wait_for_timeout(2000)

    # #Login With correct Credientials
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(2000)
    dashboard_heading = page.get_by_role("heading", name="Dashboard")
    if dashboard_heading.is_visible():
        print("Logged In Successfully:", dashboard_heading.text_content())
    else:
        print("Log in Attempt Failed")
        page.wait_for_timeout(5000)

    # #Logout the Logged in user
    # page.pause()
    page.get_by_role("listitem").locator("i").click()
    page.get_by_role("menuitem", name="Logout").click()
    page.wait_for_url("**/auth/login")
    if "auth/login" in page.url:
        print("Successfully Logged Out Page Title", page.title())
    else:
        print("Logout Failed or Incorrect Redirection")
        page.wait_for_timeout(2000)

    #Forgot your password page to reset password
    page.get_by_text("Forgot your password?").click()
    page.wait_for_url("**/requestPasswordResetCode")
    reset_password = page.get_by_role("heading", name="Reset Password")
    page.wait_for_timeout(2000)
    if reset_password.is_visible():
        print(reset_password.text_content(),"Page is displayed")
    else:
        print("Reset Password page is not displayed")

    #Username required validation in reset password
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Reset Password").click()
    usernaame_required = page.get_by_text("Required")
    if usernaame_required.is_visible():
        print("Username",usernaame_required.text_content())
    else:
        print("Didnt got the error message")

    #Reset Password for username
    page.wait_for_timeout(2000)
    page.get_by_role("textbox", name="Username").fill("Admin")
    page.get_by_role("button", name="Reset Password").click()
    page.wait_for_timeout(2000)
    success = page.get_by_role("heading", name="Reset Password link sent")
    if success.is_visible():
        print(success.text_content())
    else:
        print("Reset password was not Successfull")
        page.wait_for_timeout(2000)

    #Cancel button functionality on reset password page
    page.go_back()
    page.get_by_role("button", name="Cancel").click()
    page.get_by_role("heading", name="Login").is_visible()
    page.wait_for_timeout(2000)
    if page.get_by_role("heading", name="Login").is_visible():
        print(page.get_by_role("heading", name="Login").text_content(),"Page is displayed again")
    else:
        print("Browser back button is not clickable")

    #OrangeHRM.Inc functionality
    page.wait_for_timeout(2000)
    with page.expect_popup() as popup_info:
        page.get_by_role("link", name="OrangeHRM, Inc").click()
    new_tab = popup_info.value
    new_tab.wait_for_load_state()
    print("New Tab URL:", new_tab.url)
    try:
        heading = new_tab.locator("h1")
        if heading.is_visible():
            print("Heading Found:", heading.text_content())
        else:
            print("Heading not found")
    except:
        print("Heading element not located")


