from oo_resale_shop import*
from computer import*
def main():
    c = Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    c2 = Computer("Mac Pro (Late 2012)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    mystore = ResaleShop()
    mystore.buy(c)
    mystore.buy(c2)
    mystore.print_inventory(c)
    
    # mystore.sell(c)
    # mystore.print_inventory(c)
    mystore.refurbish(c)
    mystore.print_inventory(c)
   
    mystore.update_os(c, "MAC BURGER")
    mystore.print_inventory(c)
    
main()