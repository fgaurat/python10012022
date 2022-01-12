def main():
    a = 2
    b = 3
    c = a/b

    p = f"valeur de {a=}/{b=} = {c:.2%}"
    print(p)
    p = f"valeur de {a=:-3}/{b=:-3} = {c:.2%}"
    print(p)
    p = "valeur de {}/{}={}".format(a,b,c)
    print(p)
    p = "valeur de {2:.2%} = {0}/{1}".format(a,b,c)
    print(p)
    l = [a,b,c]
    p = "valeur de {2:.2%} = {0}/{1}".format(*l)
    print("unpack list",p)
    d = {
        "val_a":a,
        "val_b":b,
        "val_c":c
        }
    p = "valeur de {c:.2%} = {a}/{b}".format(a=d["val_a"],b=d["val_b"],c=d["val_c"])
    print("dict",p)
    # p = "valeur de {c:.2%} = {a}/{b}".format(val_a=d["val_a"],..)
    p = "valeur de {val_c:.2%} = {val_a}/{val_b}".format(**d)
    print("unpack dict",p)
    p = f"valeur de {l[2]:.2%} = {l[0]}/{l[1]}"
    print("fstring list",p)
    p = f"valeur de {d['val_c']:.2%} = {d['val_a']}/{d['val_b']}"
    print("fstring dict",p)

if __name__ == '__main__':
    main()