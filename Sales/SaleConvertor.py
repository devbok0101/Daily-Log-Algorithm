import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def process_sales_data(input_file, output_file):
    try:
        # Load the Excel file
        data = pd.ExcelFile(input_file).parse('firstSheet')

        # Set header and clean data
        data.columns = data.iloc[0]
        data = data.drop(0).reset_index(drop=True)

        # Rename columns
        column_names = ['매장명', '매뉴명', '메뉴코드', '월간 합계'] + [f'{i}일' for i in range(1, 32)]
        data.columns = column_names

        # Remove commas in sales data and convert to numeric
        for col in column_names[4:]:
            data[col] = pd.to_numeric(data[col].str.replace(',', ''), errors='coerce')

        # Convert to long format
        long_format = data.melt(id_vars=['매뉴명', '메뉴코드'], var_name='일자', value_name='매출량')
        long_format['일자'] = long_format['일자'].str.extract('(\d+)').astype(float).astype('Int64')
        long_format['일자'] = long_format['일자'].apply(lambda x: f"2024-01-{x:02}" if pd.notnull(x) else None)

        # Filter out rows with missing '매뉴명' or '일자' values and reorder columns
        long_format_cleaned = long_format.dropna(subset=['매뉴명', '일자'])
        long_format_cleaned = long_format_cleaned[['일자', '매뉴명', '메뉴코드', '매출량']]

        # Save the cleaned data to a new Excel file
        long_format_cleaned.to_excel(output_file, index=False)
        messagebox.showinfo("완료", f"데이터가 {output_file}에 저장되었습니다.")
    except Exception as e:
        messagebox.showerror("에러", f"오류가 발생했습니다: {e}")

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    output_entry.delete(0, tk.END)
    output_entry.insert(0, file_path)

def process_files():
    input_file = input_entry.get()
    output_file = output_entry.get()
    if input_file and output_file:
        process_sales_data(input_file, output_file)
    else:
        messagebox.showwarning("경고", "입력 및 출력 파일을 모두 선택하세요.")

# GUI 설정
root = tk.Tk()
root.title("매출 데이터 처리")
root.geometry("400x200")

# 입력 파일 선택
tk.Label(root, text="입력 파일:").pack(pady=5)
input_entry = tk.Entry(root, width=40)
input_entry.pack(pady=5)
tk.Button(root, text="파일 선택", command=select_input_file).pack(pady=5)

# 출력 파일 선택
tk.Label(root, text="출력 파일:").pack(pady=5)
output_entry = tk.Entry(root, width=40)
output_entry.pack(pady=5)
tk.Button(root, text="저장 위치 선택", command=select_output_file).pack(pady=5)

# 실행 버튼
tk.Button(root, text="파일 처리 시작", command=process_files, bg="blue", fg="white").pack(pady=20)

root.mainloop()
