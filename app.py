import streamlit as st

# =====================================================================
# 1. WARSTWA BEZPIECZEŃSTWA (Ekran blokady)
# =====================================================================
st.sidebar.title("🔐 Autoryzacja")
haslo = st.sidebar.text_input("Wpisz hasło klienta biura:", type="password")

# Definiujemy Twoje tajne hasło dla klientów
TAJNE_HASLO = "Biuro2026!"

if haslo == TAJNE_HASLO:
    st.sidebar.success("🔑 Zalogowano pomyślnie!")
    
    # =====================================================================
    # 2. NAWIGACJA (Menu boczne po zalogowaniu)
    # =====================================================================
    st.sidebar.title("📁 Menu narzędzi")
    wybor_kalkulatora = st.sidebar.radio(
        "Wybierz kalkulator, którego chcesz użyć:",
        ["💰 Kalkulator Wyniku Netto", "🚗 Proporcja Leasingu"]
    )
    
    # =====================================================================
    # 3. ZAKŁADKA 1: KALKULATOR "NA RĘKĘ"
    # =====================================================================
    if wybor_kalkulatora == "💰 Kalkulator Wyniku Netto":
        st.title("💰 Kalkulator Wyniku Netto (Na Rękę)")
        st.write("Oblicz, ile czystego zysku zostaje w Twojej kieszeni po odliczeniu podatków i ZUS.")
        
        # Wejścia danych
        kwota_faktury = st.number_input("Suma wystawionych faktur netto (PLN):", value=15000, step=1000)
        podatek_ppe = st.number_input("Podatek dochodowy / PPE do zapłaty (PLN):", value=1200, step=100)
        skladka_zus = st.number_input("Suma składek ZUS (PLN):", value=1600, step=100)
        koszty_dodatkowe = st.number_input("Inne koszty firmowe netto (PLN):", value=500, step=100)
        
        # Obliczenia
        czysty_zysk = kwota_faktury - podatek_ppe - skladka_zus - koszty_dodatkowe
        
        # Wyjście
        st.write("---")
        st.metric("Kwota, która zostaje Ci na rękę:", f"{czysty_zysk:,.2f} PLN")
        
        if czysty_zysk <= 0:
            st.error("🚨 Ryzyko! Wydatki przewyższają przychód!")
        else:
            st.success("✅ Ta kwota jest bezpieczna do wypłaty.")

    # =====================================================================
    # 4. ZAKŁADKA 2: PROPORCJA LEASINGU
    # =====================================================================
    elif wybor_kalkulatora == "🚗 Proporcja Leasingu":
        st.title("🚗 Kalkulator Proporcji Leasingu (Limit 150 tys. zł)")
        st.write("Sprawdź, jaką część raty leasingowej możesz zaliczyć do kosztów uzyskania przychodu.")
        
        # Wejścia danych
        wartosc_auta = st.number_input("Wartość samochodu (netto + nieodliczony VAT) (PLN):", value=200000, step=10000)
        kwota_raty = st.number_input("Kwota bieżącej raty leasingowej (PLN):", value=2000, step=100)
        
        LIMIT = 150000
        
        # Obliczenia i logika
        if wartosc_auta > LIMIT:
            proporcja = LIMIT / wartosc_auta
            st.warning(f"⚠️ Auto przekracza limit. Proporcja kosztów: {proporcja * 100:.2f}%")
        else:
            proporcja = 1.0
            st.success("✅ Auto mieści się w limicie. Odliczasz 100% kosztów.")
            
        kup_w_koszty = kwota_raty * proporcja
        kup_strata = kwota_raty - kup_w_koszty
        
        # Wyjście
        st.write("---")
        kol1, col2 = st.columns(2)
        kol1.metric("Kwota w KUP (Koszty):", f"{kup_w_koszty:,.2f} PLN")
        col2.metric("Kwota NKUP (Strata):", f"{kup_strata:,.2f} PLN")

# =====================================================================
# 5. EKRAN BLOKADY (Gdy hasło jest błędne lub puste)
# =====================================================================
else:
    st.title("🔒 Panel Klienta Biura Rachunkowego")
    st.info("System jest zabezpieczony. Aby uzyskać dostęp do kalkulatorów biznesowych, wprowadź hasło w panelu po lewej stronie.")
    if haslo != "":
        st.error("❌ Niepoprawne hasło! Spróbuj ponownie.")
