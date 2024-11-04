import os
import random
from os import makedirs, listdir
from time import strftime as st
from openpyxl.utils import get_column_letter
from .models import *
from io import BytesIO
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font
from iris.settings import BASE_DIR


relations = {
    "all_cars": "Автомобілі",
    "all_furnitures": "Меблі",
    "all_bulddings": "Будівлі",
    "all_office_equipments": "Орг.техніка",
    "all_peripheres": "Периферія",
    "all_PC_and_laptops": "Ноутбуки та ПК",
    "all_smartphone_and_tablet": "Смартфони та планшети",
    "all_warehouse_equipment": "Складське обладнання",
    "all_interior_items": "Предмети інтерєру"
}

def inventar_number():
    number = random.randint(10000000000, 99999999999)
    try:
        Inventaryzation.object.get(inv_numb=number)
        inventar_number()
    except:
        return f'{number}'


class ParsExcel(object):
    """this class take a file in a byte code, convert him and pars.
        After that, created new items if this item is not created yet"""

    def __init__(self, file):
        self.file = file

    def parse(self):
        wb = load_workbook(filename=BytesIO(self.file.read()))
        sheet = wb['Sheet1']
        n = 99999  # число рядков
        count = 0
        for i in range(2, n):
            if count >= 5:
                break
            item_atr = []
            for j in range(1, 12):
                a = sheet.cell(row=i, column=j).value
                item_atr.append(a)
            if item_atr[0] == None and item_atr[1] == None:
                count += 1
                continue
            try:
                Inventaryzation.objects.get(serial=item_atr[3])
                continue
            except:
                self.create_item(item_atr)

    def create_item(self, item_atr):
        Inventaryzation.objects.create(
            group=item_atr[0] if item_atr[0] in [i[0] for i in INVENT_GROUP] else '---',
            name=item_atr[1],
            model=item_atr[2],
            serial=item_atr[3] if item_atr[3] != None else '-',
            inv_numb=inventar_number(),
            location=item_atr[4],
            responsible=item_atr[5],
            description=item_atr[6],
            price=item_atr[7] if item_atr[7] != None else 0,
            date_of_purchase=item_atr[8],
            market_price=item_atr[9] if item_atr[9] != None else 0,
            date_of_registration=item_atr[10]
        ).save()


class CreateExcel(object):
    """this class create dir 'downloads', if not excist, in a base path
     and crate excel file with content models date"""

    def __init__(self):
        self.path_to_download = f'{BASE_DIR}/downloads'
        self.workbook = Workbook()
        self.file_name = f"Таблиця_{st('%d')}-{st('%m')}-{st('%y')}_{st('%H')}-{st('%M')}-{st('%S')}"
        self.table_path = self.__create_dir()
        self.sheet = self.workbook.worksheets[0]
        self.line_count = 2
        self.header = (
            ["№п/п", "Група матеріального активу", "Назва матеріального активу", "Модель",
             "Серійний номер/VIN-номер для авто",
             "Інвентарний номер неамтеріального активу", "Місцезнаходження нематеріального активу",
             "Матеріально-відповідальна особа",
             "Опис", "Ціна придбання, з ПДВ", "Дата придбання",
             "Ринкова ціна на дату постановки активу на облік, якщо ціна придбання невідома",
             "Дата оприбуткування при інвентаризації якщо дата придбання невідома"]
        )
        self.__preset()

    def __create_dir(self):
        if "downloads" not in listdir(BASE_DIR):
            makedirs("downloads")
        self.__clear_dir()
        path = f"{self.path_to_download}/{self.file_name}.xlsx"
        return path

    def __preset(self):
        self.sheet.title = f"{st('%d')}_{st('%m')}_{st('%y')}"
        self.sheet.append(self.header)

        for i in range(1, len(self.header) + 1):
            cell_header = self.sheet.cell(row=1, column=i)
            cell_header.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
            cell_header.font = Font(name="Calibri", bold=True, size=9)
            self.sheet.row_dimensions[1].height = 70
            self.sheet.column_dimensions[get_column_letter(i)].width = 20

    def push_objects(self, item_atr_list):

        self.sheet.append(item_atr_list)

        for g in range(1, len(self.header) + 1):
            cell = self.sheet.cell(row=self.line_count, column=g)
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
            cell.font = Font(name="Calibri", size=11)
            self.sheet.row_dimensions[g].height = 30
        self.line_count += 1

    def save_excel(self):
        self.workbook.save(self.table_path)

    def __clear_dir(self):
        if len(listdir(self.path_to_download)) > 0:
            for i in listdir(self.path_to_download):
                os.remove(f'{self.path_to_download}/{i}')