from playwright.sync_api import sync_playwright

def add_job_title(job_title, job_description, file_path=None, note=None):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        # Open your web application URL
        page.goto("https://your-app-url.com/login")  # Replace with your actual URL

        # Login if required
        page.fill("input[name='username']", "your_username")
        page.fill("input[name='password']", "your_password")
        page.click("button[type='submit']")

        # Navigate to Job > Add Job Title
        page.click("text=Job")  # Click Job menu
        page.click("text=Add Job Title")  # Click Add Job Title

        # Fill the form
        page.fill("input[placeholder='Job Title']", job_title)
        page.fill("textarea[placeholder='Type description here']", job_description)
        
        if file_path:
            # Upload file if specified
            page.set_input_files("input[type='file']", file_path)
        
        if note:
            page.fill("textarea[placeholder='Add note']", note)
        
        # Submit the form
        page.click("button:has-text('Save')")  # Adjust the selector to the actual Save button

        print("Job added successfully!")
        browser.close()

# Example usage
add_job_title(
    job_title="Software Engineer",
    job_description="Responsible for developing software.",
    file_path="C:/Users/amrit/Desktop/job_spec.pdf",  # Optional
    note="This is a note about the job."
)