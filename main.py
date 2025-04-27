import streamlit as st 
from PIL import Image
import webbrowser

# instalar streamlit -> pip install streamlit
# instalar webbroser???

# Configurações da página
st.set_page_config(
    page_title = "Portfólio - Marcel Bruno", # Adicionando nome na aba do navegador
    page_icon = "📑", # Adicionando icone na aba do navegador
    layout = "wide",
    initial_sidebar_state="expanded"
)

# Cria função para definir estilo css da página
def load_css():
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <style>
            :root {
                --primary-color: #1a365d;
                --secondary-color: #2d547d;
                --accent-color: #38bdf8;
                --text-light: #f8fafc;
                --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }

            .project-card {
                background: white;
                border-radius: 10px;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                box-shadow: var(--shadow);
                transition: all 0.3s ease;
                border: 1px solid rgba(0, 0, 0, 0.1);
            }

            .project-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            }

            .experience-item {
                padding: 1.5rem;
                background: white;
                border-radius: 10px;
                box-shadow: var(--shadow);
                margin-bottom: 1.5rem;
                transition: all 0.3s ease;
            }

            .experience-item:hover {
                transform: translateY(-3px);
            }
        </style>
    """, unsafe_allow_html=True)

    

def app():
    # Chama a função css
    load_css()

    # Configurações sidebar
    with st.sidebar:

        # Configurando parte do nome e ferramentas
        st.markdown("""
                    <div style="text-align: center;">
                        <img src="C:\ProjetosStreamlit\Portfolio\img\img_marcel.png" style="border-radius: 50%; width: 160px; height: 160px; object-fit: cover; margin-bottom: 1rem;">
                        <h2> Marcel Bruno </h2>
                        <p style="color: var(--accent-colo);"> Engenheiro de Dados | Data Engineer </p>
                    </div>

                    """, unsafe_allow_html=True)

        # Configurando a parte de contatos
        with st.expander("📫 Contato", expanded=True):
            st.markdown("""
            
                        <p><i class="fas fa-map-marker-alt"></i> Barueri - SP</i></p>
                        <p><i class="fas fa-phone"></i> +55 21 99999999 </p>
                        <p><i class="fas fa-envelope"></i> marcelbrn@gmail.com </p>
            
                        """, unsafe_allow_html=True)





if __name__ == "__main__":
    app()  

