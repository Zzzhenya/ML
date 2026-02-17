def main():
    # print("Hello from 00!")
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello" : "titi!"}

    # List
    ft_list[1] = "World!"

    # Tuple
    # because tuples are immutable
    ft_tuple = ("Hello", "Germany!")

    # Set
    # because sets are unordered. 
    # Can't determine the order of insertion or printing, unless printing is sorted
    # when it is sorted, it becomes a list
    # ft_set = sorted(ft_set, reverse=True)
    ft_set.remove("tutu!")
    ft_set.add("Berlin!")

    # Dict
    ft_dict["Hello"] = "42Berlin" 

    

    print(ft_list)
    print(ft_tuple)
    print(ft_set)
    print(ft_dict)

if __name__ == "__main__":
    main()
