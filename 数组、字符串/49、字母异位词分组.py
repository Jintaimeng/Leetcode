from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    results = []
    if len(strs) == 1:
        results.append(strs)
        return results
    res = {''.join(sorted(strs[0])): [strs[0]]}
    for s in range(1, len(strs)):
        if ''.join(sorted(strs[s])) in res.keys():
            res[''.join(sorted(strs[s]))].append(strs[s])
        else:
            res[''.join(sorted(strs[s]))] = [strs[s]]
    for k, v in res.items():
        results.append(v)
    return results

def main():
    strs = ["eat", "", "tan", "", "nat", "bat"]
    res = groupAnagrams(strs)
    print(res)

if __name__ == "__main__":
    main()