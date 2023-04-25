import random

class RubiksCube:
    faces = {'up':1,'left':2,'front':3,'right':4,'back':5,'down':6}
    color_map = {'u':'W','l':'O','f':'G','r':'R','b':'B','d':'Y',' ':' '}
    allowed_rotation_types = ["F","f","R","r","U","u","B","b","L","l","D","d"]
    cube = {}
    blank_row = [' ', ' ', ' ']
    
    #initializes cube
    def __init__(self):
        for key,value in self.faces.items():
            if key != 'blank':
                self.cube[key] = self._init_face_(key[0])
    
    #intitializes a face
    def _init_face_(self, color):
        f = []
        for i in range(3):
            l = []
            for j in range(3):
                l.append(color)
            f.append(l)
        return f

    #gets a row (0:2) from a face (from self.faces)
    def _get_row_(self, face_str:str, row_number, direction:bool=True):
        if face_str == 'blank':
            return self.blank_row
        else:
            if direction: return self.cube[face_str][row_number]
            else: return list(reversed(self.cube[face_str][row_number]))

    #gets a column (0:2) from a face (from self.faces)
    def _get_col_(self, face_str:int, col_number, direction:bool=True):
        if face_str == 'blank':
            return self.blank_row
        else:
            l = []
            for row in self.cube[face_str]:
                l.append(row[col_number])
            if direction: return l
            else: return list(reversed(l))

    #allowed_rotation_types = ["F","f","R","r","U","u","B","b","L","l","D","d"]
    def rotate(self, rotation_type:str):
        if rotation_type not in self.allowed_rotation_types: return
        if   rotation_type=='F': self._rotate_F_()
        elif rotation_type=='f': self._rotate_f_()
        elif rotation_type=='R': self._rotate_R_()
        elif rotation_type=='r': self._rotate_r_()
        elif rotation_type=='U': self._rotate_U_()
        elif rotation_type=='u': self._rotate_u_()
        elif rotation_type=='B': self._rotate_B_()
        elif rotation_type=='b': self._rotate_b_()
        elif rotation_type=='L': self._rotate_L_()
        elif rotation_type=='l': self._rotate_l_()
        elif rotation_type=='D': self._rotate_D_()
        elif rotation_type=='d': self._rotate_d_()
    
    #executes a list of rotations (I.E. "b U f u U r L")
    def exec_rotation_list(self, rotation_str:list):
        rotation_list = rotation_str.split(' ')
        for rotation_type in rotation_list:
            self.rotate(rotation_type)

    # Rotate front face clockwise
    def _rotate_F_(self):
        tmp = self._get_col_('right',0,False)
        self._set_col_('right',0,self._get_row_('up',2,True))
        self._set_row_('up',2,self._get_col_('left',2,False))
        self._set_col_('left',2,self._get_row_('down',0,True))
        self._set_row_('down',0,tmp)
        self._rotate_face_('front',True)

    # Rotate front face counter-clockwise
    def _rotate_f_(self):
        tmp = self._get_col_('right',0,True)
        self._set_col_('right',0,self._get_row_('down',0,False))
        self._set_row_('down',0,self._get_col_('left',2,True))
        self._set_col_('left',2,self._get_row_('up',2,False))
        self._set_row_('up',2,tmp)
        self._rotate_face_('front',False)
    
    # Rotate right face clockwise
    def _rotate_R_(self):
        tmp = self._get_col_('back',0,False)
        self._set_col_('back',0,self._get_col_('up',2,False))
        self._set_col_('up',2,self._get_col_('front',2,True))
        self._set_col_('front',2,self._get_col_('down',2,True))
        self._set_col_('down',2,tmp)
        self._rotate_face_('right',True)

    # Rotate right face counter-clockwise
    def _rotate_r_(self):
        tmp = self._get_col_('back',0,False)
        self._set_col_('back',0,self._get_col_('down',2,False))
        self._set_col_('down',2,self._get_col_('front',2,True))
        self._set_col_('front',2,self._get_col_('up',2,True))
        self._set_col_('up',2,tmp)
        self._rotate_face_('right',False)
    
    # Rotate up face clockwise
    def _rotate_U_(self):
        tmp = self._get_row_('left',0,True)
        self._set_row_('left',0,self._get_row_('front',0,True))
        self._set_row_('front',0,self._get_row_('right',0,True))
        self._set_row_('right',0,self._get_row_('back',0,True))
        self._set_row_('back',0,tmp)
        self._rotate_face_('up',True)
        
    # Rotate up face counter-clockwise
    def _rotate_u_(self):
        tmp = self._get_row_('left',0,True)
        self._set_row_('left',0,self._get_row_('back',0,True))
        self._set_row_('back',0,self._get_row_('right',0,True))
        self._set_row_('right',0,self._get_row_('front',0,True))
        self._set_row_('front',0,tmp)
        self._rotate_face_('up',False)
    
    # Rotate back face clockwise
    def _rotate_B_(self):
        tmp = self._get_col_('right',2,True)
        self._set_col_('right',2,self._get_row_('down',2,False))
        self._set_row_('down',2,self._get_col_('left',0,True))
        self._set_col_('left',0,self._get_row_('up',0,False))
        self._set_row_('up',0,tmp)
        self._rotate_face_('back',True)
    
    # Rotate back face counter-clockwise
    def _rotate_b_(self):
        tmp = self._get_col_('right',2,False)
        self._set_col_('right',2,self._get_row_('up',0,True))
        self._set_row_('up',0,self._get_col_('left',0,False))
        self._set_col_('left',0,self._get_row_('down',2,True))
        self._set_row_('down',2,tmp)
        self._rotate_face_('back',False)

    # Rotate left face clockwise
    def _rotate_L_(self):
        tmp = self._get_col_('front',0,True)
        self._set_col_('front',0,self._get_col_('up',0,True))
        self._set_col_('up',0,self._get_col_('back',2,False))
        self._set_col_('back',2,self._get_col_('down',0,False))
        self._set_col_('down',0,tmp)
        self._rotate_face_('left',True)
    
    # Rotate left face counter-clockwise
    def _rotate_l_(self):
        tmp = self._get_col_('front',0,True)
        self._set_col_('front',0,self._get_col_('down',0,True))
        self._set_col_('down',0,self._get_col_('back',2,False))
        self._set_col_('back',2,self._get_col_('up',0,False))
        self._set_col_('up',0,tmp)
        self._rotate_face_('left',False)
    
    # Rotate down face clockwise
    def _rotate_D_(self):
        tmp = self._get_row_('left',2,True)
        self._set_row_('left',2,self._get_row_('back',2,True))
        self._set_row_('back',2,self._get_row_('right',2,True))
        self._set_row_('right',2,self._get_row_('front',2,True))
        self._set_row_('front',2,tmp)
        self._rotate_face_('down',True)
    
    # Rotate down face counter-clockwise
    def _rotate_d_(self):
        tmp = self._get_row_('left',2,True)
        self._set_row_('left',2,self._get_row_('front',2,True))
        self._set_row_('front',2,self._get_row_('right',2,True))
        self._set_row_('right',2,self._get_row_('back',2,True))
        self._set_row_('back',2,tmp)
        self._rotate_face_('down',False)

    #sets a row (0:2) to a face (from self.faces)
    def _set_row_(self, face_str:int, row_number:int, row:list):
        if face_str != 'blank':
            self.cube[face_str][row_number] = row

    #sets a column (0:2) to a face (from self.faces)
    def _set_col_(self, face_str:str, col_number:int, col:list):
        if face_str != 'blank':
            for i, v in enumerate(self.cube[face_str]):
                v[col_number] = col[i]

    #rotates a face (from self.faces) clockwise or counter-clockwise
    def _rotate_face_(self, face_str:str, clockwise:bool):
        face = self.cube[face_str]
        el = list(zip(*reversed(face)))
        new_face = []
        if clockwise:
            new_face = [list(e) for e in el]
        else:
            new_face = [list(e)[::-1] for e in el][::-1]
        self.cube[face_str] = new_face

    #shuffles the cube with random rotations
    def shuffle(self, rotations:int=20):
        l = random.choices(self.allowed_rotation_types,k=rotations)
        s = ' '.join(l)
        self.shuffled_rotation = s
        self.exec_rotation_list(s)

    #returns a 2D string with human readable representation of the cube
    def __str__(self):
        face_sequence = [['blank','up','blank','blank'],
                         ['left','front','right','back'],
                         ['blank','down','blank','blank']]
        s = ''
        s+= '------------------------\n'
        s+= '--------- Cube ---------\n'
        s+= '------------------------\n'
        for i, cs in enumerate(face_sequence):
            for j in range(3):
                for c in cs:
                    for g in self._get_row_(c,j):
                        s+=self.color_map[g][0]
                        s+=' '
                s+='\n'
        s+= '------------------------'
        return s

if __name__ == "__main__":

    cube = RubiksCube()
    cube.shuffle(50)

    print(cube)
    print(cube.shuffled_rotation)
    
