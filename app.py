import streamlit as st

# Ustawienia strony
st.set_page_config(page_title="Panel Klienta Biura", page_icon="📊", layout="wide")

# =====================================================================
# 1. LOGO I AUTORYZACJA (Pasek boczny w głębokim granacie)
# =====================================================================
# TUTAJ PODMIEŃ LINK na prawdziwe logo Twojego biura:
LINK_DO_LOGO = "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=150" # Tymczasowa profesjonalna ikona biznesowa

st.sidebar.image(LINK_DO_LOGO, use_container_width=True)
st.sidebar.divider()

st.sidebar.subheader("🔐 Autoryzacja")
haslo = st.sidebar.text_input("Wpisz hasło klienta:", type="password")

TAJNE_HASLO = "Biuro2026!"

if haslo == TAJNE_HASLO:
    st.sidebar.success("🔑 Zalogowano pomyślnie!")
    
    # =====================================================================
    # 2. NAWIGACJA
    # =====================================================================
    st.sidebar.divider()
    st.sidebar.subheader("📁 Dostępne narzędzia")
    wybor_kalkulatora = st.sidebar.radio(
        "Wybierz analizę:",
        ["💰 Wynik Netto (Na Rękę)", "🚗 Proporcja Leasingu"]
    )
    
    # =====================================================================
    # 3. KALKULATOR "NA RĘKĘ"
    # =====================================================================
    if wybor_kalkulatora == "💰 Wynik Netto (Na Rękę)":
        st.title("💰 Inteligentny Kalkulator Wyniku Netto")
        st.write("Przeanalizuj swoje realne przepływy pieniężne w tym miesiącu.")
        st.divider()
        
        col_in1, col_in2 = st.columns(2)
        with col_in1:
            kwota_faktury = st.number_input("Suma faktur przychodowych netto (PLN):", value=15000, step=1000)
            podatek_ppe = st.number_input("Podatek dochodowy / PPE do zapłaty (PLN):", value=1200, step=100)
        with col_in2:
            skladka_zus = st.number_input("Suma składek ZUS (PLN):", value=1600, step=100)
            koszty_dodatkowe = st.number_input("Inne koszty firmowe netto (PLN):", value=500, step=100)
        
        czysty_zysk = kwota_faktury - podatek_ppe - skladka_zus - koszty_dodatkowe
        suma_danin = podatek_ppe + skladka_zus
        
        st.divider()
        st.subheader("📊 Twój raport płynności finansowej")
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Przychód operacyjny", f"{kwota_faktury:,.2f} PLN")
        c2.metric("Suma danin (ZUS + Podatki)", f"{suma_danin:,.2f} PLN")
        
        procent_zysku = (czysty_zysk * 100 / kwota_faktury) if kwota_faktury > 0 else 0
        c3.metric("Zostaje w kieszeni (Na Rękę)", f"{czysty_zysk:,.2f} PLN", delta=f"{procent_zysku:.1f}% przychodu")
        
        st.write("")
        if czysty_zysk <= 0:
            st.error("🚨 Ryzyko! Koszty i daniny przewyższają Twój przychód.")
        else:
            st.success("✅ Płynność bezpieczna. Tę kwotę możesz bezpiecznie przetransferować na konto prywatne.")

    # =====================================================================
    # 4. PROPORCJA LEASINGU
    # =====================================================================
    elif wybor_kalkulatora == "🚗 Proporcja Leasingu":
        st.title("🚗 Kalkulator Limitu i Proporcji Leasingu")
        st.write("Automatyczne rozliczenie kosztów dla samochodów osobowych z uwzględnieniem typu napędu.")
        st.divider()
        
        col_le1, col_le2 = st.columns(2)
        with col_le1:
            wartosc_auta = st.number_input("Wartość auta (netto + nieodliczony VAT) (PLN):", value=200000, step=10000)
            typ_napedu = st.selectbox("Wybierz rodzaj napędu auta:", ["Spalinowy / Hybryda", "Elektryczny (EV)"])
        with col_le2:
            kwota_raty = st.number_input("Kwota faktury za ratę leasingową (PLN):", value=2000, step=100)
        
        if typ_napedu == "Elektryczny (EV)":
            LIMIT = 225000
        else:
            LIMIT = 100000
        
        if wartosc_auta > LIMIT:
            proporcja = LIMIT / wartosc_auta
            st.warning(f"⚠️ Pojazd przekracza przyjęty limit {LIMIT:,.2f} zł dla aut typu: {typ_napedu}. Proporcja odliczenia: **{proporcja * 100:.2f}%**")
        else:
            proporcja = 1.0
            st.success(f"✅ Pojazd mieści się w przyjętym limicie {LIMIT:,.2f} zł dla aut typu: {typ_napedu}. Odliczasz **100%** wartości raty.")
            
        kup_w_koszty = kwota_raty * proporcja
        kup_strata = kwota_raty - kup_w_koszty
        
        st.divider()
        st.subheader("🎯 Dekretacja księgowa dla bieżącej raty")
        
        col_m1, col_m2 = st.columns(2)
        col_m1.metric("KUP (Koszty Uzyskania Przychodu)", f"{kup_w_koszty:,.2f} PLN")
        col_m2.metric("NKUP (Koszty niestanowiące przychodu)", f"{kup_strata:,.2f} PLN")
        
        with st.expander("ℹ️ Zobacz specyfikację wyliczenia"):
            st.write(f"Koszty rozliczane są proporcją wynikającą z limitu kwotowego {LIMIT:,.2f} PLN w stosunku do całkowitej wartości początkowej pojazdu.")

# =====================================================================
# 5. EKRAN BLOKADY (Brak hasła)
# =====================================================================
else:
    st.title("🔒 Portal Finansowy Klientów Biura")
    st.info("Dostęp zabezpieczony certyfikatem. Wprowadź uniwersalne hasło w panelu bocznym po lewej stronie, aby odblokować narzędzia analityczne.")
    if haslo != "":
        st.error("❌ Błędne hasło autoryzacyjne. Spróbuj ponownie.")
