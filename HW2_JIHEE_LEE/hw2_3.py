'''
3. 문자 'a'가 들어가는 단어를 키보드에서 입력 받아

첫 번째 줄에는'a'까지의 문자열을 출력하고 
두 번째 줄에는 나머지 문자열을 출력하는 프로그램을 작성하라.

Your word: Buffalo
Buffa
lo    '''


word = input('Your word : ')
idx = word.find('a')

print(word[:idx + 1])
print(word[idx + 1:])