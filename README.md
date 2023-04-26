# Facebook Page About Scrapper
Scrappes About section of any Facebook Page

## Support

<a href="https://www.buymeacoffee.com/rexshijaku" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="50" width="180"></a>

# Warning
Due to recent Facebook changes, this script will not be able to extract the promised information. Until the changes are adapted this project will not be functional. 


### Usage
Download facebook_page_about_scrapper folder and include it in your project. Afterwards import extractor function as follows : 
```py
from facebook_page_about_scrapper.scrapper import  getFacebookPageAbout
```
and use it one of two ways : 
```py
about = getFacebookPageAbout("telegraficom")
```
or 
```py
about = getFacebookPageAbout("http://www.facebook.com/telegraficom")
```
the about object (the result object) will have a value like below : 

```js
{ 
   'success': True, 
   'info':  { 'is_verified': True, 
              'phone': {'exists': True, 'value': '038 224 093'}, 
              'website': {'exists': True, 'value': 'https://telegrafi.com/'}, 
              'instagram': {'exists': True, 'value': '@telegrafi'}, 
              'email': {'exists': True, 'value': 'info@telegrafi.com'}
            }
}
```
or in case of some error :
```js
{ 
  'success': False, 
  'message': <HTTPError 404: 'Not Found'>
}
```

### Known Issues
- Can't scrappe age restricted pages

### To-Do
- Create sessions/cookies to access age restricted pages
- Scrappe more fileds

### Support
For general questions about Facebook Page About Scrapper, tweet at @rexshijaku or write me an email on rexhepshijaku@gmail.com.

### Author
##### Rexhep Shijaku
 - Email : rexhepshijaku@gmail.com
 - Twitter : https://twitter.com/rexshijaku
 
### License
MIT License

Copyright (c) 2020 | Rexhep Shijaku

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
