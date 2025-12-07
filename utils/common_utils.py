def convert_rec_cord_to_center_h_w(x_min, y_min, x_max, y_max):
    x_center= (x_min + x_max)/2
    y_center= (y_min + y_max)/2
    w= x_max - x_min
    h= y_max - y_min
    return x_center, y_center, w, h

def convert_rec_cord_to_x_y_h_w(x_min, y_min, x_max, y_max, grid_cell_size):
    
    