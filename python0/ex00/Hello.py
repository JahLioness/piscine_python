ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
update_tuple = list(ft_tuple)
update_tuple[1] = "France!"
ft_tuple = tuple(update_tuple)
ft_set.update(["Paris!"])
ft_set.remove("tutu!")
ft_dict["Hello"] = "42Paris!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
