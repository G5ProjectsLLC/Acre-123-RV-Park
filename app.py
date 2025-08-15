import streamlit as st

st.set_page_config(page_title="Acre 123 RV Park", layout="wide")

st.markdown("""
    <style>
    /* Remove Streamlit default padding/margin */
    .block-container {
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    [data-testid="stAppViewContainer"] > .main {
        padding-top: 0 !important;
    }

    /* Contact Bar fixed at top */
    .contact-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 1000;
    }

    /* Header fixed directly under contact bar */
    .header {
        position: fixed;
        top: 35px; /* match contact bar height */
        left: 0;
        width: 100%;
        z-index: 999;
    }

    /* Add drop shadow for nice separation */
    .contact-bar, .header {
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }

    /* Push page content down to avoid overlap */
    .hero-section,
    .about-section,
    .rates-section,
    .amenities-section,
    .park_map-section,
    .book-section {
        margin-top: 110px; /* 35px contact bar + ~75px header height */
    }
    </style>
""", unsafe_allow_html=True)




#CONTACT FORM INFO
contact_form = """
<form action="https://formsubmit.co/acre123rvpark@outlook.com" method="POST">
     <input type="text" name="name" placeholder="Your full name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <input type="phone" name="phone" placeholder="Your phone number" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
     <input type="hidden" name="_autoresponse" value="Your inquiry has been received and we will be in contact with you shortly!">
</form>
"""



# IMAGE URLs (replace with your actual GitHub raw URLs)
newlogo_url = "https://raw.githubusercontent.com/G5ProjectsLLC/Acre-123-RV-Park/main/assets/newlogo.png"
wifi_url = "https://raw.githubusercontent.com/G5ProjectsLLC/Badger-Den-RV-Park/main/assets/wifi.png"
dog_url = "https://raw.githubusercontent.com/G5ProjectsLLC/Badger-Den-RV-Park/main/assets/dog.png"
laundry_url = "https://raw.githubusercontent.com/G5ProjectsLLC/Badger-Den-RV-Park/main/assets/laundry.png"

# SMOOTH SCROLL CSS targeting Streamlit's main scroll container
st.markdown("""
    <style>
    section.main > div {
        scroll-behavior: smooth;
    }
    </style>
""", unsafe_allow_html=True)

# FIXED CONTACT BAR + HEADER
st.markdown(f"""
    <style>
    /* Remove default top spacing */
    .block-container {{
        padding-top: 0 !important;
        margin-top: 0 !important;
    }}
    [data-testid="stAppViewContainer"] > .main {{
        padding-top: 0 !important;
    }}

    /* Contact Bar fixed */
    .contact-bar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #BFA77F;
        color: #333;
        font-size: 0.85rem;
        padding: 5px 20px;
        display: flex;
        justify-content: flex-end;
        gap: 20px;
        z-index: 1001;
    }}
    .contact-bar span {{
        display: flex;
        align-items: center;
        gap: 6px;
    }}
    .contact-bar a {{
        color: inherit;
        text-decoration: none;
    }}
    .contact-bar a:hover {{
        text-decoration: underline;
    }}

    /* Header fixed directly under contact bar */
    .header {{
        position: fixed;
        top: 15px;
        left: 0;
        width: 100%;
        background-color: #E8D7B3;
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1rem 2rem;
        border-bottom: 1px solid #ddd;
        z-index: 1000;
    }}
    .header-left {{
        display: flex;
        align-items: center;
    }}
    .header-left img {{
        height: 50px;
        margin-right: 15px;
    }}
    .nav {{
        display: flex;
        gap: 20px;
    }}
    .nav a {{
        text-decoration: none;
        font-weight: 500;
        color: #333;
        padding: 6px 12px;
        border-radius: 6px;
        transition: background 0.2s ease;
    }}
    .nav a:hover {{
        background-color: #eee;
    }}
    .book-btn {{
        background-color: #D3AF37;
        color: white !important;
        padding: 6px 16px;
        border-radius: 20px;
        font-weight: bold;
    }}
    .book-btn:hover {{
        background-color: #e64a19;
    }}

    /* Drop shadow */
    .contact-bar, .header {{
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}

    /* Push page content down */
    .hero-section,
    .about-section,
    .rates-section,
    .amenities-section,
    .park_map-section,
    .book-section {{
        margin-top: 110px; /* 35px contact bar + header height */
    }}

    /* Form styling */
    input[type=text], input[type=email], input[type=phone], textarea {{
      width: 80%;
      padding: 12px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
      margin-top: 6px;
      margin-bottom: 16px;
      resize: vertical;
    }}
    button[type=submit] {{
      background-color: #04AA6D;
      color: white;
      padding: 12px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
      display: block;
      margin-top: 5px;
      margin-left: 90px;
    }}
    button[type=submit]:hover {{
      background-color: #45a049;
    }}

    /* Mobile responsive adjustments */
    @media (max-width: 768px) {{
        .header {{
            flex-direction: column;
            align-items: flex-start;
            padding: 0.5rem 1rem;
        }}
        .nav {{
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 5px;
        }}
        .book-btn {{
            padding: 4px 10px;
            font-size: 0.9rem;
        }}
    }}
    </style>

    <!-- Contact Bar -->
    <div class="contact-bar">
        <span>📞 <a href="tel:8305835739">830-583-5739</a></span>
        <span>📩 acre123rvpark@outlook.com</span>
        <span>📍 <a href="https://www.google.com/maps/dir/?api=1&destination=711+Helena+Rd,+Karnes+City,+TX+78118" target="_blank">711 Helena Rd, Kenedy, TX 78118</a></span>
    </div>

    <!-- Navigation Header -->
    <div class="header">
        <div class="header-left">
            <img src="{newlogo_url}" alt="Logo">
            <h2> Welcome to Acre 123 RV Park!</h2>
        </div>
        <div class="nav">
            <a href="#about">About</a>
            <a href="#rates">Rates</a>
            <a href="#amenities">Amenities</a>
            <a href="#park_map">Park Map</a>
            <a class="book-btn" href="#book">BOOK NOW</a>
        </div>
    </div>
""", unsafe_allow_html=True)

# GLOBAL STYLES
st.markdown(f"""
    <style>
    /* App-wide background fix for Streamlit containers */
    html, body, .stApp, [data-testid="stAppViewContainer"] {{
        background-color: #E8D7B3 !important; /* ensure the page below hero isn't white */
    }}
    /* Make Streamlit's block container transparent so the page background shows */
    main [data-testid="block-container"] {{
        background-color: transparent !important;
        padding-top: 0rem !important; /* remove default top spacing */
    }}
    /* Optional: remove default Streamlit header background if visible */
    header[role="banner"], header[data-testid="stHeader"] {{
        background: transparent !important;
    }}

    
    /* Hero Background */
    .hero-section {{
        background-image: url('{newlogo_url}');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: top center;
        height: 450px;
        display: flex;
        align-items: flex-start;
        justify-content: center;
        color: #D3AF37;
        text-shadow: 0 0 10px rgba(0,0,0,0.7);
        font-size: 2rem;
        font-weight: bold;
        padding-top: 0px;
        margin-bottom: 2rem;
    }}

    /* About Section */
    .about-section {{
        margin: 3rem 0;
        padding: 0 10%;
    }}
    .about-title {{
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 2rem;
        color: #333;
    }}
    .about-content {{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        gap: 40px;
        flex-wrap: wrap;
    }}
    .about-text, .about-list {{
        flex: 1;
        min-width: 250px;
        font-size: 1rem;
        color: #444;
    }}
    .about-text {{
        line-height: 1.6;
    }}
    .about-list ul {{
        padding-left: 20px;
    }}

    /* Rates Section */
    .rates-section {{
        margin: 3rem 0;
        padding: 0 10%;
    }}
    .rates-title {{
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
        color: #333;
    }}
    .rates-table {{
        font-size: 1.1rem;
        margin: 0 auto;
        max-width: 500px;
        color: #444;
    }}
    .rates-table table {{
        width: 100%;
        border-collapse: collapse;
        border: 2px solid #757575;
    }}
    .rates-table th, .rates-table td {{
        padding: 20px;
        border-bottom: 2px solid #757575;
        text-align: left;
    }}

    /* Amenities Section */
    .amenities {{
        display: flex;
        flex-wrap: wrap;
        gap: 40px;
        justify-content: center;
        margin: 3rem 0;
    }}
    .amenity {{
        text-align: center;
        font-size: 1.1rem;
        color: #333;
    }}
    .amenity img {{
        width: 60px;
        margin-bottom: 0.5rem;
    }}

    /* Availability Section */
    .availability-section{{
        margin: 3rem 0;
        padding: 0 10%;
        text-align: center;
                }}
    .availability-title {{
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 2rem;
        color: #333;
    }}

    
    /* Book Now Section */
    .book-section {{
        margin: 3rem 0;
        padding: 0 10%;
        text-align: center;
    }}
    .book-title {{
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 1.5rem;
        color: #333;
    }}
    .book-content {{
        font-size: 1.1rem;
        color: #555;
    }}
    .book-content a {{
        color: #000000;
        text-decoration: none;
    }}
    .book-content a:hover {{
        text-decoration: underline;
    }}
    
/* Style inputs with type="text", select elements and textareas */
input[type=text], input[type=email], input[type=phone], textarea {{
  width: 80%; /* Full width */
  padding: 12px; /* Some padding */ 
  border: 1px solid #ccc; /* Gray border */
  border-radius: 4px; /* Rounded borders */
  box-sizing: border-box; /* Make sure that padding and width stays in place */
  margin-top: 6px; /* Add a top margin */
  margin-bottom: 16px; /* Bottom margin */
  resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
}}

/* Style the submit button with a specific background color etc */
button[type=submit] {{
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  display: block;         /* forces it onto its own line */
  margin-top: 5px;       /* moves it down */
  margin-left: 90px;
}}

/* When moving the mouse over the submit button, add a darker green color */
button[type=submit]:hover {{
  background-color: #45a049;
}}



    </style>
""", unsafe_allow_html=True)

# CONTACT BAR
st.markdown("""
    <div class="contact-bar">
        <span>📞 <a href="tel:8305835739">830-583-5739</a></span>
        <span>📩 acre123rvpark@outlook.com</span>
        <span>📍 <a href="https://www.google.com/maps/dir/?api=1&destination=711+Helena+Rd,+Karnes+City,+TX+78118" target="_blank">711 Helena Rd, Kenedy, TX 78118</a></span>
    </div>
""", unsafe_allow_html=True)

# HEADER NAVIGATION
st.markdown(f"""
        <div class="header">
            <div class="header-left">
                <img src="{newlogo_url}" alt="Logo">
                <h2> Welcome to Acre 123 RV Park!</h2>
            </div>
            <div class="nav">
                <a href="#about">About</a>
                <a href="#rates">Rates</a>
                <a href="#amenities">Amenities</a>
                <a href="#park_map">Park Map</a>
                <a class="book-btn" href="#book">BOOK NOW</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

# HERO / BACKGROUND IMAGE
st.markdown("""
    <div class="hero-section">
    </div>
""", unsafe_allow_html=True)

# ABOUT SECTION
st.markdown("""
             <div id="about" style="position: relative; top: -140px;"></div>
    <div id="about" class="about-section">
        <div class="about-title">About</div>
        <div class="about-content">
            <div class="about-text">
                <p>Welcome to Acre 123 RV Park, your peaceful home away from home. We're a family-owned getaway offering comfort, convenience, and a sense of community for every traveler. Whether you're here for a short stay or a few months, we’re proud to host you!</p>
            </div>
            <div class="about-list">
                <ul>
                    <li>Spacious RV Sites</li>
                    <li>Full Hookups</li>
                    <li>On-site Laundry</li>
                    <li>Pet Friendly</li>
                    <li>High-Speed Wi-Fi</li>
                </ul>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# RATES SECTION
st.markdown("""
             <div id="rates" style="position: relative; top: -140px;"></div>
    <div id="rates" class="rates-section">
        <div class="rates-title">Rates</div>
        <div class="rates-table">
            <table>
    <tr>
        <th>Length of Stay</th>
        <th>Price (30A)</th>
        <th>Price (50A)</th>
    </tr>
    <tr>
        <td>Bi-Monthly</td>
        <td>$300</td>
        <td>$350</td>
    </tr>
    <tr>
        <td>Monthly</td>
        <td>$550</td>
        <td>$600</td>
    </tr>
</table>
        </div>
    </div>
""", unsafe_allow_html=True)

#PARK MAP SECTION
st.markdown("""
    <div id="park_map" style="scroll-margin-top: 110px; text-align: center;">
        <h2>Park Map</h2>
        <p>Check which RV sites are currently available. (Availability map coming soon!)</p>
    </div>
""", unsafe_allow_html=True)


# AMENITIES SECTION
st.markdown(f"""
    <style>
    .amenities-section {{
        padding: 3rem 10%;
        text-align: center;
    }}

    .amenities-title {{
        font-size: 2rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 1rem;
    }}

    .amenities-description {{
        font-size: 1.1rem;
        color: #555;
        max-width: 700px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }}

    .amenities {{
        display: flex;
        flex-wrap: wrap;
        gap: 40px;
        justify-content: center;
        margin-top: 2rem;
    }}

    .amenity {{
        text-align: center;
        font-size: 1.1rem;
        color: #333;
    }}

    .amenity img {{
        width: 60px;
        margin-bottom: 0.5rem;
    }}
    </style>
            
     <div id="amenities" style="position: relative; top: -110px;"></div>
    <div id="amenities" class="amenities-section">
        <div class="amenities-title">Amenities</div>
        <div class="amenities-description">
            We offer a variety of on-site amenities to make your stay more comfortable, convenient, and connected. Whether you're traveling solo or with pets, we provide the essentials to help you feel right at home.
        </div>
        <div class="amenities">
            <div class="amenity">
                <img src="{wifi_url}" alt="Wi‑Fi">
                <div>Free Wi‑Fi</div>
            </div>
            <div class="amenity">
                <img src="{dog_url}" alt="Pet Friendly">
                <div>Pet Friendly</div>
            </div>
            <div class="amenity">
                <img src="{laundry_url}" alt="Laundry">
                <div>Laundry Facilities</div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# BOOK NOW SECTION
st.markdown(f"""
             <div id="book" style="position: relative; top: -110px;"></div>
    <div id="book" class="book-section">
        <div class="book-title">Book Now</div>
        <div class="book-content">
            Complete the contact form below and we will be in contact about your stay shortly!
            {contact_form}
""", unsafe_allow_html=True)