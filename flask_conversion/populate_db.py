import DAL

# Initialize the database
DAL.init_database()

# Insert the existing projects from your website
projects_data = [
    {
        'title': 'Dynamic Pricing Recommendation Tool at Insight2Profit',
        'description': '''Developed a sophisticated pricing analytics solution that transformed transaction data into actionable pricing strategies, resulting in significant revenue impact for the business.

Key Highlights:
• Analyzed and processed over 10 million transactions using Power BI to create comprehensive pricing insights
• Designed and implemented a dynamic pricing recommendation tool that standardized discount strategies
• Generated projected revenue impact of $1.7 million through optimized pricing strategies
• Established robust data mapping and validation practices for ERP implementations
• Created detailed documentation and training materials for stakeholder adoption''',
        'image_filename': None
    },
    {
        'title': 'Predictive Analytics & Dashboards for Republic Airways',
        'description': '''Led development of sophisticated data analytics solutions for a major regional airline operating 200+ aircraft and 900+ daily flights. Created predictive models and interactive dashboards that revolutionized operational decision-making processes.

Key Highlights:
• Engineered predictive models for pilot attrition and fuel consumption analysis using Python and advanced analytics
• Developed 5 interactive Power BI dashboards tracking key operational metrics and KPIs
• Implemented automated data pipelines that significantly improved reporting efficiency
• Provided actionable insights that directly influenced strategic operational decisions''',
        'image_filename': None
    },
    {
        'title': 'Personal Portfolio Website',
        'description': '''Designed and developed a modern, responsive personal portfolio website using Flask and contemporary web technologies. Built to showcase professional experience and technical capabilities while demonstrating clean code practices and web development skills.

Key Highlights:
• Built with Flask framework for robust backend functionality and efficient routing
• Implemented responsive design using modern CSS techniques for optimal viewing across devices
• Created modular HTML templates for consistent styling and maintainable code
• Deployed with proper configuration for secure and reliable hosting''',
        'image_filename': None
    }
]

# Insert each project
for project in projects_data:
    project_id = DAL.insert_project(
        title=project['title'],
        description=project['description'],
        image_filename=project['image_filename']
    )
    print(f"Inserted project: {project['title']} (ID: {project_id})")

print("\nAll projects inserted successfully!")
print(f"\nTotal projects in database: {len(DAL.get_all_projects())}")
