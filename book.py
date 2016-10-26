import xlsxwriter

for sheet_name in book.sheet_names():

	temp_sheet_name = sheet_name.lower()

	if temp_sheet_name == tab_name:
		tab_matching = 1

		sheet = book.sheet_by_name(sheet_name)
		temp_sheet_name = file_prefix+part_file_name+"_"+file_type+".xlsx"
		if os.path.exists(detail_path):
			xlsx_file_name = detail_path+"/"+temp_sheet_name
		else:
			xlsx_file_name = dirname+"/"+temp_sheet_name

		new_book = xlsxwriter.Workbook(xlsx_file_name)
		sheet1 = new_book.add_worksheet()


		for row in range(sheet.nrows):

			for col in range(sheet.ncols):  
				sheet1.write(row,col,sheet.cell(row,col).value)     

		new_book.close()
