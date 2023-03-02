import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize web driver
driver = webdriver.Chrome()

# Navigate to website
driver.get("http://www.google.com")

# Inject a JavaScript function that returns the XPath of the clicked element
driver.execute_script("""
    function getElementXPath(elt) {
        const paths = [];
        for (; elt && elt.nodeType === 1; elt = elt.parentNode) {
            let idx = 0;
            for (let sibling = elt.previousSibling; sibling; sibling = sibling.previousSibling) {
                if (sibling.nodeType === 1 && sibling.nodeName === elt.nodeName) {
                    idx++;
                }
            }
            const tagName = elt.nodeName.toLowerCase();
            let pathIndex = (idx ? "[" + (idx+1) + "]" : "");
            paths.unshift(tagName + pathIndex);
        }
        return paths.join("/");
    }
    document.addEventListener("click", function(event) {
        let xpath = getElementXPath(event.target);
        console.log(xpath);
    }, false);
""")

# Click on an element on the website
# driver.find_element(By.CSS_SELECTOR,"FPdoLc lJ9FBc").click()
time.sleep(10)
# Get the XPath of the clicked element from the browser's console
xpath = driver.execute_script("return console.log")

# Print the XPath
print(xpath)

# Close the browser

driver.quit()