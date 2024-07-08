if __name__=='__main__':
    list=[1,2,390,4,520,6,7999,8,9,0,12,122]
    for i,item in enumerate(list):
        if  i==2 or i==4 or i==6:
            print(f"{item} is at position {i+1}" )
            print("Done")
