# GameOfLife-UAS
import random
import keyboard #pip install keyboard
import time
import os

class Cell(object):
    def __init__(self):
        self.status='Dead'

    def set_dead(self):
        self.status='Dead'

    def set_alive(self):
        self.status='Alive'

    def is_alive(self):
        if self.status=='Alive':
            return True
        else:
            return False

    def print_as_symbols(self):
        if self.is_alive():
            return "⬜" #untuk cell hidup
        else:
            return "⬛" #untuk cell mati

class Board(object):
    def __init__(self, rows, columns):
        self.rows=rows
        self.columns=columns
        self.grid=[[Cell() for column_cells in range (self.columns)] for row_cells in range (self.rows)]
        self.generate_board()

    def draw_board(self):
        print("\n*10")
        print("printing board...")
        for row in self.grid:
            for column in row:
                print (column.print_as_symbols(), end='')
            print()

    def generate_board(self):
        for row in self.grid:
            for column in row:
                chance = random.randint(0,2) #0, 1 ,2 = 33%
                if chance==1:
                    column.set_alive()

    def check_neighbour(self, check_row, check_column):
        search_min = -1
        search_max = 2
        neighbour_list = []
        for row in range (search_min, search_max): #syarat cell neighbor hanya 1 cell disekitar main cell
            for column in range (search_min, search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column

                valid_neighbour = True
                if (neighbour_row) == check_row and (neighbour_column) == check_column: #diluar grid = tidak valid
                    valid_neighbour = False
                if (neighbour_row) < 0 or (neighbour_row >= self.rows):
                    valid_neighbour = False
                if (neighbour_column) < 0 or (neighbour_column >= self.columns):
                    valid_neighbour = False
                if valid_neighbour == True:
                    neighbour_list.append(self.grid[neighbour_row][neighbour_column])
        return neighbour_list

    def update_board(self):
        print("updating board...")
        goes_alive = []
        gets_killed = []

        for row in range (len(self.grid)):
            for column in range (len(self.grid[row])):
                check_neighbour = self.check_neighbour(row,column)
                living_neighbours_count = [] #variable penampung cell tetangga hidup
            
                for neighbour_cell in check_neighbour:
                    #mengecek status dari cell tetangga
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)
                
                cell_object=self.grid[row][column]
                status_main_cell = cell_object.is_alive() 
                #pengecekan cell utama
                #jika cell utama hidup, maka cek status cell tetangga
                #Aturan utama game of life
                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

                for cell_items in goes_alive:
                    cell_items.set_alive()

                for cell_items in gets_killed:
                    cell_items.set_dead()

    def print_grid(self):
        for row in self.grid:
            print(row)

def main():
    user_rows = int(input("How many rows? "))
    user_columns = int(input("How many columns? "))

    game_of_life_board = Board(user_rows, user_columns)

    game_of_life_board.draw_board()

    user_action = ''
    while user_action != 'q':
        user_action = input("Press enter to add generation, 'a' to automate board generation, and 'q' to quit")

        if user_action == 'a':
            while keyboard.is_pressed ('s') == False:
                game_of_life_board.update_board()
                game_of_life_board.draw_board()
                print("press 's' to stop automatic generation")
                time.sleep(1)
                os.system("cls")
        
        if user_action == '':
            game_of_life_board.update_board()
            game_of_life_board.draw_board()

if __name__ == "__main__":
    main()
                