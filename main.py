import streamlit as st

# Title of the portfolio
st.title('Kuldeep Singh - Software Developer | DevOps Engineer')

st.write("""
**Address:** 838 Kasba Peth, behind Maya Bakery Pune 411011  
**Phone:** +91 7387236721  | **Email:** [kuldeeps.official@gmail.com](mailto:kuldeeps.official@gmail.com)  
**LinkedIn:** [linkedin.com/in/kuldeepsingh666](https://www.linkedin.com/in/kuldeepsingh666/)  | **GitHub:** [github.com/kuldeepsingh666](https://github.com/kuldeepsingh666)
""")

# Technical Skills
st.header('Technical Skills')
st.write("""
- **Languages:** Python, Go, HTML, Java, SQL (Postgres, SQLite, MySQL, Oracle DB)
- **Frameworks/Libraries:** BeautifulSoup, Scrapy, Flask, Pandas, Selenium
- **Version Control:** Git, GitHub
- **Cloud and DevOps:** AWS EC2, RDS, S3, Elastic Beanstalk, EBS, Linux (Configuring and Managing), Docker
- **Others:** Object-Oriented Programming (OOP), Functional Programming, Networking, Databases, ETL, CI/CD Pipelines, Agile
""")

# Experience
st.header('Experience')
st.write("""
**SDE 1 | Wissen Research**  
*January 2024 – Present*  
- Architected and implemented advanced web scrapers that performed comprehensive scans of hundreds of websites, significantly enhancing the efficiency and scope of data collection.
- Led the development of a sophisticated web application and various APIs that consolidated data from diverse sources, providing real-time updates and robust data management capabilities.
- Collaborated with a team of seasoned developers to establish cloud operations with AWS and build CI/CD pipelines, playing a key role in the development and deployment of the web application.

**Technologies used:** AWS, Python, Flask, HTML, Javascript, MySQL, Scrapy, Selenium, BeautifulSoup, JSON, Postman, SQLite, API, Docker, Linux
""")

# Education
st.header('Education')
st.write("""
**Modern College of Arts, Science and Commerce (Autonomous), Pune**  
*2021 - 2024*  
- **Bachelor of Computer Applications (Science)**  
- **SGPA:** 8.7

**Relevant Coursework:** Object Oriented Programming, Databases, Discrete Maths, Data Structures and Algorithms, Operating Systems, Computer Networks, Web Development, Software Development, Cloud Computing(AWS)
""")

# Projects
st.header('Projects')
st.write("""
**Algorithmic Trading Bot**  
*November 2023*  
- Developed an algorithmic trading bot using Python to automate and optimize my trading strategy.
- Leveraged APIs to fetch real-time stock data and implemented strategy with processes to automate strike price selections, taking multiple trades.

**SQL Injection Scanner**  
*October 2023*  
- Developed a SQL injection scanner to automate testing for forms on websites which could be vulnerable.
- Decreased time spent on manual testing for SQL injections.

**Project Manager**  
*March 2024*  
- Developed a Project Manager using Flask for my organization to help manage projects by creating a proper hierarchy between different departments.

**Web Scrapers**  
*January 2024*  
- Developed web scrapers for my organization to handle diverse data collection needs, utilizing technologies like Scrapy, SQLite, AWS EC2, RDS, MySQL, HTML, JSON, and AWS S3.

**PDF Scraper**  
*January 2024*  
- Created a PDF file scraper using Selenium, Scrapy, and OCR to overcome data scraping challenges from PDF files.
- Doubled efficiency of projects by removing the manual data mining from PDF files.
""")

# Certifications
st.header('Certifications')
st.write("""
- **AWS Academy Graduate** - AWS Academy Cloud Foundations
- **Certified Ethical Hacker (CEH)** - Training Certification by Sysap Technologies
- **CCNA (Cisco Certified Network Associate)** - Training Certification by Sysap Technologies
""")

# Footer
st.write("---")
st.write("© 2024 Kuldeep Singh. All Rights Reserved.")

