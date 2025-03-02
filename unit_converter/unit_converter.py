import streamlit as st  # type: ignore

# Length conversion function
def convert_length(value, from_unit, to_unit):
    length_factors = {
        'm': 1,
        'km': 0.001,
        'cm': 100,
        'mm': 1000,
        'inch': 39.3701,
        'ft': 3.28084,
        'yd': 1.09361,
        'mile': 0.000621371
    }
    return value * (length_factors[to_unit] / length_factors[from_unit])

# Weight conversion function
def convert_weight(value, from_unit, to_unit):
    weight_factors = {
        'kg': 1,
        'g': 1000,
        'mg': 1e6,
        'lb': 2.20462,
        'oz': 35.274
    }
    return value * (weight_factors[to_unit] / weight_factors[from_unit])

# Temperature conversion function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'C' and to_unit == 'F':
        return (value * 9/5) + 32
    elif from_unit == 'F' and to_unit == 'C':
        return (value - 32) * 5/9
    elif from_unit == 'C' and to_unit == 'K':
        return value + 273.15
    elif from_unit == 'K' and to_unit == 'C':
        return value - 273.15
    elif from_unit == 'F' and to_unit == 'K':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'K' and to_unit == 'F':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Streamlit app
def main():
    st.title("📏 Unit Converter App By🚀")
    st.title(" ERUM WARIS ")
    st.write("🔄 Conversion between different units of length, weight, and temperature. 🌡️")

    # Select conversion type
    conversion_type = st.selectbox(
        "🎯 Select the type of conversion:",
        ["📏 Length", "⚖️ Weight", "🌡️ Temperature"]
    )

    if conversion_type == "📏 Length":
        st.subheader("📏 Length Conversion")
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("🔢 Enter value:", min_value=0.0)
            from_unit = st.selectbox(
                "📤 From unit:",
                ["m", "km", "cm", "mm", "inch", "ft", "yd", "mile"]
            )
        with col2:
            to_unit = st.selectbox(
                "📥 To unit:",
                ["m", "km", "cm", "mm", "inch", "ft", "yd", "mile"]
            )
        if st.button("🔄 Convert"):
            result = convert_length(value, from_unit, to_unit)
            st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit} 📏")

    elif conversion_type == "⚖️ Weight":
        st.subheader("⚖️ Weight Conversion")
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("🔢 Enter value:", min_value=0.0)
            from_unit = st.selectbox(
                "📤 From unit:",
                ["kg", "g", "mg", "lb", "oz"]
            )
        with col2:
            to_unit = st.selectbox(
                "📥 To unit:",
                ["kg", "g", "mg", "lb", "oz"]
            )
        if st.button("🔄 Convert"):
            result = convert_weight(value, from_unit, to_unit)
            st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit} ⚖️")

    elif conversion_type == "🌡️ Temperature":
        st.subheader("🌡️ Temperature Conversion")
        col1, col2 = st.columns(2)
        with col1:
            value = st.number_input("🔢 Enter value:")
            from_unit = st.selectbox(
                "📤 From unit:",
                ["C", "F", "K"]
            )
        with col2:
            to_unit = st.selectbox(
                "📥 To unit:",
                ["C", "F", "K"]
            )
        if st.button("🔄 Convert"):
            result = convert_temperature(value, from_unit, to_unit)
            st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit} 🌡️")

if __name__ == "__main__":
    main()