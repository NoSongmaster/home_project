'''
    base_url=request.path

    all_count=models.UserInfo.objects.all().count()

    u_page = Page(current_page, 10, base_url,all_count,11)

    user_list=models.UserInfo.objects.all()[u_page.start():u_page.end()]

    return render(request,'my_show.html',{'user_list':user_list,'u_page':u_page})

'''
class Page(object):
    def __init__(self,current_page,per_page_num,base_url,all_count,page_range):
        '''
        :param current_page:        #当前显示页面
        :param per_page_num:        #一个页面显示数据的数量
        :param base_url:            #当前要进行分页的url地址
        :param all_count:           #记录总数
        :param page_range:          #要进行显示下标的数量
        '''
        self.current_page=current_page
        self.per_page_num=per_page_num
        self.base_url=base_url

        a,b=divmod(all_count,per_page_num)      #计算所有的数据需要多少页可以显示
        if b!=0:
            self.all_page=a+1
        else:
            self.all_page = a
        if self.current_page>self.all_page:     #判断用户传入的?p=2121是否超出最大也
            self.current_page=self.all_page
        elif self.current_page< 1:
            self.current_page=1
        self.page_range=page_range
    def start(self):    #当前页待显示起点 num
        return (self.current_page - 1) * self.per_page_num
    def end(self):      #当前页面节点 num
        return self.current_page * self.per_page_num
    def html_str(self):
        str_list=[]
        str_list.append('''
        <nav aria-label="...">
          <ul class="pagination">
                ''')
        if self.current_page<=1:                #判断当前页是否超出最小
            pev = '<li><a href="#">上一页</a></li>'
        else:
            pev ='<li><a href="%s?p=%s">上一页</a></li>'%(self.base_url,self.current_page-1)
        str_list.append(pev)
        # 如果页面的总数小于-可以显示的数量
        if self.all_page < self.current_page:
            start=1
            end=self.all_page+1

        else:   #页面 18   页面总数大于可以显示的数量
            if self.current_page>int(self.page_range/2):    #当前页面大于
                if (self.current_page+self.page_range/2)>self.all_page:
                    start=self.all_page -self.page_range
                    end =self.all_page+1
                else:
                    start=self.current_page - int(self.page_range/2)
                    end = self.current_page+ int(self.page_range/2)+1

            else:       #页码:1,2,3,4,5   当前页为3
                start=1
                end=self.page_range+1
                print(1111)


        # start = self.current_page-5
        # end =self.current_page+6
        print(start,end)

        for i in range(start,end):    #页面选择显示
            if i==self.current_page:
                line='<li class="active"><a href="%s?p=%s">%s</a></li>'%(self.base_url,i,i)     #当前页标记-选中状态
            else:
                line='<li><a href="%s?p=%s">%s</a></li>'%(self.base_url,i,i)
            str_list.append(line)
        if self.current_page>=self.all_page:                    #判断当前页是否超出最大
            nex = '<li><a href="#">下一页</a></li>'
        else:
            nex ='<li><a href="%s?p=%s">下一页</a></li>'%(self.base_url,self.current_page+1)
        str_list.append(nex)
        str_list.append('''
          </ul>
</nav>
        ''')
        return ''.join(str_list)