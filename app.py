import streamlit as st 

# Configurações da página
st.set_page_config(
    page_title = "Portfólio - Marcel Bruno", # Adicionando nome na aba do navegador
    page_icon = "📑", # Adicionando icone na aba do navegador
    layout = "wide",
    initial_sidebar_state="expanded"
)

# Gerando informações dos links para as redes sociais
links_redes_sociais = {
    "LinkedIn": {"url": "https://www.linkedin.com/in/marcel-bruno/", "icon": "fab fa-linkedin"},
    "GitHub": {"url": "https://github.com/Marcelbrn/", "icon": "fab fa-github"}
}

# Gerando informações para o quadro de Habilidades
habilidades_tecnicas = {
    "Linguagens & Desenvolvimento": ["SAS", "SQL", "Python, PySpark, Shell Script", "DBT"],
    "BD & Armazenamento": ["SQL Server, Oracle, Teradata", "MongoDB, Cassandra", "Data Warehouse", "Data Lake"],
    "Ferramentas & Orquestração": ["Airflow", "Docker, Kubernetes","Terraform, CI/CD", "Streamlit, Power BI"],
    "Cloud & Processamento": ["AWS, Azure, GCP", "Databricks", "Snowflake", "BigQuery"]
}

# Gerando informações para o quadro de Projetos
projetos = [
    {
        "titulo": "Portfólio",
        "url": "https://github.com/Marcelbrn/marcel-portfolio/tree/main",
        "descricao": "Implementação de página web para apresentação de portfólio profissional, destacando projetos, habilidades e experiências."
    }
]

# Gerando informações para o quadro de Certificações
certificacoes = [
    {
        "img": "https://github.com/Marcelbrn/marcel-portfolio/raw/7d7f1e5dbff9ed1d6370e929c5ae8e4440233a58/img/img_certificacao_microsoft.png",
        "tipo": "Microsoft Certified:",
        "certificacao": "AZ-900",
        "url": ""
    },
    {
        "img": "https://github.com/Marcelbrn/marcel-portfolio/raw/8d7506d39ae93358dd1ed90503e2bdb0cae09f3b/img/img_certificacao_sas.png",
        "tipo": "SAS Certified Professional:",
        "certificacao": "Advanced Programming Using SAS 9.4",
        "url": "https://www.credly.com/badges/3e324c11-c28b-46aa-be33-0e780f9a4fcd/linked_in_profile"
    },
    {
        "img": "https://github.com/Marcelbrn/marcel-portfolio/raw/8d7506d39ae93358dd1ed90503e2bdb0cae09f3b/img/img_certificacao_sas.png",
        "tipo": "SAS Certified Specialist:",
        "certificacao": "Base Programming Using SAS 9.4",
        "url": "https://www.credly.com/badges/603b630f-203c-43a8-a568-6384de851889/linked_in"
    },
    {
        "img": "https://github.com/Marcelbrn/marcel-portfolio/raw/8d7506d39ae93358dd1ed90503e2bdb0cae09f3b/img/img_certificacao_sas.png",
        "tipo": "SAS Certified:",
        "certificacao": "Base Programmer for SAS 9",
        "url": "https://www.youracclaim.com/badges/b2d53d81-f4d4-4f24-af0a-322c2b673020/linked_in_profile"
    }
]

# Cria função para definir estilo css da página
def f_load_css():
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

# Cria função para links da rede sociais
def f_links_redes_sociais():
    link_html = "".join(
        f'<a href={info["url"]} target="_blank" style="margin: 0 10px; font-size: 1.5rem; color: var(--primaty-color);">'
        f'<i class="{info["icon"]}"></i></a>'
        for name, info in links_redes_sociais.items()
    )
    st.markdown(f'<div style="text-align: center; margin: 2rem 0;">{link_html}</div>', unsafe_allow_html=True)

# Cria função para os projetos
def f_projetos():
    st.markdown("## 👨🏻‍💻 Projetos")
    cols = st.columns(4)
    for idx, projeto in enumerate(projetos):
        with cols[idx % 4]:

            st.markdown(f"""
                            <div class="project-card">
                                <h4><a href="{projeto['url']}" target="_blank">{projeto['titulo']}</a></h4>
                                <p>{projeto['descricao']}</p>
                            </div>
                        """, unsafe_allow_html=True)

# Cria função para as certificações
def f_certificacoes():
    st.markdown("## 🏅 Certificações")
    cols = st.columns(4)
    for idx, cert in enumerate(certificacoes):
        with cols[idx % 4]:

            st.markdown(f"""
                            <div style="text-align: center; margin: 20px 0;">
                                <a href="{cert['url']}" target="_blank">
                                    <img src="{cert['img']}" width="120">
                                </a>
                                <h5>{cert['tipo']}</h5>
                                <p style="margin-top: -10px;">{cert['certificacao']}</p>
                            </div>
                        """, unsafe_allow_html=True)     

# Função principal da aplicação 
def app():
    # Configurado estilos CSS
    f_load_css()

    # Configuração sidebar 
    with st.sidebar:

        # Configurando parte do nome, título e imagem de perfil
        st.markdown("""
                        <div style="text-align: center;">
                            <img src="https://github.com/Marcelbrn/marcel-portfolio/raw/6721ec536e4cdd14fa4748889c45cfd9ef3a00c0/img/img_marcel.png" style="border-radius: 50%; width: 240px; height: 240px; object-fit: cover; margin-bottom: 1rem;">
                            <h1> Marcel Bruno </h1>
                            <p style="color: var(--accent-colo);"> Engenheiro de Dados </p>
                        </div>
                    """, unsafe_allow_html=True)

        # Configurando a parte de contatos
        with st.expander("📫 Contato", expanded=True):
            st.markdown("""
                            <p><i class="fas fa-map-marker-alt"></i> Barueri - SP</i></p>
                            <p><i class="fas fa-phone"></i> +55 21 999999999 </p>
                            <p><i class="fas fa-envelope"></i> marcelbrn@gmail.com </p>
                        """, unsafe_allow_html=True)


        # Chamando a função de links das redes sociais
        f_links_redes_sociais()


    # Configuração container
    with st.container():
        col1, col2 = st.columns([3,1])

        # Configurando o texto 'sobre mim' e imagem
        with col1:
            st.markdown("""## 👋🏻 Olá, sou Marcel Bruno""", unsafe_allow_html=True)
            st.markdown("""Profissional de Engenharia de Dados, com aproximadamente 8 anos de experiência no desenvolvimento de pipelines de dados, especializado em programação SAS. Atualmente, estou ampliando meus conhecimentos em engenharia de dados, explorando novas linguagens, ferramentas e tecnologias em nuvem para fortalecer ainda mais minha atuação no universo de dados. Além da carreira, sou pai do Heitor e também dos meus pets Thor, Pandora e Tico, gosto de estudar sobre plantas medicinais e cultivo uma vida espiritualizada, buscando equilíbrio e aprendizado contínuo em todas as áreas da vida.""", unsafe_allow_html=True)

        # Adicionando imagem ao lado do texto 'sobre mim'
        with col2:
            st.image("https://github.com/Marcelbrn/marcel-portfolio/raw/6318010389277bad826acee2d15f26774bd0ce21/img/img_dados.png", width=200)

        # Configurando parte das habilidades
        st.markdown("## 🛠️ Habilidades Técnicas")
        cols = st.columns(4)
        for idx, (title, items) in enumerate(habilidades_tecnicas.items()):
            with cols[idx]:
                lista_habilidades = "".join(f"<li>{item}</li>" for item in items)

                st.markdown(f"""
                                <div style="padding: 1.5rem; background: white; border-radius: 10px; box-shadow: var(--shadow);">
                                    <h5>{title}</h5>
                                    <ul>{lista_habilidades}</ul>
                                </div><br>
                            """, unsafe_allow_html=True)

        # Configurando parte dos projetos
        f_projetos()

        # Configurando parte das certificações
        f_certificacoes()

# Executa a aplicação
if __name__ == "__main__":
    app()  

