import streamlit as st
from dashboard_pages.home import home
from dashboard_pages.profile import profile
from dashboard_pages.settings import settings

def dashboard(user):
    # Initialize session state for dashboard page if it doesn't exist
    if 'dashboard_page' not in st.session_state:
        st.session_state['dashboard_page'] = 'home'

    # Custom CSS for styling
    st.markdown("""
    <style>
        h1 {
            text-shadow: 2px 2px 6px rgba(168, 168, 168, 1);
        }
        [data-testid=stSidebar] {
            background-color: #6EE7B7;
        }
        .stButton button{
                display: flex;  
                margin: 10px auto;
        }
        .stButton button:hover{
                color:black;
                transition: 0.5s;
                transform: scale(1.1);
        }
        .stButton button span {
            font-size: 2.5rem;
            margin-right: 20px;
            text-align: center;
            text-shadow: 2px 2px 6px rgba(100, 100, 100, 1);
        }
        .stButton button div {
            font-size: 1.25rem;
            text-align: center;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Sidebar with navigation buttons
    with st.sidebar:
        # Home button
        st.button("Home", type="tertiary", icon=":material/home:", on_click=lambda: st.session_state.update({"dashboard_page": "home"}))
        
        st.divider()
        
        # CSV Import button
        st.button("CSV Import", type="tertiary", icon=":material/download:", on_click=lambda: st.session_state.update({"dashboard_page": "csv_import"}))
        
        st.divider()
        
        # Profile button
        st.button("Profile", type="tertiary", icon=":material/person:", on_click=lambda: st.session_state.update({"dashboard_page": "profile"}))
        
        st.divider()
        
        # Settings button
        st.button("Settings", type="tertiary", icon=":material/settings:", on_click=lambda: st.session_state.update({"dashboard_page": "settings"}))
    
    # Display the appropriate page based on session state
    if st.session_state['dashboard_page'] == 'home':
        home(user)
    elif st.session_state['dashboard_page'] == 'profile':
        profile(user)
    elif st.session_state['dashboard_page'] == 'settings':
        settings(user)
    elif st.session_state['dashboard_page'] == 'csv_import':
        st.title("CSV Import Page")  # Placeholder for CSV Import page

if __name__ == "__main__":
    dashboard("User")