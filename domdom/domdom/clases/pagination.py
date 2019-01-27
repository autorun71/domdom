class Pagination:

    def __init__(self, count, page, n=20, n_pag=2):
        self.pages = self.paginations(count, page, n, n_pag)
        self.design = self.design(self.pages)
        self.sort = self.sort(count, page, n)

    def paginations(self, count, page, n, n_pag):

        pagin = self.paginBegin(count, page, n)

        pagin = self.paginPagesBegin(pagin, count, page, n, n_pag)



        pagin = self.paginEnd(pagin, count, page, n)

        # self.pages.id
        # self.pages[0].aaa=[]

        return pagin

    def sort(self, count, page, n):

        finish = page * n
        start = finish - n + 1

        return (start, finish)


        pass

    def paginBegin(self, count, page, n):
        pagin = []

        if (page != 1 and count > n):
            pagin.append({'title': 'Начало', 'url': '1'})
            pagin.append({'title': 'Назад', 'url': page - 1})
        else:

            pagin.append({'title': 'Начало', 'url': 0})
            pagin.append({'title': 'Назад', 'url': 0})

        return pagin

    def paginEnd(self, pagin, count, page, n):
        endPage = self.endPage(count, n)


        if (page != endPage):
            pagin.append({'title': 'Вперед', 'url': page + 1})
            pagin.append({'title': 'Конец', 'url': endPage})
        else:

            pagin.append({'title': 'Вперед', 'url': 0})
            pagin.append({'title': 'Конец', 'url': 0})

        return pagin

    def endPage(self, count, n):
        endPage = int(count / n)
        ostatok = int(count % n)

        if ostatok > 0:
            endPage += 1

        return endPage


    def paginPagesBegin(self, pagin, count, page, n, n_pag):
        na_skolko = 0
        na_skolkom = 0


        endPage = self.endPage(count, n)


        if (page + n_pag) > endPage:
            na_skolkom = page + n_pag - endPage

        if page > n_pag:
            i = page - n_pag - na_skolkom
        else:
            na_skolko = n_pag - page + 1
            i = page - n_pag + na_skolko - na_skolkom

        while True:
            if (i < 1) :
                i += 1
                continue
            if i >= int(page):
                break
            pagin.append(
                {'title': i, 'url': i}
            )
            i += 1

        pagin.append({'title': page, 'url': '0', 'active': 'Y'})
        pagin = self.paginPagesEnd(pagin, count, page, n, n_pag, na_skolko)
        return pagin

    def paginPagesEnd(self, pagin, count, page, n, n_pag, skolko = 0):

        if (skolko > 0):
            n_pag += skolko

        endPage = self.endPage(count, n)
        i = page + 1

        if endPage > page + n_pag:
            endI = page + n_pag

        else:
            endI = endPage

        while True:
            if i > int(endI):
                break
            pagin.append(
                {'title': i, 'url': i}
            )
            i += 1

        return pagin

    def design(self, pagin):
        ret = ""
        for page in pagin:
            page['url'] = int(page['url'])
            if (page['url'] != 1):
                try:
                    if (page['active']):

                        ret += "<span>"
                        ret += str(page['title'])
                        ret += "</span>"
                except:

                    ret += "<a"
                    ret += " href='?page="+ str(page['url']) + "'" if int(page['url']) != 0 else ''
                    ret += ">"
                    ret += str(page['title'])
                    ret += "</a>"
            else:
                ret += "<a"
                ret += " href='?' "
                ret += ">"
                ret += str(page['title'])
                ret += "</a>"
        return ret