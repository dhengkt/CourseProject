def idistance(x, y, pt):
    output_shape = (np.size(y), np.size(x))
    xall = np.resize(x, output_shape)
    yall = np.reshape(np.repeat(y, np.size(x)), output_shape)
    return ( ((xall - pt[0]) ** 2) + ((yall - pt[1]) ** 2) ) ** 0.5