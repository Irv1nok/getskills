# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return cc
    return f"{'#' * (len(cc) - 4)}{cc[-4:]}"




print(maskify("4556364607935616"))

# def maskify(cc):
#     return "#"*(len(cc)-4) + cc[-4:]