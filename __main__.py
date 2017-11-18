import collection

# 페이스북 뉴스 페이지 크롤링(자료 조사)
items = [{'pagename': 'jtbcnews', 'since': '2017-10-01', 'until': '2017-10-16'},
         {'pagename': 'chosun', 'since': '2017-10-01', 'until': '2017-10-16'}]

if __name__ == '__main__':
    # collection
    for item in items:
        resultfile = collection.crawling(**item)
        item['resultfile'] = resultfile

        print(item)

    '''
   # analysis
   for item in items:
       data = analyze.json_to_str(item['resultfile'], 'message')
       item['count'] = analyze.count_wordfreq(data)

   # visualization
   for item in items:
       count = item['count']
       cout_t50 = dict(count.most_common(50))

       filename = '%s_%s_%s' % (item['pagename'], item['since'], item['until'])

       visualize.wordcloud(cout_t50, filename)
       """
       visualize.graph_bar(
           values=list(cout_t50.values()),
           ticks=list(cout_t50.keys()),
           showgrid=True,
           filename=filename,
           showgraph=False
       )
       """
       '''
