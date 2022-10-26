from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver import Keys
from GenericFunction import *

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


def test_TC009_import_leads_as_campaign_members_using_CSV_and_verify(
    my_driver, salesforce
):
    salesforce
    my_driver.maximize_window()
    my_driver.find_element(
        By.XPATH, "//div[@class='slds-icon-waffle']"
    ).click()  # click dropdown
    my_driver.find_element(
        By.XPATH,
        "//*[@id='07p5g000001AvVhAAK']/div/lightning-formatted-rich-text/span/p",
    ).click()  # select marketing
    my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/one-app-nav-bar/nav/div/one-app-nav-bar-item-root[3]",
    ).click()  # click on campaign

    my_driver.find_element(By.XPATH, "//table[@role='grid']/tbody/tr/th/span/a").click()
    sleep(3)
    my_driver.find_element(By.LINK_TEXT, "Campaign Members").click()
    sleep(2)
    text = my_driver.find_element(By.XPATH, "//h1[@title='Campaign Members']").text
    assert text == "Campaign Members"
    print("Navigated to Campaign  - Campaign Members view Successfully!")
    sleep(2)
    my_driver.find_element(By.XPATH, "//a[@title='Show 2 more actions']").click()
    sleep(2)
    my_driver.find_element(By.LINK_TEXT, "Import Leads and Contacts").click()
    sleep(2)
    ele = my_driver.find_element(By.XPATH, "//iframe")
    my_driver.switch_to.frame(ele)
    sleep(3)
    my_driver.find_element(By.LINK_TEXT, "Leads").click()  # click upload lead
    my_driver.find_element(
        By.LINK_TEXT, "Add new records"
    ).click()  # click add new record
    sleep(2)
    # select rule
    boxes = my_driver.find_elements(
        By.XPATH,
        "//select[@class='select uiInput uiInputSelect uiInput--default uiInput--select']",
    )
    box = boxes[-1]
    ele = Select(box)
    ele.select_by_visible_text(
        bring_data_from_json_file(
            "data_Marketing_Leads_TC009.json", "pre_defined_rule_name"
        )
    )
    sleep(3)
    my_driver.find_element(
        By.XPATH,
        "//div[@class='firstBox selectable-input dataImporterDiCsvSelectionActivity']",
    ).click()  # click csv
    my_driver.find_element(By.XPATH, "//input[@size='16' and @type='file']").send_keys(
        bring_data_from_json_file(
            file_name="data_Marketing_Leads_TC009.json", value_name="path_leads_csv"
        )
    )  # upload file
    sleep(3)
    my_driver.find_element(
        By.XPATH, "//a[@data-interactive-lib-uid='7']"
    ).click()  # click next
    sleep(3)
    my_driver.find_element(
        By.XPATH, "//a[text()='Next']"
    ).click()  # map & click next again
    sleep(3)
    my_driver.find_element(
        By.XPATH, "//a[text()='Start Import']"
    ).click()  # click  start import
    sleep(3)

    # verify : Imported sucessfully
    element = my_driver.find_element(By.XPATH, "//div[@class='congrats']")
    assert element.text.startswith("Congratulations")
    print(
        "Lead assignment rule should be selected & Leads.CSV file imported Sucessfully in Sales force without any errors"
    )
    my_driver.find_element(By.XPATH, "//a[text()='OK']").click()
    sleep(10)
    
    #Verify Updated Lead and Their Assignee According to Rule
    
    
    
    my_driver.find_element(
        By.XPATH, "//div[@class='slds-icon-waffle']"
    ).click()  # left dropdown
    my_driver.find_element(
        By.XPATH,
        "//*[@id='07p5g000001AvVhAAK']/div/lightning-formatted-rich-text/span/p",
    ).click()  # select marketing

    my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/one-app-nav-bar/nav/div/one-app-nav-bar-item-root[4]",
    ).click()  # click on leads

    my_driver.find_element(
        By.XPATH, "//button[@title='Select a List View']"
    ).click()  # click list view drop
    drop_down = my_driver.find_elements(
        By.XPATH, "//span[@class=' virtualAutocompleteOptionText']"
    )  # drop down menu
    drop_down[4].click()  # select today's lead

    sleep(5)
   
    # bring up one name and matches the assignee
    name_from_csv = bring_data_from_json_file(
        "data_Marketing_Leads_TC009.json", "name_from_csv"
    )
    my_driver.find_element(By.XPATH, "//input[@name='Lead-search-input']").send_keys(
        name_from_csv, Keys.ENTER
    )
    full_name_from_csv = bring_data_from_json_file(
        "data_Marketing_Leads_TC009.json", "full_name_from_csv"
    )
    sleep(3)
    my_driver.find_element(By.LINK_TEXT, full_name_from_csv).click()
    sleep(3)
    
    my_driver.find_element(By.XPATH, "//a[@data-label='Details']").click()
    sleep(3)

    ele = my_driver.find_element(
        By.XPATH, "//a[@class='flex-wrap-ie11']/slot/slot/span"
    )

    sleep(3)
    assert ele.text == bring_data_from_json_file(
        "data_Marketing_Leads_TC009.json", "assign_to"
    )

    print(
        "Bulk Data Uploaded, Newly created Rule Ran and Apply Sucessfully,The primary member verify as Define on applied rule!"
    )
    sleep(3)
    
    
    
    
    
    
    


# //a[@title='Show 2 more actions']

"""
    my_driver.find_element(
        By.XPATH, "//div[@class='slds-icon-waffle']"
    ).click()  # left dropdown
    my_driver.find_element(
        By.XPATH,
        "//*[@id='07p5g000001AvVhAAK']/div/lightning-formatted-rich-text/span/p",
    ).click()  # select marketing

    my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/one-app-nav-bar/nav/div/one-app-nav-bar-item-root[4]",
    ).click()  # click on lead

    my_driver.find_element(
        By.XPATH, "//*[@id='brandBand_1']/div/div/div/div/div[1]/div[1]/div[2]/ul/li[2]"
    ).click()  # click on import lead

    ele = my_driver.find_element(By.XPATH, "//iframe")
    my_driver.switch_to.frame(ele)
    sleep(3)

    my_driver.find_element(By.LINK_TEXT, "Leads").click()  # click upload lead

    my_driver.find_element(By.LINK_TEXT, "Add new records").click()  # click add new

    my_driver.find_element(
        By.XPATH,
        "//div[@class='firstBox selectable-input dataImporterDiCsvSelectionActivity']",
    ).click()  # click csv
    my_driver.find_element(By.XPATH, "//input[@size='16' and @type='file']").send_keys(
        bring_data_from_json_file(
            file_name="data_Marketing_Leads_TC007.json", value_name="path_leads_csv"
        )
    )  # upload file
    sleep(3)
    my_driver.find_element(
        By.XPATH, "//a[@data-interactive-lib-uid='7']"
    ).click()  # click next
    sleep(3)
    my_driver.find_element(
        By.XPATH, "//a[text()='Next']"
    ).click()  # map & click next again
    sleep(3)
    my_driver.find_element(
        By.XPATH, "//a[text()='Start Import']"
    ).click()  # click  start import
    sleep(3)

    # verify : Imported sucessfully
    element = my_driver.find_element(By.XPATH, "//div[@class='congrats']")
    assert element.text.startswith("Congratulations")
    print("Leads.CSV file imported Sucessfully in Sales force without any errors")
    my_driver.find_element(By.XPATH, "//a[text()='OK']").click()
    sleep(10)






    # Verify Bulk Upload

    my_driver.find_element(
        By.XPATH, "//div[@class='slds-icon-waffle']"
    ).click()  # left dropdown
    my_driver.find_element(
        By.XPATH,
        "//*[@id='07p5g000001AvVhAAK']/div/lightning-formatted-rich-text/span/p",
    ).click()  # select marketing

    my_driver.find_element(
        By.XPATH,
        "/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/one-app-nav-bar/nav/div/one-app-nav-bar-item-root[4]",
    ).click()  # click on leads

    my_driver.find_element(
        By.XPATH, "//button[@title='Select a List View']"
    ).click()  # click list view drop
    drop_down = my_driver.find_elements(
        By.XPATH, "//span[@class=' virtualAutocompleteOptionText']"
    )  # drop down menu
    drop_down[4].click()  # select today's lead

    sleep(5)
    # verify bulk upload
    text = my_driver.find_element(
        By.XPATH, "//span[@class='countSortedByFilteredBy']"
    ).text
    total_upload = int(text[:1])
    total_leads_upload = int(
        bring_data_from_json_file("data_Marketing_Leads_TC007.json", "lead_len")
    )
    assert total_upload >= total_leads_upload
    print("Lead records loaded as bulk successfully !")
    sleep(3)
    # bring up one name and matches
    name_from_csv = bring_data_from_json_file(
        "data_Marketing_Leads_TC007.json", "name_from_csv"
    )
    my_driver.find_element(By.XPATH, "//input[@name='Lead-search-input']").send_keys(
        name_from_csv, Keys.ENTER
    )
    full_name_from_csv = bring_data_from_json_file(
        "data_Marketing_Leads_TC007.json", "full_name_from_csv"
    )
    sleep(3)
    entry_text = my_driver.find_element(By.LINK_TEXT, full_name_from_csv).text
    sleep(3)
    assert entry_text == full_name_from_csv
    print("Uploaded leads from CSV found successfully!")
    sleep(3)

"""
