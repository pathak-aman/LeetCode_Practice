# DONE!
class Solution:
    def entityParser(self, text):
        text = text.replace('&quot;','"')
        text = text.replace('&apos;', "'")
        text = text.replace('&frasl;','/')
        text = text.replace('&amp;' , "&")
        text = text.replace('&gt;','>')
        text = text.replace('&lt;' , '<')
        return(text)

obj1 = Solution()
print(obj1.entityParser(text ="and I quote: &quot;...&quot;"))