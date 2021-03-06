class Map_Hex(): 
    
    def __init__(self, coord, origin):
        self.ori_cube = self.off_to_ax_coord(origin[0], origin[1])
        self.off_coord = coord
        self.ax_coord = self.off_to_ax_coord(coord[0], coord[1])
        self.description = ("{}{}").format(self.name_chart(coord[0]), self.name_chart(coord[1]))
        self.dist_from_origin = self.distance(origin)

    def off_to_ax_coord(self, col, row):
        x = col
        z = row - int((col - (col % 2))/2)
        y = -x-z
        return [x,y,z]
    
    def distance(self,origin):
        x = abs(self.ori_cube[0] - self.ax_coord[0])
        y = abs(self.ori_cube[1] - self.ax_coord[1])
        z = abs(self.ori_cube[2] - self.ax_coord[2])
        return max(x,y,z)

    def name_chart(self, number):
        chart= {
            0: "00",
            1: "01",
            2: "02",
            3: "03",
            4: "04",
            5: "05",
            6: "06",
            7: "07",
            8: "08",
            9: "09"
            }
        if number > 0 and number < 10: 
            return chart.get(number, "Invalid Number")
        else: 
            return number

