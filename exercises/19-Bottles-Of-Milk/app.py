def number_of_bottles():
    for i in range(99,1,-1):
        print("%s bottles of milk on the wall, %s bottles of milk." % (i,i))
        print("Take one down and pass it around, %s bottles of milk on the wall.\n" % (i-1))
    print("1 bottle of milk on the wall, 1 bottle of milk.")
    print("Take one down and pass it around, no more bottles of milk on the wall.\n")
    print("No more bottles of milk on the wall, no more bottles of milk.")
    print("Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()