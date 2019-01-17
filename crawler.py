import scrapy

class netflixSpider(scrapy.Spider):
  name = 'netflix_spider'
  start_urls = ['https://www.netflix.com/br-en/browse/genre/839338']
  visitedLinks = start_urls

  def parse(self, response):
    sections = '.nm-collections-row'
    movies = '.nm-content-horizontal-row-item'
    pageValue = response.css('.nm-collections-header-name::text').extract_first()

    for section in response.css(sections):
      pageLink = section.css('.nm-collections-link::attr(href)').extract_first()

      for movie in section.css(movies):
        genreValue = section.css('.nm-collections-row-name::text').extract_first()
        titleValue = movie.css('a span::text').extract_first()
        thumbnailValue = movie.css('a img::attr(src)').extract_first()
        
        yield {
          'genre': genreValue,
          'title': titleValue,
          'page': pageValue,
          'thumbnail': thumbnailValue,
        }

      if pageLink and pageLink not in self.visitedLinks:
        self.visitedLinks.append(pageLink)
        
        yield scrapy.Request(
          response.urljoin(pageLink),
          callback = self.parse
        )
