import streamlit as st
from PIL import Image

# ============================================
#   CONFIGURAÇÕES DA PÁGINA
# ============================================
st.set_page_config(
    page_title="Magia Personaliza",
    page_icon="✨",
    layout="wide"
)

# ============================================
#   CABEÇALHO DO SITE
# ============================================
st.title("✨ Magia Personaliza")
st.subheader("Personalizados para tornar cada momento único!")

st.write(
    """
    Bem-vindo(a)! Aqui você encontra toppers, lembrancinhas, decorações de bolos  
    e personalizados criados com carinho e qualidade.
    """
)

st.markdown("---")

# ============================================
#   LISTA DE PRODUTOS
# ============================================

st.header("🎁 Produtos disponíveis")

# ---- Lugar para mostrar os produtos que trabalhamos ---- 
product_list = [
    {
        "nome": "Topper de Bolo Personalizado",
        "preco": "R$ 15,00",
        "descricao": "Topper totalmente personalizado com tema, nome e idade.",
        "imagem": "topper.png"   # <-- Substitua pelas imagens reais na pasta do app
    },
    {
        "nome": "Lembrancinhas Personalizadas",
        "preco": "R$ 4,50",
        "descricao": "Lembrancinhas feitas sob medida para festas e eventos.",
        "imagem": "lembrancinha.png"
    },
    {
        "nome": "Caixinhas Decorativas",
        "preco": "R$ 7,00",
        "descricao": "Caixinhas temáticas, perfeitas para presentes e festas.",
        "imagem": "caixinha.png"
    }
]

# ============================================
#   EXIBIR PRODUTOS EM COLUNAS
# ============================================
columns_amount = 3
product_columns = st.columns(columns_amount)

for index, product in enumerate(product_list):
    current_column = product_columns[index % columns_amount]

    with current_column:
        st.markdown(f"### {product['nome']}")

        try:
            product_image = Image.open(product["imagem"])
            st.image(product_image, use_column_width=True)
        except:
            st.warning("Imagem não encontrada (adicione o arquivo na pasta do app).")

        st.markdown(f"**Preço:** {product['preco']}")
        st.caption(product["descricao"])

        whatsapp_link = (
            f"https://wa.me/55DDDNUMERO?text=Olá! Tenho interesse em: {product['nome']}" # numero do wpp
        )

        st.link_button("Falar no WhatsApp", whatsapp_link)


st.markdown("---")

# ============================================
#   CONTATO
# ============================================
st.header("📞 Entre em contato")

st.write(
    """
    Para fazer pedidos, orçamentos ou esclarecer dúvidas, fale diretamente pelo WhatsApp.
    """
)

whatsapp_general = "https://wa.me/55DDDNUMERO?text=Olá! Gostaria de saber mais sobre os personalizados."
st.link_button("📲 Chamar no WhatsApp", whatsapp_general)

st.markdown("---")
st.caption("Site criado com carinho para a Magia Personaliza ✨")
