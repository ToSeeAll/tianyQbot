def coordinates(_x, _z, _isOldWorld=True):
    """
    _isOldWorld =True:主世界到地狱
    _isOldWorld =False:地狱到主世界
    """
    if _isOldWorld:  # 主世界转地狱坐标
        new_x = int(_x) / 8
        new_z = int(_z) / 8
        return new_x, new_z
    else:  # 地狱转主世界坐标
        new_x = int(_x) * 8
        new_z = int(_z) * 8
        return new_x, new_z
