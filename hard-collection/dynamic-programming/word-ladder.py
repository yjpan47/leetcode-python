class Solution(object):
    
    def is_transformable(word1, word2):
        diff_count = 0
        length = len(word1)
        for i in range(length):
            if word1[i] == word2[i]:
                diff_count += 1
        return diff_count == 1
        
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        mapper = {}
               
        L = len(beginWord)
        
        for i in range(L):
            for word in wordList:
                generic = word[:i] + '*' + word[i+1:]
                if generic not in mapper:
                    mapper[generic] = []
                mapper[generic].append(word)
            
        queue = collections.deque([])
        queue.append((beginWord, 1))
        visited = set()
        
        while len(queue) > 0:
            curr_word, level = queue.popleft()
            visited.add(curr_word)
            if curr_word == endWord:
                return level
            for i in range(L):
                generic = curr_word[:i] + '*' + curr_word[i+1:]
                if generic in mapper:
                    reachable_words = mapper[generic]
                    for word in reachable_words:
                        if word not in visited:
                            queue.append((word, level + 1))
        
        return 0