import streamlit as st

st.set_page_config(page_title="Acre 123 RV Park", layout="wide", page_icon="assets/newlogo.png")

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
     <input type="text" name="Name" placeholder="Your full name" required>
     <input type="email" name="Email" placeholder="Your email" required>
     <input type="phone" name="Phone" placeholder="Your phone number" required>
     <textarea name="Message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
     <input type="hidden" name="_autoresponse" value="Your inquiry has been received and we will be in contact with you shortly!">
</form>
"""



# IMAGE URLs (replace with your actual GitHub raw URLs)
newlogo_url = "https://raw.githubusercontent.com/G5ProjectsLLC/Acre-123-RV-Park/main/assets/newlogo.png"
wifi_url = "https://raw.githubusercontent.com/G5ProjectsLLC/Acre-123-RV-Park/main/assets/wifi.png"
dog_url = "https://raw.githubusercontent.com/G5ProjectsLLC/Acre-123-RV-Park/main/assets/dog.png"
laundry_url = "https://raw.githubusercontent.com/G5ProjectsLLC/Acre-123-RV-Park/main/assets/laundry.png"
map_url = "https://raw.githubusercontent.com/G5ProjectsLLC/Acre-123-RV-Park/main/assets/map.png"


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

    /* Contact Bar fixed - Modern South Texas Style */
    .contact-bar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: linear-gradient(135deg, #8B6F47 0%, #A0826D 100%);
        color: #F5F1E8;
        font-size: 0.9rem;
        padding: 10px 20px;
        display: flex;
        justify-content: flex-end;
        gap: 30px;
        z-index: 1001;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    }}
    .contact-bar span {{
        display: flex;
        align-items: center;
        gap: 8px;
        font-weight: 500;
    }}
    .contact-bar a {{
        color: #F5F1E8;
        text-decoration: none;
        transition: color 0.3s ease;
    }}
    .contact-bar a:hover {{
        color: #FFD700;
        text-decoration: none;
    }}

    /* Header fixed directly under contact bar - Modern Design */
    .header {{
        position: fixed;
        top: 40px;
        left: 0;
        width: 100%;
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(10px);
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 1.2rem 3rem;
        border-bottom: 2px solid rgba(139, 111, 71, 0.1);
        z-index: 1000;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
    }}
    .header-left {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}
    .header-left img {{
        height: 55px;
        margin-right: 0;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    }}
    .header-left h2 {{
        margin: 0;
        font-size: 1.5rem;
        font-weight: 700;
        color: #5C4A37;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        letter-spacing: -0.5px;
    }}
    .nav {{
        display: flex;
        gap: 8px;
        align-items: center;
    }}
    .nav a {{
        text-decoration: none;
        font-weight: 600;
        color: #5C4A37;
        padding: 10px 18px;
        border-radius: 8px;
        transition: all 0.3s ease;
        font-size: 0.95rem;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    }}
    .nav a:hover {{
        background: linear-gradient(135deg, #F5E6D3 0%, #E8D5C0 100%);
        color: #8B6F47;
        transform: translateY(-2px);
    }}
    .book-btn {{
        background: linear-gradient(135deg, #C9A961 0%, #B8945F 100%);
        color: white !important;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: 700;
        box-shadow: 0 4px 15px rgba(201, 169, 97, 0.3);
        transition: all 0.3s ease;
        font-size: 0.95rem;
    }}
    .book-btn:hover {{
        background: linear-gradient(135deg, #D4B570 0%, #C9A961 100%);
        box-shadow: 0 6px 20px rgba(201, 169, 97, 0.4);
        transform: translateY(-2px);
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
        margin-top: 120px; /* Adjusted for new header height */
    }}

    /* Modern Form styling */
    input[type=text], input[type=email], input[type=phone], textarea {{
      width: 100%;
      max-width: 600px;
      padding: 14px 18px;
      border: 2px solid #E0D4C0;
      border-radius: 10px;
      box-sizing: border-box;
      margin-top: 8px;
      margin-bottom: 20px;
      resize: vertical;
      font-size: 1rem;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      background-color: #FAF8F3;
      transition: all 0.3s ease;
      color: #5C4A37;
    }}
    input[type=text]:focus, input[type=email]:focus, input[type=phone]:focus, textarea:focus {{
      outline: none;
      border-color: #C9A961;
      background-color: #FFFFFF;
      box-shadow: 0 0 0 3px rgba(201, 169, 97, 0.1);
    }}
    button[type=submit] {{
      background: linear-gradient(135deg, #C9A961 0%, #B8945F 100%);
      color: white;
      padding: 14px 32px;
      border: none;
      border-radius: 10px;
      cursor: pointer;
      display: block;
      margin: 20px auto 0 auto;
      font-size: 1.05rem;
      font-weight: 600;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      box-shadow: 0 4px 15px rgba(201, 169, 97, 0.3);
      transition: all 0.3s ease;
    }}
    button[type=submit]:hover {{
      background: linear-gradient(135deg, #D4B570 0%, #C9A961 100%);
      box-shadow: 0 6px 20px rgba(201, 169, 97, 0.4);
      transform: translateY(-2px);
    }}

    /* Mobile responsive adjustments */
    @media (max-width: 768px) {{
        .contact-bar {{
            font-size: 0.75rem;
            padding: 8px 15px;
            gap: 15px;
            flex-wrap: wrap;
            justify-content: center;
        }}
        .header {{
            flex-direction: column;
            align-items: flex-start;
            padding: 1rem 1.5rem;
            top: auto;
        }}
        .header-left h2 {{
            font-size: 1.2rem;
        }}
        .nav {{
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
            width: 100%;
        }}
        .nav a {{
            padding: 8px 14px;
            font-size: 0.9rem;
        }}
        .book-btn {{
            padding: 10px 20px;
            font-size: 0.9rem;
        }}
        .about-section {{
            padding: 0 5% !important;
        }}
        .about-content, .book-content, .amenities-description {{
            padding: 1.5rem;
            max-width: 100%;
            box-sizing: border-box;
        }}
        .about-text, .about-list {{
            min-width: 100%;
            max-width: 100%;
            font-size: 1rem;
        }}
        .rates-table {{
            font-size: 1rem;
        }}
        .rates-table th, .rates-table td {{
            padding: 12px 15px;
        }}
        .hero-section, .about-section, .rates-section, .amenities-section, .park_map-section, .book-section {{
            margin-top: 180px;
        }}
    }}
    </style>

    <!-- Contact Bar -->
    <div class="contact-bar">
        <span>📞 <a href="tel:8305835739">830-583-5739</a></span>
        <span>📩 acre123rvpark@outlook.com</span>
        <span>📍 <a href="https://www.google.com/maps/dir/?api=1&destination=711+Helena+Rd,+Karnes+City,+TX+78118" target="_blank">711 Helena Rd, Karnes City, TX 78118</a></span>
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
    /* App-wide background - Modern South Texas Palette */
    html, body, .stApp, [data-testid="stAppViewContainer"] {{
        background: linear-gradient(180deg, #F5F1E8 0%, #F0E8D8 100%) !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
    }}
    /* Make Streamlit's block container transparent so the page background shows */
    main [data-testid="block-container"] {{
        background-color: transparent !important;
        padding-top: 0rem !important;
    }}
    /* Optional: remove default Streamlit header background if visible */
    header[role="banner"], header[data-testid="stHeader"] {{
        background: transparent !important;
    }}

    
    /* Hero Background - Modern Design */
    .hero-section {{
        background-image: url('{newlogo_url}');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: top center;
        height: 500px;
        display: flex;
        align-items: flex-start;
        justify-content: center;
        color: #8B6F47;
        text-shadow: 0 2px 8px rgba(255,255,255,0.8);
        font-size: 2.2rem;
        font-weight: 700;
        padding-top: 20px;
        margin-bottom: 3rem;
        position: relative;
    }}
    .hero-section::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(180deg, rgba(245, 241, 232, 0.3) 0%, rgba(240, 232, 216, 0.5) 100%);
        pointer-events: none;
    }}

    /* About Section - Modern Card Design */
    .about-section {{
        margin: 4rem 0;
        padding: 0 10%;
    }}
    .about-title {{
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 3rem;
        color: #5C4A37;
        letter-spacing: -0.5px;
        position: relative;
        padding-bottom: 1rem;
    }}
    .about-title::after {{
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, #C9A961 0%, #B8945F 100%);
        border-radius: 2px;
    }}
    .about-content {{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        gap: 50px;
        flex-wrap: wrap;
        background: rgba(255, 255, 255, 0.7);
        padding: 3rem;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        backdrop-filter: blur(10px);
    }}
    .about-text, .about-list {{
        flex: 1;
        min-width: 280px;
        font-size: 1.1rem;
        color: #5C4A37;
        line-height: 1.8;
        word-wrap: break-word;
        overflow-wrap: break-word;
        max-width: 100%;
    }}
    .about-text {{
        line-height: 1.8;
    }}
    .about-text p {{
        word-wrap: break-word;
        overflow-wrap: break-word;
        max-width: 100%;
    }}
    .about-list ul {{
        padding-left: 0;
        list-style: none;
    }}
    .about-list li {{
        padding: 12px 0;
        padding-left: 30px;
        position: relative;
        font-size: 1.05rem;
    }}
    .about-list li::before {{
        content: '✓';
        position: absolute;
        left: 0;
        color: #C9A961;
        font-weight: bold;
        font-size: 1.2rem;
    }}

    /* Rates Section - Modern Table Design */
    .rates-section {{
        margin: 4rem 0;
        padding: 0 10%;
    }}
    .rates-title {{
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 3rem;
        color: #5C4A37;
        letter-spacing: -0.5px;
        position: relative;
        padding-bottom: 1rem;
    }}
    .rates-title::after {{
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, #C9A961 0%, #B8945F 100%);
        border-radius: 2px;
    }}
    .rates-table {{
        font-size: 1.15rem;
        margin: 0 auto;
        max-width: 600px;
        color: #5C4A37;
    }}
    .rates-table table {{
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        background: rgba(255, 255, 255, 0.7);
        border-radius: 16px;
        overflow: hidden;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
    }}
    .rates-table th {{
        padding: 20px;
        background: linear-gradient(135deg, #8B6F47 0%, #A0826D 100%);
        color: #F5F1E8;
        text-align: left;
        font-weight: 700;
        font-size: 1.1rem;
    }}
    .rates-table th:first-child {{
        border-top-left-radius: 16px;
    }}
    .rates-table th:last-child {{
        border-top-right-radius: 16px;
    }}
    .rates-table td {{
        padding: 18px 20px;
        border-bottom: 1px solid rgba(139, 111, 71, 0.1);
        text-align: left;
        background: rgba(255, 255, 255, 0.9);
    }}
    .rates-table tr:last-child td {{
        border-bottom: none;
    }}
    .rates-table tr:hover td {{
        background: rgba(245, 230, 211, 0.5);
    }}

    /* Amenities Section - Modern Card Layout */
    .amenities {{
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        justify-content: center;
        margin: 3rem 0;
    }}
    .amenity {{
        text-align: center;
        font-size: 1.15rem;
        color: #5C4A37;
        background: rgba(255, 255, 255, 0.7);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
        min-width: 180px;
        font-weight: 600;
    }}
    .amenity:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
        background: rgba(255, 255, 255, 0.9);
    }}
    .amenity-wifi {{
        background: #FFFFFF !important;
    }}
    .amenity-wifi:hover {{
        background: #FFFFFF !important;
    }}
    .amenity-wifi img {{
        filter: none !important;
    }}
    .amenity-dog {{
        background: #FFFFFF !important;
    }}
    .amenity-dog:hover {{
        background: #FFFFFF !important;
    }}
    .amenity-dog img {{
        filter: none !important;
    }}
    .amenity img {{
        width: 70px;
        margin-bottom: 1rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    }}

    
    /* Book Now Section - Modern Design */
    .book-section {{
        margin: 4rem 0;
        padding: 0 10%;
        text-align: center;
    }}
    .book-title {{
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        color: #5C4A37;
        letter-spacing: -0.5px;
        position: relative;
        padding-bottom: 1rem;
    }}
    .book-title::after {{
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, #C9A961 0%, #B8945F 100%);
        border-radius: 2px;
    }}
    .book-content {{
        font-size: 1.15rem;
        color: #5C4A37;
        line-height: 1.8;
        max-width: 800px;
        margin: 0 auto 2.5rem auto;
        background: rgba(255, 255, 255, 0.7);
        padding: 2.5rem;
        border-radius: 20px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
    }}
    .book-content a {{
        color: #8B6F47;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }}
    .book-content a:hover {{
        color: #C9A961;
        text-decoration: none;
    }}
    



    </style>
""", unsafe_allow_html=True)

# CONTACT BAR
st.markdown("""
    <div class="contact-bar">
        <span>📞 <a href="tel:8305835739">830-583-5739</a></span>
        <span>📩 acre123rvpark@outlook.com</span>
        <span>📍 <a href="https://www.google.com/maps/dir/?api=1&destination=711+Helena+Rd,+Karnes+City,+TX+78118" target="_blank">711 Helena Rd, Karnes City, TX 78118</a></span>
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

#Hides Streamlit Header#
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

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
        <td>Weekly</td>
        <td>$185</td>
        <td>$185</td>
    </tr>
    <tr>
        <td>Monthly</td>
        <td>$540 (plus electricity)</td>
        <td>$580 (plus electricity)</td>
    </tr>
</table>
        </div>
    </div>
""", unsafe_allow_html=True)


# AMENITIES SECTION
st.markdown(f"""
    <style>
    .amenities-section {{
        padding: 4rem 10%;
        text-align: center;
    }}

    .amenities-title {{
        font-size: 2.5rem;
        font-weight: 700;
        color: #5C4A37;
        margin-bottom: 1.5rem;
        letter-spacing: -0.5px;
        position: relative;
        padding-bottom: 1rem;
    }}
    .amenities-title::after {{
        content: '';
        position: absolute;
        bottom: 0;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, #C9A961 0%, #B8945F 100%);
        border-radius: 2px;
    }}

    .amenities-description {{
        font-size: 1.15rem;
        color: #5C4A37;
        max-width: 750px;
        margin: 0 auto 3rem auto;
        line-height: 1.8;
        background: rgba(255, 255, 255, 0.5);
        padding: 2rem;
        border-radius: 16px;
    }}

    .amenities {{
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        justify-content: center;
        margin-top: 2rem;
    }}

    .amenity {{
        text-align: center;
        font-size: 1.15rem;
        color: #5C4A37;
        background: rgba(255, 255, 255, 0.7);
        padding: 2rem 2.5rem;
        border-radius: 16px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
        transition: all 0.3s ease;
        min-width: 180px;
        font-weight: 600;
    }}
    .amenity:hover {{
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.12);
        background: rgba(255, 255, 255, 0.9);
    }}
    .amenity-wifi {{
        background: #FFFFFF !important;
    }}
    .amenity-wifi:hover {{
        background: #FFFFFF !important;
    }}
    .amenity-wifi img {{
        filter: none !important;
    }}
    .amenity-dog {{
        background: #FFFFFF !important;
    }}
    .amenity-dog:hover {{
        background: #FFFFFF !important;
    }}
    .amenity-dog img {{
        filter: none !important;
    }}

    .amenity img {{
        width: 70px;
        margin-bottom: 1rem;
        filter: drop-shadow(0 2px 4px rgba(0,0,0,0.1));
    }}
    </style>
            
     <div id="amenities" style="position: relative; top: -110px;"></div>
    <div id="amenities" class="amenities-section">
        <div class="amenities-title">Amenities</div>
        <div class="amenities-description">
            We offer a variety of on-site amenities to make your stay more comfortable, convenient, and connected. Whether you're traveling solo or with pets, we provide the essentials to help you feel right at home.
        </div>
        <div class="amenities">
            <div class="amenity amenity-wifi">
                <img src="{wifi_url}" alt="Wi‑Fi">
                <div>Free Wi‑Fi</div>
            </div>
            <div class="amenity amenity-dog">
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

# Park Map Section

# Anchor for smooth scrolling offset
st.markdown('<div id="park_map" style="scroll-margin-top: 80px;"></div>', unsafe_allow_html=True)

# Section title, centered - Modern Style
st.markdown("""
    <div style="text-align: center; margin: 4rem 0 3rem 0;">
        <h2 style='font-size: 2.5rem; font-weight: 700; color: #5C4A37; letter-spacing: -0.5px; margin-bottom: 1rem; position: relative; padding-bottom: 1rem; display: inline-block;'>
            Park Map
            <span style="position: absolute; bottom: 0; left: 50%; transform: translateX(-50%); width: 80px; height: 4px; background: linear-gradient(90deg, #C9A961 0%, #B8945F 100%); border-radius: 2px;"></span>
        </h2>
    </div>
""", unsafe_allow_html=True)

# URL of the map image on GitHub
park_map_url = "https://raw.githubusercontent.com/G5ProjectsLLC/Acre-123-RV-park/main/assets/map.png"

# Display the image in a centered, responsive container - Modern Card Style
st.markdown(
    f"""
    <div style="display: flex; justify-content: center; margin-bottom: 4rem;">
        <div style="background: rgba(255, 255, 255, 0.7); padding: 2rem; border-radius: 20px; box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);">
            <img src="{park_map_url}" style="max-width: 100%; height: auto; border-radius: 12px;" alt="Acre 123 RV Park Map">
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# BOOK NOW SECTION
st.markdown(f"""
             <div id="book" style="position: relative; top: -110px;"></div>
    <div id="book" class="book-section">
        <div class="book-title">Book Now</div>
        <div class="book-content">
            Please complete the contact form below and we will be in contact about your stay shortly!
            {contact_form}
""", unsafe_allow_html=True)