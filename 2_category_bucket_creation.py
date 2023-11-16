import json

def create_category_buckets() -> None:
    """
    Creating category buckets for each startup category.
    """

    buckets = {
        "Technology, Hardware and Computing": [
            "App Discovery", "App Stores", "Browser Extensions", "Business Information Systems", "Early-Stage Technology",
            "CAD", "CRM", "Communications Hardware", "Communications Infrastructure", "Computer Vision", "Computers",
            "Content Delivery", "Content Discovery", "Content Syndication", "Corporate IT", "Cyber", "Deep Information Technology",
            "Developer APIs", "Development Platforms", "Digital Signage", "Document Management", "Domains", "Early Stage IT", 
            "Email", "Email Marketing", "Email Newsletters", "Embedded Hardware and Software", "Facebook Applications", "FPGA", "Face Recognition", 
            "File Sharing", "Flash Storage", "Fmcg", "Forums", "Google Apps", "Google Glass","GreenTech", "Group Email", "Group SMS", "Hardware", 
            "Hardware + Software", "Cryptocurrency", "Hi Tech", "High Tech", "Human Computer Interaction", "ICT", "IT Management",
            "IaaS", "Identity Management", "Image Recognition", "Information Security", "Information Services", "Information Technology", "Infrastructure", 
            "Infrastructure Builders", "Innovation Engineering", "Innovation Management", "Internet", "Internet Infrastructure", "Internet Marketing",
            "Internet Radio Market", "Internet Service Providers", "Internet TV", "Internet Technology", "Internet of Things", "Linux", "Local Advertising",
            "Local Based Services", "Local Coupons", "Local Search", "Local Services", "Location Based Services", "Mac", "IT and Cybersecurity", 
            "Marketing Automation", "Material Science", "Mechanical Solutions", "Messaging", "MicroBlogging", "Motion Capture", 
            "Network Security", "Networking", "NFC", "Nanotechnology", "Natural Language Processing", "Natural Resources", 
            "Navigation", "Networking", "New Technologies", "Notebooks", "Nutraceutical", "Open Source", "Operating Systems",
            "Optical Communications", "Optimization", "PaaS", "Pervasive Computing", "Point of Sale", "Polling", "Portals", "Prediction Markets",
            "Predictive Analytics", "Presentations", "Price Comparison", "Printing", "Product Design", "Product Development Services", 
            "Productivity Software", "Project Management", "Proximity Internet", "Public Relations", "3D Technology", "App Discovery", "App Stores",
            "Browser Extensions", "Business Information Systems", "Communications Hardware", "Communications Infrastructure", "Computer Vision", 
            "Computers", "Corporate IT", "Cyber", "Adaptive Equipment", "Advanced Materials", "Algorithms", "Analytics", "Android", 
            "Application Performance Monitoring", "Application Platforms", "Apps", "Archiving", "Artificial Intelligence", "Assisitive Technology", 
            "Automated Kiosk", "Batteries", "Augmented Reality", "Call Center Automation", "Developer Tools", "Displays", "Gadget", "Clean Technology",
            "Displays", "Interface Design", "Intelligent Systems", "M2M", "Machine Learning", "Mining Technologies", "Mobility", "RFID", "RIM",
            "Robotics", "SaaS", "Sales Automation", "Semiconductor Manufacturing Equipment", "Semiconductors", "Sensors", "Service Industries",
            "Smart Building", "Smart Grid", "Simulation", "Clean Technology IT", "Electronics", "Semantic Web", "Software", "Software Compliance",
            "Speech Recognition", "Spam Filtering", "Storage", "Systems", "Technology", "Telecommunications", "Telephony", "Synchronization",
            "Cable", "Testing", "Text Analytics", "Ticketing", "Transaction Processing", "Translation", "UV LEDs", "Unifed Communications",
            "User Experience Design", "User Interface", "User Testing", "Utilities", "Virtual Desktop", "Virtualization", "VoIP", "Web Browsers",
            "Web CMS", "Web Design", "Web Development", "Web Hosting", "Web Presence Management", "Web Tools", "WebOS", "Windows Phone 7", "Wireless",
            "iOS", "iPad", "iPhone", "iPod Touch", "Enterprise Hardware", "Trusted Networks", "Unmanned Air Systems"
        ],


        "Data and Cloud": [
            "Cloud Data Services", "Cloud Gaming", "Cloud Infrastructure", "Cloud Management", "Cloud Security", "Data Center Automation", 
            "Data Center Infrastructure", "Data Centers", "Data Integration", "Data Privacy", "Data Security", "EDA Tools", "Predictive Analytics",
            "Cloud Data Services", "Cloud Infrastructure", "Cloud Management", "Cloud Security", "Data Center Automation", "Data Center Infrastructure",
            "Data Centers", "Data Integration", "Data Privacy", "Data Security", "Analytics", "Artificial Intelligence", "Big Data", "Big Data Analytics",
            "Business Intelligence", "Cloud Computing", "Databases", "Data Mining", "Data Visualization", "Machine Learning", "Game Mechanics",
            "Gamification", "Geospatial", "QR Codes", "Quantified Self", "Quantitative Marketing", "Semantic Search", "Storage", "Social Media Monitoring",
            "Text Analytics"
        ],


        "Mobile and Online Technology": [
            "Mobile Advertising", "Mobile Analytics", "Tablets", "Reviews and Recommendations", "Tablets", "Twitter Applications",
            "Mobile Commerce", "Mobile Coupons", "Mobile Devices", "Mobile Emergency&Health", "Semantic Web", "Web CMS", "iPad",
            "Mobile Enterprise", "Mobile Games", "Mobile Health", "Mobile Infrastructure", "Reading Apps", "Visual Search", "iPhone",
            "Mobile Payments", "Mobile Search", "Mobile Security", "Mobile Shopping", "Semantic Web", "Vertical Search", "WebOS",
            "Mobile Social", "Mobile Software Tools", "Mobile Video", "Online Dating", "Online Education", "Web Development",
            "Online Gaming", "Online Identity", "Online Rental", "Online Reservations", "Online Scheduling", "Web Hosting", "Web Tools",
            "Online Shopping", "Online Travel", "Online Video Advertising", "E-Commerce", "Online Shopping", "Web Presence Management",
            "Online Auctions", "Mobile Commerce", "Peer-to-Peer", "Performance Marketing", "Personal Data", "App Discovery", "App Stores",
            "Browser Extensions", "Android", "Application Performance Monitoring", "Application Platforms", "Apps", "Augmented Reality",
            "Bridging Online and Offline", "China Internet", "Consumer Internet", "Darknet", "Curated Web", "Mobile", "E-Commerce Platforms",
            "Group Buying", "Marketplaces", "Match-Making", "Meeting Software", "News", "Opinions", "Q&A", "Real Time", "Recipes",
            "Ride Sharing", "SEO", "SMS", "SNS", "Search", "Search Marketing", "Semantic Search", "Social + Mobile + Local",
            "Mobile Enterprise", "Mobile Payments", "Reading Apps", "Web Browsers", "Web Design", "Windows Phone 7", "iPod Touch",
            "Mobile Payments", "Mobile Commerce", "Mobile Health", "mHealth"
        ],


        "Health, Human Resource and Wellness": [
            "Assistive Technology", "Assisted Living", "Biometrics", "Clinical Trials", "Self Development", "Senior Citizens",
            "Corporate Wellness", "Cosmetic Surgery", "Dental", "Diabetes", "Diagnostics", "Skill Assessment", "Sex Industry",
            "Dietary Supplements", "Elderly", "Electronic Health Records", "Exercise", "Eyewear", "Reputation", "Tech Field Support",
            "Fertility", "First Aid", "Health and Wellness", "Neuroscience", "Health Services Industry", "SexTech", "Fertility",
            "Health and Wellness", "Healthcare Services", "Homeless Shelter", "Humanitarian", "Life Sciences", "Temporary Staffing",
            "Lifestyle", "Lifestyle Businesses", "Lifestyle Products", "Mobile Health", "Health Services Industry", "Spas",
            "Hospitals", "Human Resource Automation", "Human Resources", "Human Resource Automation", "Human Resources", "Staffing Firms",
            "Labor Optimization", "Personal Branding", "Personal Finance", "Pharmaceuticals", "Physicians", "Social Recruiting",
            "Plumbers", "Professional Networking", "Professional Services", "Psychology", "Parenting", "Active Lifestyle", "Alternative Medicine",
            "Assisitive Technology", "BPO Services", "Baby Safety", "Call Center Automation", "Babies", "Baby Boomers", "Collaboration", 
            "Contact Centers", "Contact Management", "Doctors", "Elder Care", "Families", "Child Care", "Coworking", "Demographies",
            "Field Support Services", "Health Diagnostics", "Health and Insurance", "Medical Professionals", "Medication Adherence",
            "Independent Pharmacies", "Mens Specific", "Communities", "Identity", "Indians", "Local", "Mothers", "Recruiting", "Personal Health",
            "Public Safety", "Rehabilitation", "Religion", "Remediation", "Senior Health", "Outsourcing", "Retirement", "Corporate Wellness",
            "Senior Citizens", "SexTech", "Teenagers", "Unifed Communications", "Virtual Workforces", "Mobile Health", "mHealth",
            "Temporary Staffing", "Usability", "Femtech", "Underserved Children", "Waste Management", "Women", "Young Adults"
        ],


        "Animals and Vet": [
            "Animal Feed", "Pets", "Hunting Industry", "Veterinary"
        ],


        "Enterprise, Business and Finance": [
            "Angels", "Anything Capital Intensive", "Bitcoin", "Brokers", "Social Business", "Consumer Lending", "Finance",
            "Business Analytics", "Business Development", "Business Productivity", "Business Travelers", "Social CRM",
            "Consumer Lending", "Credit", "Credit Cards", "Crowdfunding", "Crowdsourcing", "Debt Collecting", "Sponsorship",
            "Employer Benefits Programs", "Employment", "Enterprise Software", "Entrepreneur", "Staffing Firms", "Startup Histrionics",
            "Finance Technology", "Financial Exchanges", "Financial Services", "Freelancers", "Local Commerce", "Startups",
            "Outdoor Advertising", "Hedge Funds", "Insurance Companies", "Intellectual Asset Management", "Intellectual Property",
            "Interest Graph", "Lead Generation", "Lead Management", "Legal", "Licensing", "Fraud Detection", "Surveys",
            "Loyalty Programs", "Made in Italy", "Maps", "Payments", "Postal and Courier Services", "Pre Seed", "Private Corrections",
            "Private School", "Procurement", "Promotional", "Business Information Systems", "CRM", "Enterprise 2.0", "Virtual Goods",
            "Enterprise Application", "Enterprise Hardware", "Enterprise Purchasing", "Enterprise Resource Planning",
            "Enterprise Search", "Enterprise Security", "Enterprise Software", "Enterprises", "Business Information Systems", "Ad Targeting",
            "Advertising", "Auctions", "Business Intelligence", "B2B", "B2B Express Delivery", "Business Services", "Billing", "Contact Centers",
            "Classifieds", "Commodities", "Consulting", "Consumer Behavior", "Customer Service", "Customer Support Tools", "FinTech",
            "Direct Sales", "Distributors", "Field Support Services", "Flash Sales", "Freemium", "Funeral Industry", "Comparison Shopping",
            "Consumers", "Franchises", "Impact Investing", "Independent Pharmacies", "Mens Specific", "Micro-Enterprises", "Multi-level Marketing",
            "Local Businesses", "Moneymaking", "Sales Automation", "Service Providers", "Services", "Shared Services", "Non Profit", "Non-Tech",
            "Nonprofits", "Office Space", "Offline Businesses", "Oil", "Oil & Gas", "Oil and Gas", "Outsourcing", "Personalization",
            "Racing", "Radical Breakthrough Startups", "Rapidly Expanding", "Real Estate Investors", "Realtors", "Registrars", "Restaurants",
            "Risk Management", "Rural Energy", "Salesforce Killers", "Self Storage", "Shipping Broker Industry", "Small and Medium Businesses",
            "Subscription Businesses", "Subscription Service", "Social Investing", "Social Entrepreneurship","Social Fundraising", "Social Investing",
            "Mobile Commerce", "Mobile Payments", "Business Intelligence", "Business Travel", "Ventures for Good"
        ],


        "Consumer Goods and Retail": [
            "Auctions", "Automated Kiosk", "Baby Accessories", "Baby Safety", "Batteries", "Self Storage", "Toys", "Twin-Tip Skis",
            "Bicycles", "Brewing", "Coffee", "Consumer Goods", "Consumer Internet", "Consumers", "Shoes", "Skate Wear",
            "Content Creators", "Contests", "Cooking", "Coupons", "Craft Beer", "Creative Industries", "Soccer", "Electronics",
            "Custom Retail", "Direct Sales", "Discounts", "Displays", "Flash Sales", "Gift Registries", "Utilities", "Jewelry",
            "Flowers", "Food Processing", "Fruit", "Funeral Industry", "Furniture", "Gadget", "Game Mechanics", "Gift Exchange",
            "Gamification", "Gift Card", "Gift Exchange", "Gift Registries", "Gold", "Golf Equipment", "Green Consumer Goods",
            "Groceries", "Group Buying", "Guides", "Handmade", "Natural Gas Uses", "Home & Garden", "Home Automation", "Home Decor", 
            "Home Owners", "Home Renovation", "Hospitality", "Hotels", "Jewelry", "Kids", "Lighting", "Limousines", "Lingerie", 
            "Local", "Local Businesses", "Mens Specific", "Mobile Commerce", "Mobile Shopping", "Monetization", "Moneymaking", 
            "Mothers", "Musical Instruments", "Auctions", "Babies", "Baby Accessories", "Baby Boomers", "Comparison Shopping", 
            "Flash Sales", "Apparel", "Beauty", "Consumer Electronics", "Consumer Goods", "E-Commerce", "Social Buying",
            "Fashion", "Food and Beverage", "Groceries", "Luxury", "Online Shopping", "Retail", "Social Business", "Distributors",
            "Shopping", "Wearables", "Food Processing", "Groceries", "Retail", "E-Commerce", "Online Shopping", "Gift Card",
            "Online Auctions", "Mobile Commerce", "Product Search", "CRM", "Baby Accessories", "Coffee", "Cooking", "Organic",
            "Cosmetics", "Coupons", "Craft Beer", "Curated Web", "Custom Retail", "Discounts", "DIY", "E-Books", "EBooks",
            "Fruit", "Furniture", "Gadget", "Green Consumer Goods", "Guides", "Handmade", "Home & Garden", "Home Owners", "Jewelry",
            "Kids", "Lighting", "Lingerie", "Gas", "Gold", "Golf Equipment", "Hunting Industry", "Mothers", "Retail Technology",
            "Organic Food", "Outdoors", "Green Consumer Goods", "Fashion", "Specialty Foods", "Specialty Retail", "Sunglasses",
            "Sporting Goods", "Sports", "Swimming", "Tea", "Teenagers", "Textiles", "Fashion Retail", "Fast-Moving Consumer Goods",
            "Watch", "Weddings", "Wholesale", "Wine And Spirits"
        ],


        "Entertainment, Gaming and Social": [
            "Art", "Artists Globally", "Audiobooks", "Blogging Platforms", "Broadcasting", "Gaming", "Console Gaming", "Timeshares",
            "Cable", "Chat", "Cloud-Based Music", "Collectibles", "Comics", "Concerts", "Sailing Community", "Social Media Agent",
            "Console Gaming", "Content", "Creative", "Digital Entertainment", "Digital Rights Management", "Social Media Management",
            "Direct Advertising", "Direct Marketing", "Disruptive Models", "Distribution", "Diving", "Entertainment Industry", 
            "Events", "Experience Design", "Facebook Applications", "Fantasy Sports", "FreetoPlay Gaming", "Game", "Gambling", 
            "Gps", "Guide to Nightlife", "HDTV", "Nightlife", "Entertainment and Social Media", "Hip Hop", "In-Flight Entertainment", 
            "Independent Music", "Independent Music Labels", "Indoor Positioning", "Invention", "Journalism", "Social Media Marketing",
            "Knowledge Management", "Lasers", "Leisure", "Lifestyle Products", "Media", "Messaging", "MicroBlogging", "MMO Games", 
            "Mobile Games", "Mobile Social", "Motion Capture", "Music Education", "Music Services", "Music Venues", "Incentives", 
            "Incubators", "Internet Gaming", "Internet of Things", "Kinect", "Lotteries", "Low Bid Auctions", "Mac", "MMO Games", "VoIP",
            "Mobile Games", "Monetization", "Nightclubs", "Niche Specific", "Nightlife", "Online Gaming", "P2P Money Transfer", "PC Gaming",
            "Photo Sharing", "PC Gaming", "Performing Arts", "Podcast", "Politics", "Private Social Networking", "Cloud Gaming", "Content Delivery",
            "Content Discovery", "Content Syndication", "Casual Games", "Celebrity", "Cause Marketing", "Charities", "Collaborative Consumption",
            "Contests", "Entertainment", "Educational Games", "Families", "Game Mechanics", "Games", "Gay & Lesbian", "Recreation",
            "Ride Sharing", "Skill Gaming", "Social + Mobile + Local", "Social Activists", "Social Bookmarking", "Social Business",
            "Social Buying", "Social CRM", "Serious Games", "Social Media Monitoring", "Social Commerce", "Social Media", "Social Media Advertising",
            "Social Media Platforms", "Reviews and Recommendations", "Social Network Media", "Social News", "Social Opinion Platform",
            "Social Recruiting", "Social Search", "Social Television", "Social Travel", "Social Games", "Surfing Community", "Social Entrepreneurship",
            "Social Fundraising", "Social Innovation", "Social Investing", "Video Chat", "Video Conferencing", "Video on Demand", "Theatre",
            "Video Game Tournaments", "Video Games", "Reviews and Recommendations", "Writers"
        ],


        "Transportation, Automotive and Logistics": [
            "Cars", "Delivery", "Drones", "Fleet Management", "Parking", "Auto", "Bicycles", "Boating Industry", "Electric Vehicles", "Distributors",
            "Aerospace", "Automotive", "Delivery", "Freight Service", "Logistics", "Maritime", "Public Transportation", "Shipping", "Taxis",
            "Supply Chain Management", "Transportation", "Logistics", "Transportation and Logistics", "Transportation and Automotive", "Logistics Company",
            "Limousines", "Motors", "Self Storage", "Shipping Broker Industry", "Sailing Community", "Aerospace", "Space Travel", "Tracking",
            "Utility Land Vehicles", "Fashion Retail", "Fast-Moving Consumer Goods", "Freight Service", "Fuel", "Fleet Management", "Unmanned Air Systems"
        ],


        "Energy and Environment": [
            "Air Pollution Control", "Biofuels", "Biomass Power Generation", "Carbon", "Recycling", "Green Consumer Goods",
            "Clean Technology IT", "Commercial Solar", "Concentrated Solar Power", "Electrical Distribution", "Solar",
            "Energy Efficiency", "Energy IT", "Energy Management", "Energy Storage", "Environmental Innovation", 
            "Fuel Cells", "Fuels", "Green", "Green Building", "Natural Gas Uses", "Clean Energy", "Clean Tech", "Climate Change", 
            "Electric Vehicle", "Energy", "Energy Management", "Environmental Engineering", "GreenTech", "Renewable Energy",
            "Sustainability", "Clean Tech", "Energy and Clean Tech", "Energy and Environment", "Clean Technology", "Gas",
            "Renewable Energies", "Renewable Tech", "Residential Solar", "Rural Energy", "Clean Technology IT", "Energy Management",
            "Energy Storage", "Environmental Engineering", "Water", "Water Purification", "Wind"
        ],


        "Education, Learning and EdTech": [
            "All Students", "Alumni", "Career Management", "Career Planning", "Certification Test", "English-Speaking", "Corporate Training",
            "Charter Schools", "College Campuses", "College Recruiting", "Colleges", "Reading Apps", "Educational Games", "Teachers",
            "Corporate Training", "Ediscovery", "Edutainment", "EdTech", "Education and Learning", "Personal Branding", "Podcast", 
            "Polling", "Portals", "Prediction Markets", "Predictive Analytics", "Presentations", "Privacy", "Private School", "Procurement",
            "Product Design", "Product Development Services", "Product Search", "Productivity", "Productivity Software", "Professional Networking", 
            "Professional Services", "Project Management", "Presentations", "Advice", "E-Learning", "EdTech", "Education", "Higher Education", 
            "K-12 Education", "Learning", "Online Education", "Professional Education", "STEM Education", "Training", "Education and EdTech", 
            "High School Students", "High Schools", "Language Learning", "Online Education", "Education and Learning", "Reading Apps",
            "Productivity", "Productivity Software", "Professional Networking", "Professional Services", "E-Books", "EBooks", "Charter Schools",
            "Teaching STEM Concepts", "Technical Continuing Education", "Translation", "Video Processing", "Video Editing", "Tutoring",
            "Universities", "University Students", "Educational Games", "E-Learning", "EdTech", "Textbooks", "Writers"
        ],


        "Manufacturing and Industrial": [
            "Bio-Pharm", "Chemicals", "Civil Engineers", "Construction", "Diagnostics", "Industrial", "Test and Measurement", "Food Processing",
            "Electronics", "Manufacturing", "Engineering Firms", "Estimation and Quoting", "Manufacturing", "Heavy Industry", "Textiles",
            "Home Automation", "Hospitality", "Human Resource Automation", "Industrial Automation", "Industrial Energy Efficiency",
            "Industrial Automation", "Industrial Energy Efficiency", "Infrastructure", "Infrastructure Builders", "Innovation Engineering",
            "Physical Security", "Plumbers", "Polling", "Portals", "Prediction Markets", "Predictive Analytics", "Printing", "Product Design", 
            "Product Development Services", "3D Printing", "CAD", "Adaptive Equipment", "Advanced Materials", "Biotechnology and Semiconductor",
            "Boating Industry", "Brewing", "Industrial", "Minerals", "Semiconductor Manufacturing Equipment", "Semiconductors", "Specialty Chemicals",
            "Electronics Manufacturing", "Engineering", "Enterprise Hardware"
        ],


        "Real Estate, Property and Construction": [
            "Building Owners", "Building Products", "Real Estate", "Real Estate, Property, and Construction", "Architecture", 
            "Building Material", "Construction", "Home Decor", "Home Renovation", "Interior Design", "Property Management", 
            "Real Estate", "Smart Home", "Real Estate, Property and Construction", "Real Estate", "Real Estate, Property and Construction",
            "Parking", "Podcast", "Point of Sale", "Polling", "Portals", "Auctions", "Commercial Real Estate", "Real Estate Investors",
            "Rental Housing", "Real Estate Investment", "Real Estate Technology", "Residential Real Estate", "Vacation Rentals"
        ],


        "Hospitality and Travel": [
            "Home Decor", "Home Renovation", "Hospitality", "Hotels", "In-Flight Entertainment", "Online Travel", "Rental Housing",
            "Real Estate", "Real Estate, Property and Construction", "Adventure Travel", "Home & Garden", "Home Owners", "Resorts",
            "Space Travel", "Business Travel", "Hotels", "Hospitality", "Heritage Tourism", "Tourism", "Travel", "Travel & Tourism",
            "Vacation Rentals"
        ],


        "Media and Arts": [
            "Advertising Exchanges", "Advertising Networks", "Advertising Platforms", "Social Television", "Video Processing",
            "Brand Marketing", "Broadcasting", "Cloud-Based Music", "Content", "Content Creators", "User Experience Design",
            "Content Delivery", "Content Discovery", "Digital Entertainment", "Digital Rights Management", "Visualization",
            "Film", "Music", "Publishing", "Television", "Video", "Video Streaming", "Graphic Design", "Video Editing",
            "Graphics", "Film Distribution", "Film Production", "Media, Arts, and Entertainment", "FreetoPlay Gaming", 
            "Gambling", "Game", "Media, Arts, and Entertainment", "Journalism", "Media", "Hip Hop", "Independent Music", 
            "Independent Music Labels", "Music Education", "Music Services", "Music Venues", "Musical Instruments", "Musicians",
            "Photo Editing", "Photo Sharing", "Photography", "Podcast", "3D", "Audio", "Charity", "Digital Media", "Creative Industries",
            "Design", "Designers", "English-Speaking", "Mass Customization", "New Product Development", "TV Production", "TV Station",
            "Web Design", "Filmmaking", "Film Production", "Film Distribution", "Journalism", "Journalists"
        ],


        "Healthcare and Biotechnology": [
            "Assistive Technology", "Biotechnology", "Clinical Trials", "Diagnostics", "E-Health",
            "Fitness", "Genetics", "Health and Wellness", "Healthcare", "Healthcare Services",
            "Medical", "Medical Devices", "Mental Health", "Nutrition", "Pharmaceuticals", "Therapeutics",
            "Wellness", "Health Care Information Technology", "Genetic Testing", "Healthcare", "Healthcare Services",
            "Healthcare and Biotechnology", "Healthcare Services", "Hospitals", "Alternative Medicine", "Bioinformatics", 
            "Biotechnology and Semiconductor", "Health Care", "Health Diagnostics", "Senior Health", "Health Care Information Technology",
            "Health Diagnostics", "Home Health Care"
        ],


        "Financial Services and Cryptocurrency": [
            "Banking", "Bitcoin", "Blockchain", "Capital Markets", "Credit", "Cryptocurrency", "Risk Management", "Sponsorship",
            "Finance", "Financial Services", "Fintech", "Insurance", "Investment Management", "Social Investing", "Trading",
            "Payments", "Personal Finance", "Stock Exchanges", "Venture Capital", "Cryptocurrency", "Financial Services",
            "Financial Services and Cryptocurrency", "Personal Finance", "Accounting", "Mining Technologies", "Gold", "Moneymaking",
            "Virtual Currency", "Virtual Goods", "Real Estate Investment", "Fintech", "Financial Services", "Forex", "Vending and Concessions",
            "Ventures for Good", "Wealth Management"
        ],


        "Markets, Emerging Markets, Innovation and Global Trends": [
            "Emerging Markets", "General Public Worldwide", "Generation Y-Z", "New Technologies", "Emerging Markets and Global Trends", 
            "Price Comparison", "Prediction Markets", "Product Search", "Market Research", "Innovation Engineering", "Innovation Management",
            "All Markets", "App Marketing", "Cause Marketing", "Marketplaces", "Multi-level Marketing", "Quantitative Marketing", "Search Marketing",
            "Radical Breakthrough Startups", "Sales and Marketing", "Social Media Marketing", "Space Travel", "South East Asia", "East Africa",
            "Social Innovation", "Virtual Workforces", "Virtual Goods", "Virtual Currency", "Virtual Worlds", "Brand Marketing", "Global",
            "Governance", "Government Innovation", "West Africa"
        ],


        "Event Management and Planning": [
            "Event Management", "Event Management and Planning", "Sporting Goods", "Sports", "Sports Stadiums", "Sports", "Swimming", 
            "Task Management", "Soccer", "Event Management", "Event Promotion", "Experiential Marketing", "Weddings"
        ],


        "Agriculture and Horticulture": [
            "Farming", "Agriculture and Horticulture", "Agriculture", "Aquaculture", "Cannabis", "Farmers Market", "Flowers", "Landscaping", "Tea",
            "Food Processing", "Fruit", "Organic Food", "Farming", "Food Processing", "Forestry", "Water", "Water Purification"
        ],

        
        "Legal, Security and Governance": [
            "Governance", "Government Innovation", "Governments", "Legal and Governance", "Homeland Security", "Law Enforcement",
            "Physical Security", "Privacy", "Cloud Security", "IT and Cybersecurity", "Information Security", "Defense", "Cyber Security",
            "Fraud Detection", "DOD/Military", "Security", "Software Compliance", "Social Media Monitoring", "Vulnerability Management",
            "Governance", "Government Innovation", "Fraud Detection", "Financial Compliance", "Fire Safety", "Trusted Networks"
        ],


        "Not Specified": [
            "Not Specified"
        ]
    }

    # Removing duplicates from each list in the dictionary
    for key in buckets:
        buckets[key] = list(set(buckets[key]))

    # File path and name
    file_path = "category_buckets.json"

    # Writing the dictionary to a JSON file
    with open(file_path, "w") as file:
        json.dump(buckets, file, indent=4)

    return None


if __name__ == '__main__':
    # Creating json file in current directory with category buckets
    create_category_buckets()






