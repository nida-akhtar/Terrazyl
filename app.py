from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
from flask import Flask, render_template, request, jsonify, url_for
app = Flask(__name__, static_folder='static', static_url_path='/static')

# Store properties in a list instead of database
properties = []

def add_sample_data():
    global properties
    if not properties:  # Only add data if the list is empty
        # Sample Homes
        homes = [
            {
                "title": "Modern Furnished House in Gulberg",
                "price": 25000000,
                "area_size": "5 marla",
                "location": "Gulberg, Lahore",
                "property_type": "House",
                "description": "Fully furnished modern house with 3 bedrooms",
                "floor_number": 2,
                "furnished": True,
                "image_url": "/static/images/house1.jpg"
            },
            {
                "title": "Luxury Villa in DHA",
                "price": 45000000,
                "area_size": "1 kanal",
                "location": "DHA Phase 6, Karachi",
                "property_type": "House",
                "description": "Spacious villa with swimming pool",
                "floor_number": 3,
                "furnished": True,
                "image_url": "/static/images/house2.jpg"
            },
            {
                    "title": "Family Home in Bahria Town",
                    "price": 35000000,
                    "area_size": "10 marla",
                    "location": "Bahria Town, Islamabad",
                    "property_type": "House",
                    "description": "Beautiful family home with garden",
                    "floor_number": 2,
                    "furnished": False,
                    "image_url": "/static/images/house3.jpg"
                },
                {
                    "title": "Modern Apartment in Clifton",
                    "price": 28000000,
                    "area_size": "4 marla",
                    "location": "Clifton, Karachi",
                    "property_type": "House",
                    "description": "High-rise apartment with sea view",
                    "floor_number": 15,
                    "furnished": True,
                    "image_url": "/static/images/house4.jpg"
                },
                {
                    "title": "Penthouse in Johar Town",
                    "price": 42000000,
                    "area_size": "8 marla",
                    "location": "Johar Town, Lahore",
                    "property_type": "House",
                    "description": "Luxurious penthouse with roof garden",
                    "floor_number": 8,
                    "furnished": True,
                    "image_url": "/static/images/house5.jpg"
                },
                {
                    "title": "Traditional Home in Peshawar",
                    "price": 22000000,
                    "area_size": "7 marla",
                    "location": "Hayatabad, Peshawar",
                    "property_type": "House",
                    "description": "Beautiful traditional style home",
                    "floor_number": 1,
                    "furnished": False,
                    "image_url": "/static/images/house6.jpg"
                },
                {
                    "title": "Modern Flat in Gulshan",
                    "price": 18000000,
                    "area_size": "3 marla",
                    "location": "Gulshan, Karachi",
                    "property_type": "House",
                    "description": "Newly built apartment with modern amenities",
                    "floor_number": 5,
                    "furnished": True,
                    "image_url": "/static/images/house7.jpg"
                },
                {
                    "title": "Family House in Faisalabad",
                    "price": 32000000,
                    "area_size": "6 marla",
                    "location": "Civil Lines, Faisalabad",
                    "property_type": "House",
                    "description": "Spacious family house with parking",
                    "floor_number": 2,
                    "furnished": False,
                    "image_url": "/static/images/house8.jpg"
                },
                {
                    "title": "Luxury Apartment in E-11",
                    "price": 38000000,
                    "area_size": "5 marla",
                    "location": "E-11, Islamabad",
                    "property_type": "House",
                    "description": "Premium apartment with mountain view",
                    "floor_number": 10,
                    "furnished": True,
                    "image_url": "/static/images/house9.jpg"
                },
                {
                    "title": "Modern Home in Quetta",
                    "price": 27000000,
                    "area_size": "9 marla",
                    "location": "Samungli Road, Quetta",
                    "property_type": "House",
                    "description": "Contemporary design with all facilities",
                    "floor_number": 2,
                    "furnished": True,
                    "image_url": "/static/images/house10.jpg"
                }
            
        ]

        # Sample Plots
        plots = [
            {
                "title": "Commercial Plot in DHA",
                "price": 50000000,
                "area_size": "1 kanal",
                "location": "DHA Phase 1, Lahore",
                "property_type": "Plot",
                "description": "Prime location commercial plot",
                "image_url": "/static/images/plot1.jpg"
            },
            {
                "title": "Residential Plot in Bahria",
                "price": 15000000,
                "area_size": "5 marla",
                "location": "Bahria Town, Karachi",
                "property_type": "Plot",
                "description": "Corner plot in prime location",
                "image_url": "/static/images/plot2.jpg"
            },
             {
                    "title": "Investment Plot in Capital",
                    "price": 25000000,
                    "area_size": "10 marla",
                    "location": "F-7, Islamabad",
                    "property_type": "Plot",
                    "description": "Excellent investment opportunity",
                    "image_url": "/static/images/plot3.jpg"
                },
                {
                    "title": "Commercial Plot in Gulberg",
                    "price": 45000000,
                    "area_size": "2 kanal",
                    "location": "Gulberg III, Lahore",
                    "property_type": "Plot",
                    "description": "Main boulevard commercial plot",
                    "image_url": "/static/images/plot4.jpg"
                },
                {
                    "title": "Residential Plot in DHA",
                    "price": 20000000,
                    "area_size": "7 marla",
                    "location": "DHA Phase 8, Karachi",
                    "property_type": "Plot",
                    "description": "Ready for construction",
                    "image_url": "/static/images/plot5.jpg"
                },
                {
                    "title": "Plot in Gulshan",
                    "price": 18000000,
                    "area_size": "8 marla",
                    "location": "Gulshan-e-Iqbal, Karachi",
                    "property_type": "Plot",
                    "description": "Residential plot in secure area",
                    "image_url": "/static/images/plot6.jpg"
                },
                {
                    "title": "Commercial Plot in Blue Area",
                    "price": 80000000,
                    "area_size": "4 kanal",
                    "location": "Blue Area, Islamabad",
                    "property_type": "Plot",
                    "description": "Premium commercial location",
                    "image_url": "/static/images/plot7.jpg"
                },
                {
                    "title": "Plot in Johar Town",
                    "price": 22000000,
                    "area_size": "6 marla",
                    "location": "Johar Town, Lahore",
                    "property_type": "Plot",
                    "description": "Residential plot near park",
                    "image_url": "/static/images/plot8.jpg"
                },
                {
                    "title": "Investment Plot in Peshawar",
                    "price": 17000000,
                    "area_size": "5 marla",
                    "location": "Hayatabad, Peshawar",
                    "property_type": "Plot",
                    "description": "Growing area investment plot",
                    "image_url": "/static/images/plot9.jpg"
                },
                {
                    "title": "Commercial Plot in Faisalabad",
                    "price": 35000000,
                    "area_size": "1.5 kanal",
                    "location": "Susan Road, Faisalabad",
                    "property_type": "Plot",
                    "description": "Main road commercial plot",
                    "image_url": "/static/images/plot10.jpg"
                }
            
        ]

        # Add IDs to properties and combine homes and plots
        id_counter = 1
        for property in homes + plots:
            property['id'] = id_counter
            properties.append(property)
            id_counter += 1

# Initialize sample data
add_sample_data()

@app.route('/')
def home():
    # Get filter parameters
    search_query = request.args.get('query', '').lower()
    area_size = request.args.get('area_size', '')
    property_type = request.args.get('property_type', '')
    
    # Filter properties based on search criteria
    filtered_properties = properties

    if search_query:
        filtered_properties = [p for p in filtered_properties if 
            search_query in p['title'].lower() or 
            search_query in p['location'].lower() or 
            search_query in p['description'].lower()]
    
    if area_size:
        filtered_properties = [p for p in filtered_properties if p['area_size'] == area_size]
    
    if property_type:
        filtered_properties = [p for p in filtered_properties if p['property_type'] == property_type]
    
    return render_template('home.html', properties=filtered_properties)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/search')
def search():
    query = request.args.get('query', '').lower()
    area_size = request.args.get('area_size', '')
    property_type = request.args.get('property_type', '')
    
    filtered_properties = properties

    if query:
        filtered_properties = [p for p in filtered_properties if 
            query in p['title'].lower() or 
            query in p['location'].lower() or 
            query in p['description'].lower()]
    
    if area_size:
        filtered_properties = [p for p in filtered_properties if p['area_size'] == area_size]
    
    if property_type:
        filtered_properties = [p for p in filtered_properties if p['property_type'] == property_type]
    
    return jsonify(filtered_properties)

if __name__ == '__main__':
    app.run(debug=True)