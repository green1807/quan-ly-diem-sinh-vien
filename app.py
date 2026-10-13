import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Dữ liệu ban đầu
data = {
    'Ho_ten': ['Nguyễn Văn An', 'Trần Thị Bình', 'Lê Hoàng Chi', 'Phạm Quốc Dũng', 'Vũ Thị Hà', 
               'Đỗ Ngọc Lan', 'Bùi Văn Minh', 'Hoàng Tấn Nam', 'Đặng Hồng Phúc', 'Ngô Thị Trang'],
    'Chuyen_can': [8.5, 9.0, 7.0, 9.5, 8.0, 6.0, 9.0, 7.5, 8.0, 9.5],
    'Giua_ky': [7.5, 8.5, 6.5, 9.0, 7.0, 5.5, 8.5, 6.5, 7.5, 9.0],
    'Cuoi_ky': [8.0, 8.5, 6.5, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.0]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết và xếp loại
df['Tong_ket'] = (0.2 * df['Chuyen_can'] + 0.3 * df['Giua_ky'] + 0.5 * df['Cuoi_ky']).round(2)

def xep_loai(score):
    if score >= 8.5: return 'Giỏi'
    elif score >= 7.0: return 'Khá'
    elif score >= 5.0: return 'Trung bình'
    else: return 'Yếu'

df['Xep_loai'] = df['Tong_ket'].apply(xep_loai)

# 2. Thiết kế giao diện Web App bằng Streamlit
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

st.subheader("Bảng điểm chi tiết của 10 sinh viên")
st.dataframe(df)

st.subheader("Thống kê chung")
dtb_lop = round(df['Tong_ket'].mean(), 2)
so_sv_dat = (df['Tong_ket'] >= 5.0).sum()
sv_max = df.loc[df['Tong_ket'].idxmax()]
sv_min = df.loc[df['Tong_ket'].idxmin()]

col1, col2 = st.columns(2)
col1.metric("Điểm trung bình lớp", dtb_lop)
col2.metric("Số sinh viên đạt (>= 5.0)", f"{so_sv_dat}/10")

st.write(f"**Sinh viên điểm cao nhất:** {sv_max['Ho_ten']} ({sv_max['Tong_ket']} điểm)")
st.write(f"**Sinh viên điểm thấp nhất:** {sv_min['Ho_ten']} ({sv_min['Tong_ket']} điểm)")

st.subheader("Tra cứu điểm theo sinh viên")
selected_student = st.selectbox("Chọn tên sinh viên:", df['Ho_ten'])
student_info = df[df['Ho_ten'] == selected_student].iloc[0]

st.write(f"- **Chuyên cần:** {student_info['Chuyen_can']}")
st.write(f"- **Giữa kỳ:** {student_info['Giua_ky']}")
st.write(f"- **Cuối kỳ:** {student_info['Cuoi_ky']}")
st.write(f"- **Điểm tổng kết:** {student_info['Tong_ket']}")
st.write(f"- **Xếp loại:** {student_info['Xep_loai']}")

st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df['Ho_ten'], df['Tong_ket'], color='skyblue')
ax.set_xlabel('Điểm tổng kết')
ax.set_ylabel('Họ và tên')
ax.set_title('BIỂU ĐỒ ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN')
ax.set_xlim(0, 10)
ax.invert_yaxis()
ax.grid(axis='x', linestyle='--', alpha=0.7)
st.pyplot(fig)

# Hiển thị thông tin người tạo ở cuối trang với chữ nhỏ
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='font-size:12px; color:gray;'>Người tạo: Nguyễn Đức Mạnh | MSSV: [31]</p>", unsafe_allow_html=True)
