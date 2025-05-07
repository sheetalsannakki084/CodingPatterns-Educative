
class solution:

    def combi(self,digits):
        result=[]
        mapping={"1":[""],
                 "2":["a","b","c"],
                 "3":["d","e","f"],
                 "4":["g","h","i"],
                 "5":["j","k","l"],
                 "6":["m","n","o"],
                 "7":["p","q","r""s"],
                 "8":["t","u","v"],
                 "9":["w","x","y","z"]}
        self.backtrack(0,[],digits,mapping,result)
        return result


    def backtrack(self,index,path,digits,mapping,result):
        if len(path)==len(digits):
            result.append("".join(path))
            return

        possibleletters=mapping[digits[index]]
        if possibleletters is not None:
            for w in possibleletters:
                path.append(w)
                self.backtrack(index + 1, path, digits, mapping, result)
                path.pop()


digits="23"
# digits="4235"----this giv e4 digit combinations
obj=solution()

print(obj.combi(digits))


# # time complexity
# for 1 digit =k option
#     2 digit=k*k=k**2
#     3 digit=k*k*k=k**3
# # so ndigit=k**n adn n recirsive call so time complexity=k**n *n
# spce=o(N)