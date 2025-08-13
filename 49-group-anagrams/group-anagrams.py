class Solution(object):
    def groupAnagrams(self, strs):
        out={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in out:
                out[key]=[]
            out[key].append(word)
        return list(out.values())